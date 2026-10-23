"""Reproducible 2-D registration experiments for Week 15 (Parts I-VI).

All transforms use column points (x,y,1): A: fixed -> moving; M: moving -> fixed.
The geometric evaluation grid is never passed to a fitting algorithm.
Run: python scripts/registration_lab.py --all
"""
from __future__ import annotations
import argparse, csv, hashlib, importlib.metadata, json, platform, sys, time
from pathlib import Path
import numpy as np
import cv2
import scipy
from scipy.ndimage import binary_erosion
import skimage
from skimage.registration import phase_cross_correlation
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DATA, FIG, OUT = [ROOT / s for s in ('data', 'figures', 'results')]
SEED, CRITERION_PX, SIZE = 20261031, 2.0, 384
for p in (DATA, FIG, OUT): p.mkdir(exist_ok=True, parents=True)
cv2.setNumThreads(1)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'axes.titlesize':18,
                     'axes.labelsize':15,'xtick.labelsize':12,'ytick.labelsize':12,
                     'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
COLORS = {'baseline':'#8A94A5', 'estimate':'#117F88', 'oracle':'#D59721', 'criterion':'#BA3D50'}

def clean_json(x):
    if isinstance(x, dict): return {k:clean_json(v) for k,v in x.items()}
    if isinstance(x, (list, tuple)): return [clean_json(v) for v in x]
    if isinstance(x, np.ndarray): return clean_json(x.tolist())
    if isinstance(x, np.generic): return x.item()
    return x

def save_json(path, obj):
    path.write_text(json.dumps(clean_json(obj), indent=2, allow_nan=False), encoding='utf-8')

def save_csv(name, rows):
    with (OUT/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

def savefig(name, fig):
    fig.savefig(FIG/name, dpi=190, bbox_inches='tight',facecolor='white')
    plt.close(fig)

def image(name='camera.png', size=SIZE):
    arr = np.array(Image.open(DATA/name).convert('L'), dtype=np.float32)/255
    if size is not None: arr=cv2.resize(arr,(size,size),interpolation=cv2.INTER_AREA)
    return arr

def write_image(name, arr):
    Image.fromarray(np.uint8(np.clip(arr,0,1)*255)).save(DATA/name)

def homogeneous(M): return np.vstack([M,[0,0,1]]) if M.shape==(2,3) else M

def transform(dx=0,dy=0,angle=0,scale=1,shape=(SIZE,SIZE)):
    h,w=shape
    A=cv2.getRotationMatrix2D(((w-1)/2,(h-1)/2),angle,scale)
    A[:,2]+=np.array([dx,dy])
    return homogeneous(A)

def warp(im,M,interpolation=cv2.INTER_LINEAR):
    h,w=im.shape
    return cv2.warpAffine(im,homogeneous(M)[:2].astype(float),(w,h),flags=interpolation,
                          borderMode=cv2.BORDER_CONSTANT,borderValue=0)

def points(M,p):
    return (homogeneous(M)@np.c_[p,np.ones(len(p))].T).T[:,:2]

def grid(shape, A, n=8):
    h,w=shape
    xx,yy=np.meshgrid(np.linspace(.15*w,.85*w,n),np.linspace(.15*h,.85*h,n))
    p=np.c_[xx.ravel(),yy.ravel()]; q=points(A,p)
    keep=(q[:,0]>=2)&(q[:,0]<w-2)&(q[:,1]>=2)&(q[:,1]<h-2)
    return p[keep],q[keep]

def point_error(A,M,shape=(SIZE,SIZE)):
    p,q=grid(shape,A)
    e=np.linalg.norm(points(M,q)-p,axis=1)
    return {'mean_px':float(e.mean()),'median_px':float(np.median(e)),
            'max_px':float(e.max()),'n_points':len(e)}

def mi(a,b,bins=32):
    h=np.histogram2d(a.ravel(),b.ravel(),bins=bins,range=[[0,1],[0,1]])[0]
    p=h/h.sum(); pa=p.sum(axis=1); pb=p.sum(axis=0); den=pa[:,None]*pb[None,:]
    nz=p>0
    return float(np.sum(p[nz]*np.log(p[nz]/den[nz])))

def scores(a,b,mask=None):
    if mask is not None: a,b=a[mask],b[mask]
    a,b=a.astype(float).ravel(),b.astype(float).ravel()
    az,bz=a-a.mean(),b-b.mean(); den=np.linalg.norm(az)*np.linalg.norm(bz)
    return {'mse':float(np.mean((a-b)**2)), 'ncc':float(az@bz/den) if den>0 else 0.,
            'mi_nats':mi(a,b),'valid_pixels':len(a)}

def compare_images(fixed,moving,A,M):
    support=warp(np.ones_like(fixed),A)
    oracle=warp(moving,np.linalg.inv(A)); registered=warp(moving,M)
    # Same pixels for every image-based comparison; no padding/fill participates.
    common=(support>.999)&(warp(support,M)>.999)&(warp(support,np.linalg.inv(A))>.999)
    common=binary_erosion(common,iterations=2)
    return {'baseline':scores(fixed,moving,common), 'estimated':scores(fixed,registered,common),
            'oracle':scores(fixed,oracle,common), 'overlap_fraction':float(common.mean())},registered,common

def overlay(a,b):
    return np.dstack([a,b,a])

def show_images(name, arrays, titles, suptitle=None,cmaps=None):
    fig,axes=plt.subplots(1,len(arrays),figsize=(5*len(arrays),5))
    axes=np.atleast_1d(axes)
    for i,(ax,ar,title) in enumerate(zip(axes,arrays,titles)):
        ax.imshow(ar,cmap='gray' if cmaps is None else cmaps[i],vmin=0,vmax=1)
        ax.set_title(title);ax.axis('off')
    if suptitle: fig.suptitle(suptitle,fontsize=19)
    fig.tight_layout();savefig(name,fig)

def experiment_transform():
    fixed=image();A=transform(24,-15,12,1.03);M=np.linalg.inv(A)
    moving=warp(fixed,A); report,registered,mask=compare_images(fixed,moving,A,M)
    write_image('fixed_384.png',fixed);write_image('transform_moving.png',moving)
    show_images('transform_lab.png',[fixed,moving,overlay(fixed,moving),overlay(fixed,registered)],
                ['Fixed image','Moving: +24, -15 px; 12 degrees','Before: magenta / green','After known inverse'])
    maskshow=overlay(fixed,registered);maskshow[~mask]=[1,.88,.8]
    show_images('valid_overlap.png',[overlay(fixed,registered),maskshow,np.abs(fixed-registered)],
                ['Aligned by known inverse','Orange = excluded pixels','Absolute difference'],
                'Correct geometry still leaves interpolation differences')
    roi=np.s_[170:250,170:250]
    show_images('interpolation_zoom.png',[fixed[roi],registered[roi],np.clip(20*np.abs(fixed[roi]-registered[roi]),0,1)],
                ['Original: same 80 x 80 pixel ROI','After bilinear forward + inverse','Absolute intensity difference x20'],
                'Known inverse restores coordinates; interpolation alters pixel values')
    show_images('fusion_handoff.png',[(fixed+moving)/2,(fixed+registered)/2],
                ['50/50 blend before registration','50/50 blend after known correction'],
                'Alignment reduces double edges before combining information')
    out={'id':'transform','slides':[6,7],'purpose':'Explain transform direction, interpolation, and valid overlap.',
         'n_trials':1,'resolution_px':[SIZE,SIZE],'forward_matrix':A,'inverse_matrix':M,
         'baseline_mean_px':point_error(A,np.eye(3))['mean_px'],'estimated_mean_px':point_error(A,M)['mean_px'],
         'oracle_mean_px':0.,'image_comparison':report,'figures':['transform_lab.png','valid_overlap.png','interpolation_zoom.png','fusion_handoff.png'],
         'interpretation':'The known inverse eliminates coordinate error; resampling cannot restore all lost intensities.'}
    save_json(OUT/'transform.json',out);return clean_json(out)

def orb_register(fixed,moving):
    orb=cv2.ORB_create(nfeatures=1800,fastThreshold=12,edgeThreshold=24)
    a,b=(np.uint8(np.clip(z,0,1)*255) for z in (fixed,moving))
    kf,df=orb.detectAndCompute(a,None);km,dm=orb.detectAndCompute(b,None)
    empty={'fixed_keypoints':len(kf),'moving_keypoints':len(km),'ratio_matches':0,'inliers':0}
    if df is None or dm is None: return None,empty,(kf,km,[],None)
    pairs=cv2.BFMatcher(cv2.NORM_HAMMING).knnMatch(dm,df,k=2)
    good=[p[0] for p in pairs if len(p)==2 and p[0].distance<.75*p[1].distance]
    empty['ratio_matches']=len(good)
    if len(good)<4:return None,empty,(kf,km,good,None)
    src=np.float32([km[m.queryIdx].pt for m in good]);dst=np.float32([kf[m.trainIdx].pt for m in good])
    M,inl=cv2.estimateAffinePartial2D(src,dst,method=cv2.RANSAC,ransacReprojThreshold=3,
                                   maxIters=3000,confidence=.995,refineIters=10)
    empty['inliers']=int(inl.sum()) if inl is not None else 0
    return homogeneous(M) if M is not None else None,empty,(kf,km,good,inl)

def experiment_features(n=15):
    rng=np.random.default_rng(SEED+1);fixed=image();rows=[];examples=None
    for trial in range(n):
        angle=float(rng.uniform(-15,15));scale=float(rng.uniform(.93,1.07))
        dx,dy=rng.uniform(-22,22,2);A=transform(dx,dy,angle,scale)
        moving=warp(fixed,A)
        gain=float(rng.uniform(.9,1.1));offset=float(rng.uniform(-.03,.03))
        moving=np.clip(gain*moving+offset+rng.normal(0,.01,moving.shape),0,1).astype(np.float32)
        cv2.setRNGSeed(SEED+trial)
        start=time.perf_counter();M,counts,detail=orb_register(fixed,moving);elapsed=time.perf_counter()-start
        if M is None: M=np.eye(3)
        error=point_error(A,M);base=point_error(A,np.eye(3));metrics,registered,mask=compare_images(fixed,moving,A,M)
        rows.append({'trial':trial+1,'angle_deg':angle,'scale':scale,'dx_px':dx,'dy_px':dy,
                     'gain':gain,'offset':offset,'noise_sigma':.01,**counts,
                     'baseline_mean_px':base['mean_px'],'estimated_mean_px':error['mean_px'],
                     'oracle_mean_px':0.,'max_error_px':error['max_px'],'evaluation_points':error['n_points'],
                     'success_le_2px':error['mean_px']<=CRITERION_PX,'seconds':elapsed,
                     'common_valid_fraction':metrics['overlap_fraction'],
                     'mse_before':metrics['baseline']['mse'],'mse_after':metrics['estimated']['mse'],
                     'mse_oracle':metrics['oracle']['mse'],'ncc_before':metrics['baseline']['ncc'],
                     'ncc_after':metrics['estimated']['ncc']})
        if trial==0:examples=(fixed,moving,registered,A,M,counts,detail,metrics,error)
    save_csv('feature_trials.csv',rows)
    fixed,moving,registered,A,M,counts,detail,metrics,error=examples
    write_image('feature_moving.png',moving);write_image('feature_registered.png',registered)
    show_images('feature_example.png',[fixed,moving,overlay(fixed,moving),overlay(fixed,registered)],
                ['Fixed image','Controlled moving image','Before registration',f'ORB + RANSAC: {error["mean_px"]:.2f} px'])
    kf,km,good,inl=detail
    select=[i for i in range(len(good)) if inl[i,0]][::max(1,counts['inliers']//45)][:45]
    matches=[good[i] for i in select]
    drawn=cv2.drawMatches(np.uint8(moving*255),km,np.uint8(fixed*255),kf,matches,None,
                          matchColor=(30,200,170),flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    fig,ax=plt.subplots(figsize=(13.5,6));ax.imshow(cv2.cvtColor(drawn,cv2.COLOR_BGR2RGB));ax.axis('off')
    ax.set_title(f'Moving to fixed: {counts["ratio_matches"]} ratio matches, {counts["inliers"]} RANSAC inliers\n'
                 f'{len(matches)} inliers displayed; held-out grid error = {error["mean_px"]:.2f} px')
    savefig('feature_matches.png',fig)
    fig,ax=plt.subplots(figsize=(12,5.5));x=np.arange(1,n+1)
    ax.plot(x,[r['baseline_mean_px'] for r in rows],'o-',c=COLORS['baseline'],label='No registration')
    ax.plot(x,[r['estimated_mean_px'] for r in rows],'o-',c=COLORS['estimate'],label='ORB + RANSAC')
    ax.axhline(CRITERION_PX,c=COLORS['criterion'],ls='--',label='Classroom criterion: 2 px')
    ax.set(xlabel='Controlled trial (same source image)',ylabel='Mean independent-point error (pixels)',
           title=f'Feature registration: {n} controlled transformations; lower is better')
    ax.set_xticks(x);ax.legend(ncol=3,fontsize=12,loc='upper center');ax.set_ylim(bottom=-.7)
    fig.tight_layout();savefig('feature_results.png',fig)
    # An observed failure: featureless inputs cannot provide correspondences.
    uniform=np.full_like(fixed,.5);fail_M,fail_counts,_=orb_register(uniform,warp(uniform,transform(12,-8)))
    out=aggregate('features',[11,12],rows,'ORB + RANSAC similarity transform',
                  ['feature_example.png','feature_matches.png','feature_results.png'])
    out.update({'example':{'trial':1,'forward_matrix':A,'estimated_matrix':M,'counts':counts,
                           'image_comparison':metrics,'point_error':error},
                'failure_example':{'case':'Uniform image','estimated_transform_available':fail_M is not None,
                                   **fail_counts},'records_csv':'feature_trials.csv',
                'settings':{'nfeatures':1800,'ratio_threshold':.75,'ransac_threshold_px':3,'model':'similarity'},
                'interpretation':'Small held-out point error supports geometric recovery for these modest transforms on one textured image; inlier count alone is not proof.'})
    save_json(OUT/'features.json',out);return clean_json(out)

def experiment_intensity(n_per_level=3):
    rng=np.random.default_rng(SEED+2);fixed=image();rows=[];example=None
    # Hanning suppresses zero-padding edges; mean centering reduces constant-offset leakage.
    window=np.outer(np.hanning(SIZE),np.hanning(SIZE)).astype(np.float32)
    for sigma in [0.,.03,.06,.10]:
        for k in range(n_per_level):
            dx,dy=rng.uniform(-18,18,2);gain=float(rng.uniform(.75,1.25));offset=float(rng.uniform(-.06,.06))
            A=transform(dx,dy);moving=np.clip(gain*warp(fixed,A)+offset+rng.normal(0,sigma,fixed.shape),0,1).astype(np.float32)
            start=time.perf_counter()
            shift,_,_=phase_cross_correlation((fixed-fixed.mean())*window,(moving-moving.mean())*window,
                                               upsample_factor=20,normalization='phase')
            elapsed=time.perf_counter()-start;M=transform(float(shift[1]),float(shift[0]))
            e=point_error(A,M);metrics,registered,mask=compare_images(fixed,moving,A,M)
            rows.append({'trial':len(rows)+1,'noise_sigma':sigma,'gain':gain,'offset':offset,'dx_px':dx,'dy_px':dy,
                         'estimated_correction_x_px':float(shift[1]),'estimated_correction_y_px':float(shift[0]),
                         'baseline_mean_px':point_error(A,np.eye(3))['mean_px'],'estimated_mean_px':e['mean_px'],
                         'oracle_mean_px':0.,'success_le_2px':e['mean_px']<=CRITERION_PX,'seconds':elapsed,
                         'common_valid_fraction':metrics['overlap_fraction'],'mse_before':metrics['baseline']['mse'],
                         'mse_after':metrics['estimated']['mse'],'mse_oracle':metrics['oracle']['mse'],
                         'ncc_before':metrics['baseline']['ncc'],'ncc_after':metrics['estimated']['ncc']})
            if sigma==.06 and k==0:example=(moving,registered,A,M,e)
    save_csv('intensity_trials.csv',rows)
    moving,registered,A,M,e=example
    write_image('intensity_moving.png',moving);write_image('intensity_registered.png',registered)
    show_images('intensity_example.png',[fixed,moving,overlay(fixed,moving),overlay(fixed,registered)],
                ['Fixed image','Gain + offset + noise','Before registration',f'Phase correlation: {e["mean_px"]:.2f} px'])
    fig,axes=plt.subplots(1,2,figsize=(13.5,5.5))
    for sigma in [0,.03,.06,.1]:
        vals=[r['estimated_mean_px'] for r in rows if r['noise_sigma']==sigma]
        axes[0].scatter([sigma]*len(vals),vals,s=75,c=COLORS['estimate'],zorder=3)
        axes[0].plot(sigma,np.mean(vals),'_',ms=30,mew=3,c='#123344')
    axes[0].axhline(2,c=COLORS['criterion'],ls='--',label='2 px classroom criterion')
    axes[0].set(xlabel='Added Gaussian noise sigma (intensity 0-1)',ylabel='Mean point error (pixels)',
                title='Each dot = one controlled translation')
    axes[0].legend(fontsize=11)
    axes[1].scatter([r['baseline_mean_px'] for r in rows],[r['estimated_mean_px'] for r in rows],s=65,c=COLORS['estimate'])
    axes[1].set(xlabel='No-registration error (pixels)',ylabel='Estimated error (pixels)',
                title=f'Translation recovery, n = {len(rows)}')
    axes[1].axhline(2,c=COLORS['criterion'],ls='--');axes[1].set_ylim(bottom=0)
    fig.tight_layout();savefig('intensity_results.png',fig)
    out=aggregate('intensity',[15,16],rows,'Windowed phase cross-correlation',
                  ['intensity_example.png','intensity_results.png'])
    out.update({'records_csv':'intensity_trials.csv','noise_levels':[0,.03,.06,.1],
                'settings':{'upsample_factor':20,'normalization':'phase','window':'Hanning, mean-centered','translation_range_px':[-18,18]},
                'example':{'forward_matrix':A,'estimated_matrix':M,'point_error':e},
                'interpretation':'The trials test translation, brightness, and noise only; the method is not a general rotation or deformation solver.'})
    save_json(OUT/'intensity.json',out);return clean_json(out)

def translation_search(fixed,moving,radius=16,bins=32,roi_mask=None,margin=None):
    """Integer exhaustive search on a constant central ROI, avoiding padding bias.

    dx,dy are CORRECTIONS moving->fixed. Each candidate samples moving[y-dy,x-dx].
    Scores use identical fixed pixels and identical sample count for every candidate.
    """
    h,w=fixed.shape;r=radius+2 if margin is None else margin
    if r < radius+2: raise ValueError('Margin must exceed the candidate radius by at least two pixels.')
    a=fixed[r:h-r,r:w-r]
    sel=np.ones_like(a,dtype=bool) if roi_mask is None else roi_mask[r:h-r,r:w-r]
    aa=a[sel];xs=np.arange(-radius,radius+1);ys=xs.copy()
    maps={name:np.zeros((len(ys),len(xs))) for name in ['mse','ncc','mi_nats']}
    az=aa-aa.mean(); an=np.linalg.norm(az)
    for iy,dy in enumerate(ys):
        for ix,dx in enumerate(xs):
            bb=moving[r-dy:h-r-dy,r-dx:w-r-dx][sel]
            bz=bb-bb.mean();den=an*np.linalg.norm(bz)
            maps['mse'][iy,ix]=np.mean((aa-bb)**2)
            maps['ncc'][iy,ix]=float(az@bz/den) if den>0 else 0
            maps['mi_nats'][iy,ix]=mi(aa,bb,bins=bins)
    best={}
    for name,z in maps.items():
        index=np.unravel_index(np.argmin(z) if name=='mse' else np.argmax(z),z.shape)
        best[name]={'dx_px':int(xs[index[1]]),'dy_px':int(ys[index[0]]),'score':float(z[index]),
                    'valid_pixels':int(sel.sum())}
    return best,maps,xs,ys

def plot_search(name,maps,xs,ys,best,true_correction,title):
    fig,axes=plt.subplots(1,3,figsize=(16.5,5))
    names=['mse','ncc','mi_nats'];labels=['MSE: minimize','Signed NCC: maximize','MI (nats): maximize']
    for ax,key,label in zip(axes,names,labels):
        im=ax.imshow(maps[key],origin='lower',extent=[xs[0]-.5,xs[-1]+.5,ys[0]-.5,ys[-1]+.5],aspect='equal',cmap='viridis')
        ax.scatter([true_correction[0]],[true_correction[1]],marker='x',s=140,c='white',linewidth=2.5,label='Known inverse')
        ax.scatter([best[key]['dx_px']],[best[key]['dy_px']],marker='o',s=170,facecolor='none',edgecolor='#FF9C44',linewidth=2.5,label='Metric optimum')
        ax.set(title=label,xlabel='Correction x (pixels)',ylabel='Correction y (pixels)')
        fig.colorbar(im,ax=ax,fraction=.045,pad=.03)
    axes[1].legend(loc='upper center',bbox_to_anchor=(.5,-.2),ncol=2,fontsize=12)
    fig.suptitle(title,fontsize=20);fig.tight_layout();savefig(name,fig)

def experiment_multimodal():
    fixed=image(size=160);A=transform(11,-7,shape=fixed.shape)
    # Deliberate nonlinear inversion, NOT an acquired second modality.
    contrast=(1-fixed)**.65; moving=warp(contrast,A)
    # 29 = candidate radius16 + largest introduced displacement11 + 2 safety pixels.
    # Thus every candidate samples source-supported content, never introduced fill.
    start=time.perf_counter();best,maps,xs,ys=translation_search(fixed,moving,16,margin=29);elapsed=time.perf_counter()-start
    rows=[]
    for method,b in best.items():
        err=float(np.linalg.norm(np.array([b['dx_px'],b['dy_px']])-[-11,7]))
        rows.append({'method':method,'correction_x_px':b['dx_px'],'correction_y_px':b['dy_px'],
                     'metric_score':b['score'],'baseline_mean_px':float(np.hypot(11,7)),
                     'estimated_mean_px':err,'oracle_mean_px':0.,'success_le_2px':err<=2,
                     'search_radius_px':16,'search_step_px':1,'valid_pixels':b['valid_pixels']})
    save_csv('contrast_metric_comparison.csv',rows)
    M=transform(best['mi_nats']['dx_px'],best['mi_nats']['dy_px'],shape=fixed.shape)
    registered=warp(moving,M)
    write_image('simulated_contrast_moving.png',moving);write_image('simulated_contrast_fixed.png',fixed)
    write_image('simulated_contrast_registered.png',registered)
    plot_search('contrast_metric_search.png',maps,xs,ys,best,(-11,7),
                'Simulated contrast inversion: same structures, different intensity relationship')
    show_images('contrast_example.png',[fixed,moving,overlay(fixed,moving),overlay(fixed,registered)],
                ['Fixed (160 x 160)','Simulated contrast + shift','Before','After MI search'])
    # Joint histogram under same bounded central ROI.
    r=29;mask=np.zeros_like(fixed,dtype=bool);mask[r:-r,r:-r]=True
    fig,axes=plt.subplots(1,2,figsize=(11,5))
    for ax,b,title in [(axes[0],moving,'Before alignment'),(axes[1],registered,'After MI alignment')]:
        h,_,_=np.histogram2d(fixed[mask],b[mask],bins=32,range=[[0,1],[0,1]])
        ax.imshow(np.log1p(h.T),origin='lower',extent=[0,1,0,1],cmap='magma',aspect='equal')
        ax.set(title=title,xlabel='Fixed intensity (0-1)',ylabel='Moving intensity (0-1)')
    fig.suptitle('Joint histograms: concentrated dependence can be nonlinear',fontsize=18)
    fig.tight_layout();savefig('joint_histograms.png',fig)
    out={'id':'contrast','slides':[18,19],'purpose':'Compare metric assumptions with an explicitly simulated contrast inversion.',
         'n_trials':1,'resolution_px':[160,160],'forward_shift_xy_px':[11,-7],
         'known_inverse_xy_px':[-11,7],'methods':rows,'search_seconds':elapsed,
         'best':best,'records_csv':'contrast_metric_comparison.csv',
         'baseline_mean_px':float(np.hypot(11,7)),'estimated_mean_px':rows[2]['estimated_mean_px'],
         'oracle_mean_px':0.,'criterion_px':2.,'success_count':int(rows[2]['success_le_2px']),
         'search':{'radius_px':16,'step_px':1,'bins':32,'margin_px':29,'roi':'constant central 102 x 102 pixels; excludes introduced fill for every candidate'},
         'figures':['contrast_example.png','contrast_metric_search.png','joint_histograms.png'],
         'interpretation':'MI recovers the introduced shift here. Signed NCC expects positive correlation; using absolute NCC would be a different metric. One simulated case is not evidence of universal superiority.'}
    if (DATA/'brain_pd.png').exists() and (DATA/'brain_t1.png').exists():
        out['genuine']=experiment_genuine()
    else: out['genuine']={'available':False,'reason':'Public paired teaching images were not yet downloaded.'}
    save_json(OUT/'multimodal.json',out);return clean_json(out)

def experiment_genuine():
    fixed=image('brain_pd.png',None);t1=image('brain_t1.png',None)
    assert fixed.shape==t1.shape,'T1/PD teaching pair must share array shape.'
    # Foreground selection based only on fixed PD; same selected pixels for each search candidate.
    mask=fixed>.07;A=transform(9,-6,shape=fixed.shape);moving=warp(t1,A)
    # 27 = radius16 + introduced displacement9 + 2, shared by BOTH searches.
    native,nmaps,xs,ys=translation_search(fixed,t1,16,roi_mask=mask,margin=27)
    shifted,maps,xs,ys=translation_search(fixed,moving,16,roi_mask=mask,margin=27)
    native_xy=np.array([native['mi_nats']['dx_px'],native['mi_nats']['dy_px']])
    shifted_xy=np.array([shifted['mi_nats']['dx_px'],shifted['mi_nats']['dy_px']])
    recovery=shifted_xy-native_xy;err=float(np.linalg.norm(recovery-[-9,6]))
    registered=warp(moving,transform(*shifted_xy,shape=fixed.shape))
    show_images('genuine_multimodal.png',[fixed,t1,moving,overlay(fixed,registered)],
                ['Public PD MRI teaching image','Public T1 MRI teaching image','T1: introduced +9, -6 px','MI-aligned overlay'])
    plot_search('genuine_metric_search.png',maps,xs,ys,shifted,tuple(native_xy+[-9,6]),
                'Public T1 / PD MRI teaching pair: recovery of an introduced perturbation')
    rows=[]
    for key in ['mse','ncc','mi_nats']:
        nxy=np.array([native[key]['dx_px'],native[key]['dy_px']]);sxy=np.array([shifted[key]['dx_px'],shifted[key]['dy_px']])
        rows.append({'method':key,'native_optimum_x_px':int(nxy[0]),'native_optimum_y_px':int(nxy[1]),
                     'shifted_optimum_x_px':int(sxy[0]),'shifted_optimum_y_px':int(sxy[1]),
                     'recovery_x_px':int((sxy-nxy)[0]),'recovery_y_px':int((sxy-nxy)[1]),
                     'perturbation_recovery_error_px':float(np.linalg.norm((sxy-nxy)-[-9,6])),
                     'valid_pixels':shifted[key]['valid_pixels']})
    save_csv('genuine_multimodal_search.csv',rows)
    return {'available':True,'source':'Public ITK T1 / proton-density MRI teaching pair',
            'resolution_px':list(fixed.shape[::-1]),'introduced_shift_xy_px':[9,-6],
            'native_mi_optimum_xy_px':native_xy,'shifted_mi_optimum_xy_px':shifted_xy,
            'incremental_correction_xy_px':recovery,'perturbation_recovery_error_px':err,
            'introduced_displacement_px':float(np.hypot(9,6)),
            'records_csv':'genuine_multimodal_search.csv','methods':rows,
            'roi':'fixed PD foreground > 0.07, inside constant central ROI with 27-pixel margin; same mask for native and perturbed search',
            'figures':['genuine_multimodal.png','genuine_metric_search.png'],
            'interpretation':'The error measures recovery of the researcher-introduced displacement relative to the native metric optimum. It does not establish native anatomical alignment or clinical accuracy.'}

def aggregate(id,slides,rows,method,figures):
    vals=np.array([r['estimated_mean_px'] for r in rows]);base=np.array([r['baseline_mean_px'] for r in rows])
    return {'id':id,'slides':slides,'method':method,'n_trials':len(rows),
            'resolution_px':[SIZE,SIZE],'baseline_mean_px':float(base.mean()),
            'estimated_mean_px':float(vals.mean()),'estimated_median_px':float(np.median(vals)),
            'estimated_max_px':float(vals.max()),'oracle_mean_px':0.,
            'criterion_px':CRITERION_PX,'success_count':int((vals<=CRITERION_PX).sum()),
            'seconds_median':float(np.median([r['seconds'] for r in rows])),
            'figures':figures,'metric_direction':'Independent-point geometric error, pixels; lower is better.'}

def metadata():
    versions={name:importlib.metadata.version(name) for name in ['numpy','scipy','scikit-image','matplotlib','Pillow','nbformat','nbclient']}
    versions['opencv-python']=cv2.__version__  # Conda OpenCV may have no pip distribution metadata.
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in DATA.glob('*.png')}
    return {'seed':SEED,'criterion_px':CRITERION_PX,
            'criterion_status':'Predefined classroom demonstration criterion; not an industry or clinical standard.',
            'python':sys.version,'platform':platform.platform(),'processor':platform.processor(),
            'versions':versions,'opencv_threads':1,'data_sha256':hashes,
            'datasets':[
                {'file':'data/camera.png','name':'scikit-image camera','source':'https://scikit-image.org/docs/stable/api/skimage.data#skimage.data.camera','license':'CC0; photographer Lav Varshney','original_size_xy':[512,512]},
                {'files':['data/brain_pd.png','data/brain_t1.png'],'name':'ITK T1 / PD MRI teaching pair','source_commit':'50c5b33430e98b91b53fbaae2dd94f0edb2a639a','source':'https://github.com/InsightSoftwareConsortium/ITK/tree/50c5b33430e98b91b53fbaae2dd94f0edb2a639a/Examples/Data','license':'Repository Apache 2.0; original acquisition metadata not established','original_size_xy':[221,257]}
            ],
            'coordinate_convention':'x is column, y is row; forward A fixed->moving; registration M moving->fixed.',
            'evaluation':'Independent 8 x 8 grid in central 70% of fixed image; retained only if forward points remain in image; never used for fitting.',
            'timing':'Hardware-specific registration operation only, excluding image loading and plotting.',
            'repeats':'Controlled perturbations of one camera image, not independent subjects or a population benchmark.'}

def experiment_evaluation():
    saved={name:json.loads((OUT/f'{name}.json').read_text(encoding='utf-8')) for name in ['transform','features','intensity','multimodal']}
    exps=[saved['transform'],saved['features'],saved['intensity'],saved['multimodal']]
    feature=saved['features'];intensity=saved['intensity'];contrast=saved['multimodal']
    fig,ax=plt.subplots(figsize=(12,6));xs=np.arange(2);width=.24
    for shift,key,label,color in [(-width,'baseline_mean_px','No registration',COLORS['baseline']),
                                  (0,'estimated_mean_px','Estimated correction',COLORS['estimate']),
                                  (width,'oracle_mean_px','Known inverse (oracle)',COLORS['oracle'])]:
        bars=ax.bar(xs+shift,[z[key] for z in [feature,intensity]],width,label=label,color=color)
        for bar,z in zip(bars,[feature,intensity]):
            h=z[key];ax.annotate(f'{h:.2f}',(bar.get_x()+bar.get_width()/2,max(h,0)),ha='center',va='bottom',fontsize=14,xytext=(0,4),textcoords='offset points')
    ax.axhline(2,c=COLORS['criterion'],ls='--',label='2 px classroom criterion')
    ax.set_xticks(xs,['ORB + RANSAC\nn = 15 controlled trials','Phase correlation\nn = 12 controlled trials'])
    ax.set(ylabel='Mean independent-point error (pixels)',title='Controlled geometry recovery at 384 x 384; lower is better')
    ax.legend(loc='upper center',ncol=2,fontsize=12);ax.set_ylim(0,max(feature['baseline_mean_px'],intensity['baseline_mean_px'])*1.5)
    fig.tight_layout();savefig('overall_results.png',fig)
    # Visual diagram: the evaluation points differ from fitted keypoints.
    fixed=image();A=transform(24,-15,12,1.03);p,q=grid(fixed.shape,A)
    fig,axes=plt.subplots(1,2,figsize=(12,5.5))
    for ax,im,pts,title in [(axes[0],fixed,p,'Fixed: independent evaluation grid'),(axes[1],warp(fixed,A),q,'Moving: known forward locations')]:
        ax.imshow(im,cmap='gray',vmin=0,vmax=1);ax.scatter(pts[:,0],pts[:,1],s=30,c='#FFB548',edgecolor='black',linewidth=.4)
        ax.set_title(title);ax.axis('off')
    fig.suptitle('Error = distance between estimated correction of q and its known fixed point p',fontsize=16)
    fig.tight_layout();savefig('evaluation_grid.png',fig)
    # Observed featureless failure shown with the successful textured case.
    uniform=np.full((SIZE,SIZE),.5,np.float32)
    show_images('failure_cases.png',[fixed,uniform],['Textured: many usable keypoints','Featureless: 0 detected keypoints'],
                'A registration pipeline must be allowed to report insufficient evidence')
    summary={'metadata':metadata(),'experiments':exps,
             'figure_map':{'transform':'figures/transform_lab.png','overlap':'figures/valid_overlap.png',
                           'features':'figures/feature_results.png','intensity':'figures/intensity_results.png',
                           'contrast':'figures/contrast_metric_search.png','genuine':'figures/genuine_multimodal.png',
                           'evaluation':'figures/evaluation_grid.png','overall':'figures/overall_results.png'},
             'summary_rows':[{'method':z['method'],'n_trials':z['n_trials'],'baseline_mean_px':z['baseline_mean_px'],
                              'estimated_mean_px':z['estimated_mean_px'],'oracle_mean_px':0.,
                              'success_count':z['success_count'],'criterion_px':2.} for z in [feature,intensity]]}
    save_json(OUT/'summary.json',summary);save_json(OUT/'manifest.json',summary['metadata'])
    save_csv('summary.csv',summary['summary_rows'])
    return clean_json(summary)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--all',action='store_true');parser.add_argument('--experiment',choices=['transform','features','intensity','multimodal','evaluation'])
    args=parser.parse_args()
    funcs={'transform':experiment_transform,'features':experiment_features,'intensity':experiment_intensity,'multimodal':experiment_multimodal,'evaluation':experiment_evaluation}
    if args.all:
        for name,fn in funcs.items():
            start=time.perf_counter();out=fn();print(f'{name}: saved in {time.perf_counter()-start:.1f}s',flush=True)
        print(json.dumps(json.loads((OUT/'summary.json').read_text())['summary_rows'],indent=2))
    elif args.experiment:
        print(json.dumps(funcs[args.experiment](),indent=2))
