# Setup and offline use

## Presentation and browser lesson

Download the complete repository. Open the PowerPoint in PowerPoint or a compatible viewer, and double-click `demo/index.html` in Chrome, Edge, Firefox or another modern browser. These finished artifacts do not require Python. The browser lesson has no runtime network dependency. The saved notebook HTML is also available without a running notebook server.

## Python experiments and notebook

The recorded environment used **Python 3.12.7**, CPU execution and the library versions in [requirements.txt](../requirements.txt). Python 3.10–3.12 is the intended range for these pins. Install dependencies once while online; input images and evidence are already bundled.

From the repository root:

```sh
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```sh
source .venv/bin/activate
```

Then:

```sh
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open `notebooks/01_chronological_experiments.ipynb` using this environment's kernel. The notebook reads bundled evidence and performs short calculations; it does not run the full image searches or ORB pipeline.

To execute another copy without overwriting the shipped notebook:

```sh
python -m nbconvert --to notebook --execute notebooks/01_chronological_experiments.ipynb --output-dir notebooks/reruns --ExecutePreprocessor.timeout=180
```

For an optional real-browser check, install Node.js 22+ separately and run:

```sh
node tools/check_demo.cjs
```

The check uses an installed Chrome/Chromium browser, visits all 45 lessons and checks that the embedded presentation path resolves in this repository. Supply the browser executable through the `CHROME_PATH` environment variable if automatic discovery fails. Browser profiles are created in the OS temporary directory, outside the repository. The check does not upload or publish anything.
