/* Optional real-browser verification. Requires Node.js 22+ and Chrome/Chromium.
   Browser profiles and other runtime scratch files stay outside the repository. */
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const net = require('node:net');
const cp = require('node:child_process');
const {pathToFileURL} = require('node:url');
const root = path.resolve(__dirname, '..');
const plan = JSON.parse(fs.readFileSync(path.join(root, 'content/lesson_plan.json'), 'utf8'));
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

function findChrome() {
  const paths = [process.env.CHROME_PATH,
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
    process.env.LOCALAPPDATA && path.join(process.env.LOCALAPPDATA, 'Google/Chrome/Application/chrome.exe'),
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium', '/usr/bin/chromium-browser'];
  const executable = paths.find(candidate => candidate && fs.existsSync(candidate));
  if (!executable) throw Error('Chrome/Chromium not found. Set CHROME_PATH to its executable.');
  return executable;
}

async function freePort() {
  const server = net.createServer();
  await new Promise((resolve, reject) => {server.once('error', reject); server.listen(0, '127.0.0.1', resolve);});
  const port = server.address().port;
  await new Promise(resolve => server.close(resolve));
  return port;
}

(async () => {
  let child, ws;
  const tests = [], errors = [], requests = [];
  const check = (name, condition) => {tests.push({name, passed: Boolean(condition)}); if (!condition) throw Error(name);};
  try {
    const browser = findChrome();
    const port = await freePort();
    const temporary = fs.mkdtempSync(path.join(os.tmpdir(), 'registration-browser-'));
    child = cp.spawn(browser, ['--headless=new', '--disable-gpu', '--no-first-run',
      '--disable-extensions', '--disable-background-networking',
      `--user-data-dir=${temporary}`, `--remote-debugging-port=${port}`, 'about:blank'],
      {windowsHide: true, stdio: 'ignore'});
    let targets;
    for (let i = 0; i < 100; i++) {
      try {targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); if (targets.length) break;} catch {}
      await delay(100);
    }
    if (!targets?.length) throw Error('Browser debugging session did not start.');
    ws = new WebSocket(targets.find(target => target.type === 'page').webSocketDebuggerUrl);
    await new Promise((resolve, reject) => {ws.onopen = resolve; ws.onerror = reject;});
    let sequence = 0;
    const pending = new Map();
    ws.onmessage = event => {
      const message = JSON.parse(event.data);
      if (message.id) {
        const task = pending.get(message.id); pending.delete(message.id);
        if (!task) return;
        clearTimeout(task.timeout);
        message.error ? task.reject(Error(JSON.stringify(message.error))) : task.resolve(message.result);
      } else if (message.method === 'Runtime.exceptionThrown' ||
          message.method === 'Runtime.consoleAPICalled' && message.params.type === 'error') {
        errors.push(message.method);
      } else if (message.method === 'Network.requestWillBeSent') {
        requests.push(message.params.request.url);
      }
    };
    const call = (method, params = {}) => new Promise((resolve, reject) => {
      const id = ++sequence;
      const timeout = setTimeout(() => {pending.delete(id); reject(Error('Browser command timeout: ' + method));}, 15000);
      pending.set(id, {resolve, reject, timeout});
      ws.send(JSON.stringify({id, method, params}));
    });
    const evaluate = async expression => {
      const value = await call('Runtime.evaluate', {expression, returnByValue: true, awaitPromise: true});
      if (value.exceptionDetails) throw Error('Browser evaluation failed.');
      return value.result.value;
    };
    const waitFor = async expression => {
      for (let i = 0; i < 160; i++) {if (await evaluate(expression)) return; await delay(60);}
      throw Error('The offline demo did not reach the expected state.');
    };
    await call('Runtime.enable'); await call('Page.enable'); await call('Network.enable');
    const artifact = pathToFileURL(path.join(root, 'demo/index.html')).href;
    await call('Page.navigate', {url: artifact});
    await waitFor("!!window.ChronologicalLab && document.documentElement.dataset.ready === 'true'");
    check('All three embedded applications are ready', await evaluate('ChronologicalLab.getReady().length === 3'));
    check('Default route is the presentation route', await evaluate("document.getElementById('routeMode').value === 'main'"));
    const deckRelative = await evaluate('ChronologicalLab.plan.deck.relative_from_demo');
    check('Embedded presentation path resolves', fs.existsSync(path.resolve(root, 'demo', deckRelative)));
    await evaluate("document.getElementById('routeMode').value='all'; document.getElementById('routeMode').dispatchEvent(new Event('change'))");
    for (const step of plan.steps) {
      await evaluate(`ChronologicalLab.open(${JSON.stringify(step.id)})`);
      await waitFor(`document.documentElement.dataset.activeStep === ${JSON.stringify(step.id)}`);
      const current = await evaluate('ChronologicalLab.getCurrent()');
      check('Lesson ' + step.id + ' preserves its slide references', JSON.stringify(current.slides) === JSON.stringify(step.slides));
      check('Lesson ' + step.id + ' explains purpose and interpretation', await evaluate("['purpose','do','watch','meaning'].every(id=>document.getElementById(id).textContent.trim().length>0)"));
    }
    check('All 45 ordered lessons were visited', plan.steps.length === 45);
    check('No browser JavaScript errors', errors.length === 0);
    check('No runtime internet requests', !requests.some(url => /^https?:/i.test(url)));
    check('No sibling runtime file requests', !requests.some(url => url.startsWith('file:') && url.split('#')[0] !== artifact));
    const report = {passed: true, method: 'Actual headless Chrome/Chromium on the relocated repository demo',
      lesson_count: plan.steps.length, tests, javascript_errors: errors.length,
      external_requests: 0, sibling_file_requests: 0,
      limitation: 'Navigation/reference smoke test; it does not replace the original detailed numerical and interaction checks.'};
    fs.writeFileSync(path.join(root, 'docs/browser_validation.json'), JSON.stringify(report, null, 2) + '\n');
    console.log(JSON.stringify({passed: true, lessons: plan.steps.length, checks: tests.length}));
  } catch (error) {
    console.error(error.message); process.exitCode = 1;
  } finally {
    if (ws) ws.close();
    if (child) child.kill();
  }
})();
