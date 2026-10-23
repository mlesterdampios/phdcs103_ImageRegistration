"""Six small, executed research connections for Parts I--VI.

These are controlled method-level reproductions/adaptations, NOT replications of
the papers' benchmarks, clinical datasets, timing, subjects or complete systems.
Run from any folder: python research/scripts/reproduce_studies.py
All experiment data and results are bundled for offline use.
"""
from pathlib import Path
import csv
import hashlib
import json
import math
import shutil
import platform

import cv2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.ndimage import fourier_shift
import skimage
from skimage.registration import phase_cross_correlation
from skimage.transform import SimilarityTransform

ROOT=Path(__file__).resolve().parents[1]
DATA,RESULTS,FIGURES=ROOT/"data",ROOT/"results",ROOT/"figures"
for directory in [DATA,RESULTS,FIGURES]:
    directory.mkdir(exist_ok=True)
SEED=20261023
cv2.setNumThreads(1)
plt.rcParams.update({"font.size":11,"axes.titlesize":13,"figure.dpi":130,
                     "axes.spines.top":False,"axes.spines.right":False})
BLUE,ORANGE,GREEN,RED="#1764a0","#c15b19","#21764c","#aa3344"


def clean(value):
    """Convert NumPy types to strict JSON, using null for nonfinite answers."""
    if isinstance(value,np.ndarray):return clean(value.tolist())
    if isinstance(value,dict):return {str(k):clean(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [clean(v) for v in value]
    if isinstance(value,(np.integer,)):return int(value)
    if isinstance(value,(np.bool_,)):return bool(value)
    if isinstance(value,(float,np.floating)):return float(value) if math.isfinite(float(value)) else None
    return value


def save_json(path,value):
    path.write_text(json.dumps(clean(value),indent=2,allow_nan=False),encoding="utf-8")


def save_csv(name,rows):
    with (RESULTS/name).open("w",newline="",encoding="utf-8") as handle:
        writer=csv.DictWriter(handle,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(clean(rows))


def save_image(name,image):
    pixels=np.clip(np.asarray(image)*255 if np.asarray(image).dtype.kind=="f" else image,0,255).astype(np.uint8)
    cv2.imwrite(str(DATA/name),pixels)
    return "data/"+name


def camera(size):
    target=DATA/"camera.png"
    if not target.exists():
        for source in [ROOT.parent/"data/camera.png",ROOT.parent/"beginner/data/camera.png"]:
            if source.exists():shutil.copyfile(source,target);break
    image=cv2.imread(str(target),cv2.IMREAD_GRAYSCALE)
    if image is None:raise FileNotFoundError("The bundled CC0 camera photograph is needed.")
    return cv2.resize(image,(size,size),interpolation=cv2.INTER_AREA)


def apply(points,matrix):
    """Apply a 2-D forward or inverse transform to x/y addresses."""
    points=np.asarray(points,float);matrix=np.asarray(matrix,float)
    return points@matrix[:2,:2].T+matrix[:2,2]


def inverse(matrix):
    matrix=np.asarray(matrix,float)
    if matrix.shape==(2,3):matrix=np.vstack([matrix,[0,0,1]])
    return np.linalg.inv(matrix)


def check_grid(truth,estimate,size=256):
    """Twenty-five unused points evaluate inverse recovery in FIXED pixels."""
    positions=np.linspace(size*.2,size*.8,5)
    points=np.array([[x,y] for y in positions for x in positions])
    moved=apply(points,truth)
    recovered=apply(moved,inverse(estimate))
    distances=np.linalg.norm(recovered-points,axis=1)
    return {"fixed_points":points.tolist(),"true_moving_points":moved.tolist(),
            "recovered_points":recovered.tolist(),"distances_fixed_px":distances.tolist(),
            "mean_error_fixed_px":float(distances.mean()),"maximum_error_fixed_px":float(distances.max()),
            "used_for_fitting":False,"number_of_points":25}


def scores(fixed,moving,bins=32):
    """A fixed histogram estimator; bins and sample size must accompany MI/NMI.

    H is entropy: -sum(p*ln(p)). The 0-count terms contribute zero.
    MI=H(F)+H(M)-H(F,M). NMI=(H(F)+H(M))/H(F,M).
    A constant pair has joint entropy zero, so NMI is undefined, not zero.
    """
    a=np.asarray(fixed,float).ravel();b=np.asarray(moving,float).ravel()
    if len(a)!=len(b) or len(a)==0:raise ValueError("Equal nonempty samples are required.")
    da=a-a.mean();db=b-b.mean();den=np.linalg.norm(da)*np.linalg.norm(db)
    ncc=float(np.clip(np.dot(da,db)/den,-1,1)) if den>0 else None
    ia=np.minimum(bins-1,np.floor(np.clip(a,0,1)*bins).astype(int))
    ib=np.minimum(bins-1,np.floor(np.clip(b,0,1)*bins).astype(int))
    counts=np.bincount(ia*bins+ib,minlength=bins*bins).reshape(bins,bins)
    p=counts/counts.sum()
    def entropy(prob):
        nonzero=prob[prob>0]
        return float(-np.sum(nonzero*np.log(nonzero)))
    hf,hm,hjoint=entropy(p.sum(axis=1)),entropy(p.sum(axis=0)),entropy(p)
    mi=hf+hm-hjoint
    if abs(mi)<1e-14:mi=0.0
    return {"mse":float(np.mean((a-b)**2)),"signed_ncc":ncc,"mi_nats":mi,
            "nmi":(hf+hm)/hjoint if hjoint>0 else None,
            "fixed_entropy_nats":hf,"moving_entropy_nats":hm,"joint_entropy_nats":hjoint,
            "samples":len(a)}


def r1():
    """Umeyama's least-squares similarity idea using scikit-image's implementation."""
    rng=np.random.default_rng(SEED+1)
    grid=np.array([[x,y] for y in np.linspace(32,224,4) for x in np.linspace(32,224,4)])
    clustered=128+(grid-128)/48  # Same layout, but squeezed into only 4x4 pixels.
    normal=rng.normal(size=grid.shape)
    true=SimilarityTransform(scale=1.04,rotation=np.deg2rad(8),translation=(7,-5)).params
    rows=[];traces=[]
    for layout,points in [("spread",grid),("clustered",clustered)]:
        for sigma in [0.,.5,2.]:
            moved=apply(points,true)+sigma*normal
            model=SimilarityTransform()
            success=model.estimate(points,moved)
            if not success or not np.isfinite(model.params).all():raise RuntimeError("Unexpected nondegenerate fit failure.")
            check=check_grid(true,model.params)
            fit_residuals=np.linalg.norm(apply(points,model.params)-moved,axis=1)
            row={"layout":layout,"sigma_per_coordinate_px":sigma,"fit_points":16,
                 "mean_fit_residual_moving_px":float(fit_residuals.mean()),
                 "independent_mean_error_fixed_px":check["mean_error_fixed_px"],
                 "estimated_scale":float(model.scale),"estimated_rotation_degrees":float(np.rad2deg(model.rotation))}
            rows.append(row)
            traces.append({"case_id":f"{layout}_sigma_{str(sigma).replace('.','p')}","row":row,
                           "fixed_fit_points":points,"observed_moving_fit_points":moved,
                           "estimated_forward":model.params,"independent_check":check})
    invalid=SimilarityTransform()
    with np.errstate(invalid="ignore",divide="ignore"):
        success=invalid.estimate(np.ones((4,2)),np.ones((4,2)))
    degenerate={"case":"all four reference points at the same location","success":bool(success),
                "finite_matrix":bool(np.isfinite(invalid.params).all()),
                "interpretation":"Cannot infer scale or rotation from zero spatial spread; report failure."}
    result={"method_status":"method-level reproduction using a public library, new synthetic points",
            "settings":{"sigma_values":[0,.5,2],"point_noise":"fixed normal draws, each moving x/y coordinate",
                        "fixed_fit_points":grid,"clustered_fit_points":clustered,"normal_offsets":normal,
                        "independent_points":check_grid(true,true)["fixed_points"],"fit_point_count":16,
                        "known_scale":1.04,"known_rotation_degrees_skimage":8,"known_translation_xy":[7,-5]},
            "known_forward":true,"rows":rows,"traces":traces,"degenerate_check":degenerate,"figures":{}}
    save_csv("R1_point_layout_noise.csv",rows);return result


def r2():
    """Actual ORB extraction, Hamming ratio matching and a robust similarity fit."""
    fixed=camera(256);fixed_path=save_image("R2_fixed.png",fixed)
    detector=cv2.ORB_create(nfeatures=1000,WTA_K=2)
    kf,df=detector.detectAndCompute(fixed,None)
    rows=[];case_traces=[]
    for angle in [0,15,45,75]:
        for blur in [0.,1.5,3.]:
            case_id=f"angle_{angle}_blur_{str(blur).replace('.','p')}"
            truth=cv2.getRotationMatrix2D((128,128),angle,1.03);truth[:,2]+=[8,-6]
            moving=cv2.warpAffine(fixed,truth,(256,256),flags=cv2.INTER_LINEAR)
            if blur>0:moving=cv2.GaussianBlur(moving,(0,0),sigmaX=blur,sigmaY=blur)
            image_path=save_image("R2_"+case_id+".png",moving)
            km,dm=detector.detectAndCompute(moving,None)
            match_records=[];matched=[]
            if df is not None and dm is not None and len(dm)>=2:
                choices=cv2.BFMatcher(cv2.NORM_HAMMING).knnMatch(df,dm,k=2)
                for pair in choices:
                    if len(pair)!=2:continue
                    best,second=pair
                    if second.distance>0 and best.distance<.75*second.distance:
                        matched.append(best)
                        match_records.append({"query_idx":best.queryIdx,"train_idx":best.trainIdx,
                                              "best_hamming":int(best.distance),"second_hamming":int(second.distance),
                                              "ratio":best.distance/second.distance,
                                              "fixed_xy":list(kf[best.queryIdx].pt),"moving_xy":list(km[best.trainIdx].pt)})
            estimate=None;mask=None;check=None
            if len(matched)>=3:
                source=np.array([kf[m.queryIdx].pt for m in matched],np.float32)
                target=np.array([km[m.trainIdx].pt for m in matched],np.float32)
                cv2.setRNGSeed(SEED)
                estimate,mask=cv2.estimateAffinePartial2D(source,target,method=cv2.RANSAC,ransacReprojThreshold=3,
                                                         maxIters=3000,confidence=.99,refineIters=10)
                if estimate is not None:
                    mask=mask.ravel().astype(bool);check=check_grid(truth,estimate)
                    residuals=np.linalg.norm(apply(source,estimate)-target,axis=1)
                    for r,flag,gap in zip(match_records,mask,residuals):
                        r.update({"returned_ransac_inlier":bool(flag),"final_forward_residual_moving_px":float(gap)})
            row={"case_id":case_id,"rotation_degrees_opencv":angle,"moving_blur_sigma_px":blur,
                 "fixed_keypoints":len(kf),"moving_keypoints":len(km),"ratio_pass_matches":len(matched),
                 "returned_ransac_inliers":int(mask.sum()) if mask is not None else 0,
                 "independent_mean_error_fixed_px":check["mean_error_fixed_px"] if check else None,
                 "status":"measured" if check else "insufficient evidence / fit failure"}
            rows.append(row)
            case_trace={"case_id":case_id,"row":row,"fixed_image":fixed_path,"moving_image":image_path,
                        "known_forward":truth,"estimated_forward":estimate,
                        "estimated_inverse":inverse(estimate) if estimate is not None else None,
                        "fixed_keypoints_xy":[list(k.pt) for k in kf],"moving_keypoints_xy":[list(k.pt) for k in km],
                        "fixed_descriptor_bytes":df,"moving_descriptor_bytes":dm,
                        "matches":match_records,"independent_check":check}
            save_json(RESULTS/("R2_trace_"+case_id+".json"),case_trace)
            # Browser stores points/matches plus just one real fingerprint, not all bytes.
            thin={k:v for k,v in case_trace.items() if k not in ["fixed_descriptor_bytes","moving_descriptor_bytes"]}
            if matched:
                a=df[matched[0].queryIdx];b=dm[matched[0].trainIdx]
                thin["real_descriptor_example"]={"fixed_bytes":a,"moving_bytes":b,
                    "hamming":int(np.unpackbits(np.bitwise_xor(a,b)).sum())}
            case_traces.append(thin)
    result={"method_status":"method-level public-library pipeline; not original ORB benchmark replication",
            "settings":{"image_size":256,"nfeatures_max":1000,"WTA_K":2,"descriptor_bytes":32,
                        "distance":"Hamming bit count","ratio_cutoff":.75,"forward_threshold_moving_px":3,
                        "max_iterations":3000,"confidence":.99,"refine_iterations":10,
                        "angles_degrees_opencv":[0,15,45,75],"moving_gaussian_blur_sigma_px":[0,1.5,3],
                        "known_scale":1.03,"added_translation_xy":[8,-6],"center_xy":[128,128]},
            "default_case_id":rows[0]["case_id"],"rows":rows,"cases":case_traces,
            "mask_note":"Returned masks precede final refinement; final residuals can cross the threshold after adjustment.",
            "browser_notice":"Saved actual Python/OpenCV run; browser selection replays results, it does not rerun ORB.","figures":{}}
    save_csv("R2_orb_rotation_blur.csv",rows);return result


def r3():
    """Guizar-Sicairos upsampled-DFT idea through phase_cross_correlation."""
    fixed=camera(256)/255.0
    generated=np.array([5.4,-3.7])  # y then x, as required by array APIs.
    expected=-generated
    fft_fixed=np.fft.fftn(fixed)
    fft_moving=fourier_shift(fft_fixed,generated)
    periodic=np.fft.ifftn(fft_moving)
    rng=np.random.default_rng(SEED+3)
    noisy=periodic.real+rng.normal(0,.03,fixed.shape)
    occluded=periodic.real.copy();occluded[80:176,80:176]=0
    rotation=cv2.getRotationMatrix2D((128,128),5,1)
    turned=cv2.warpAffine(fixed,rotation,(256,256),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_WRAP)
    rotated=np.fft.ifftn(fourier_shift(np.fft.fftn(turned),generated)).real
    conditions={"clean":fft_moving,"noise":np.fft.fftn(noisy),
                "occluded":np.fft.fftn(occluded),"rotated":np.fft.fftn(rotated)}
    rows=[];images={"fixed":save_image("R3_fixed.png",fixed)}
    for name,fft_variant in conditions.items():
        images[name]=save_image("R3_"+name+".png",np.fft.ifftn(fft_variant).real)
        for upsample in [1,10,100]:
            shift,normalized_error,phase=phase_cross_correlation(fft_fixed,fft_variant,space="fourier",
                                                               upsample_factor=upsample,normalization=None)
            rows.append({"condition":name,"upsample_factor":upsample,"nominal_grid_spacing_px":1/upsample,
                         "estimated_correction_y_px":float(shift[0]),"estimated_correction_x_px":float(shift[1]),
                         "translation_component_error_px":float(np.linalg.norm(shift-expected)),
                         "pure_translation_assumption_satisfied":name!="rotated"})
    result={"method_status":"method-level reproduction using public upsampled-DFT implementation, new periodic images",
            "settings":{"generated_shift_yx_px":generated,"known_correction_yx_px":expected,
                        "upsample_factors":[1,10,100],"boundary":"periodic Fourier translation",
                        "normalization":None,"noise_brightness_sigma":.03,
                        "occlusion_rectangle_yx":[80,176,80,176],"extra_rotation_degrees":5},
            "rows":rows,"images":images,"figures":{},
            "limitation":"Higher upsampling sets numerical spacing, not guaranteed accuracy. Rotated case violates translation-only geometry: reported error checks the translation component, not complete geometric recovery."}
    save_csv("R3_phase_subpixel.csv",rows);return result


def r4():
    """MI paper principle adapted to transparent 32-bin integer exhaustive search."""
    fixed=camera(96)/255.0;truth=[6,-4]
    affine=np.array([[1,0,truth[0]],[0,1,truth[1]]],float)
    moving=cv2.warpAffine(fixed,affine,(96,96),flags=cv2.INTER_NEAREST)
    yy,xx=np.mgrid[20:76,20:76]
    reference=fixed[yy,xx]
    scans={};rows=[];images={"fixed":save_image("R4_fixed.png",fixed)}
    for contrast in ["same","inverted","nonlinear_inverted"]:
        changed=moving.copy() if contrast=="same" else 1-moving if contrast=="inverted" else 1-moving**.7
        images[contrast]=save_image("R4_"+contrast+".png",changed)
        scan=[]
        for v in range(-10,11):
            for u in range(-10,11):
                record={"sampling_x_px":u,"sampling_y_px":v}
                record.update(scores(reference,changed[yy+v,xx+u]))
                scan.append(record)
        scans[contrast]=scan
        true_record=next(r for r in scan if r["sampling_x_px"]==6 and r["sampling_y_px"]==-4)
        for metric,minimize in [("mse",True),("signed_ncc",False),("mi_nats",False)]:
            eligible=[r for r in scan if r[metric] is not None]
            best=(min if minimize else max)(r[metric] for r in eligible)
            ties=[r for r in eligible if abs(r[metric]-best)<1e-12]
            chosen=ties[0];u,v=chosen["sampling_x_px"],chosen["sampling_y_px"]
            rows.append({"contrast":contrast,"metric":metric,"best_sampling_x_px":u,"best_sampling_y_px":v,
                         "geometric_error_px":float(np.hypot(u-6,v+4)),"best_score":best,"score_at_known_truth":true_record[metric],
                         "number_of_tied_best_candidates":len(ties),"same_valid_samples":reference.size})
        save_csv("R4_scan_"+contrast+".csv",scan)
    result={"method_status":"teaching adaptation: fixed 32-bin histogram and exhaustive integer search; NOT the paper's Parzen estimator or optimizer",
            "settings":{"image_size":96,"generated_forward_xy_px":truth,"known_sampling_offset_xy_px":truth,
                        "applied_point_correction_xy_px":[-6,4],"search_each_axis":[-10,10],"total_candidates":441,
                        "fixed_roi_xy_inclusive":[20,75,20,75],"samples_per_candidate":3136,"histogram_bins":32,
                        "logarithm":"natural","contrast_rules":{"same":"v","inverted":"1-v","nonlinear_inverted":"1-v**0.7"}},
            "rows":rows,"scans":scans,"images":images,"figures":{}}
    save_csv("R4_metric_search_summary.csv",rows);return result


def r5():
    """Studholme NMI formula illustrated while overlap crops change sample content."""
    fixed=camera(128)/255.0
    moving=cv2.warpAffine(fixed,np.array([[1,0,8],[0,1,0]],float),(128,128),flags=cv2.INTER_NEAREST)
    rows=[]
    for width in [96,72,48,24,12,6]:
        start=64-width//2
        yy,xx=np.mgrid[16:112,start:start+width]
        for offset in [0,8,16]:
            result=scores(fixed[yy,xx],moving[yy,xx+offset])
            rows.append({"overlap_width_px":width,"overlap_height_px":96,"overlap_fraction_of_96x96":width/96,
                         "sampling_offset_x_px":offset,"geometric_error_px":abs(offset-8),
                         "samples":result["samples"],"mi_nats":result["mi_nats"],"nmi":result["nmi"],
                         "fixed_entropy_nats":result["fixed_entropy_nats"],"moving_entropy_nats":result["moving_entropy_nats"],
                         "joint_entropy_nats":result["joint_entropy_nats"]})
    constant=scores(np.zeros((8,8)),np.zeros((8,8)))
    result={"method_status":"formula-level teaching adaptation on a public photo; not original 3-D multimodal experiments",
            "settings":{"image_size":128,"known_sampling_x_px":8,"tested_offsets_x_px":[0,8,16],
                        "crop_widths_px":[96,72,48,24,12,6],"fixed_crop_height_px":96,"center_x":64,
                        "bins":32,"nmi_formula":"(H(F)+H(M))/H(F,M)","entropy_units":"nats"},
            "rows":rows,"constant_failure":{"joint_entropy_nats":constant["joint_entropy_nats"],
                       "mi_nats":constant["mi_nats"],"nmi":constant["nmi"],
                       "message":"Both arrays are constant: joint entropy is zero; NMI cannot be calculated."},
            "limitation":"Cropping changes both sample count and foreground composition. This is not an isolated sample-count-only experiment, nor a guarantee that NMI is overlap-invariant or always better.",
            "figures":{}}
    save_csv("R5_overlap_mi_nmi.csv",rows);return result


def r6():
    """Rohlfing's warning illustrated with exact periodic ambiguity, not clinical data."""
    period=[0,0,0,0,1,1,1,1]
    row=np.tile(period,16).astype(float)
    fixed=np.tile(row,(64,1));moving=np.roll(fixed,5,axis=1)
    samples=np.arange(128)
    rows=[]
    for offset in range(-20,21):
        metric=scores(fixed,moving[:,(samples+offset)%128],bins=2)
        rows.append({"sampling_offset_x_px":offset,"applied_correction_x_px":-offset,
                     "known_sampling_x_px":5,"independent_geometric_error_px":abs(offset-5),
                     "mse":metric["mse"],"signed_ncc":metric["signed_ncc"],
                     "mi_nats":metric["mi_nats"],"nmi":metric["nmi"]})
    result={"method_status":"new counterexample illustrating a published evaluation warning; NOT a reproduction of the paper's 3-D clinical study",
            "settings":{"period_pixels":8,"period_values":period,"row_values":row,"image_shape_hw":[64,128],
                        "generated_forward_x_px":5,"known_sampling_x_px":5,"wrong_lookalike_sampling_x_px":13,
                        "tested_sampling_offsets_x_px":[-20,20],"boundary":"explicitly periodic wrap", "histogram_bins":2},
            "rows":rows,"images":{"fixed":save_image("R6_fixed.png",fixed),"moving":save_image("R6_moving.png",moving)},
            "figures":{},"limitation":"Periodic stripes are deliberately ambiguous. Excellent similarity need not establish correct physical correspondence; independent truth identifies the wrong period."}
    save_csv("R6_periodic_ambiguity.csv",rows);return result


def figure(fig,name,caption):
    fig.text(.02,.015,caption,fontsize=10,va="bottom",wrap=True)
    fig.tight_layout(rect=(0,.12,1,.98))
    fig.savefig(FIGURES/name,facecolor="white",bbox_inches="tight");plt.close(fig)
    return "figures/"+name


def figures(studies):
    fig,axes=plt.subplots(1,2,figsize=(11,5.1))
    for layout,color in [("spread",BLUE),("clustered",ORANGE)]:
        rows=[r for r in studies["R1"]["rows"] if r["layout"]==layout]
        axes[0].plot([r["sigma_per_coordinate_px"] for r in rows],[r["mean_fit_residual_moving_px"] for r in rows],"o-",label=layout,color=color)
        axes[1].plot([r["sigma_per_coordinate_px"] for r in rows],[r["independent_mean_error_fixed_px"] for r in rows],"o-",label=layout,color=color)
    for ax in axes:ax.set(xlabel="Click noise sigma per x/y coordinate (px)");ax.grid(alpha=.2);ax.legend()
    axes[0].set(ylabel="Mean fitting residual (moving px)",title="R1 | Fit agreement can look similar")
    axes[0].annotate("Both fit curves nearly overlap",xy=(.5,.600220120759),xytext=(.15,1.45),
                     arrowprops={"arrowstyle":"->","color":"#555555"},fontsize=11,
                     bbox={"facecolor":"white","edgecolor":"#c4d6df","boxstyle":"round,pad=.3"})
    axes[1].set(ylabel="Mean error on 25 unused points (fixed px)",title="R1 | Check away from fitted points")
    studies["R1"]["figures"]["comparison"]=figure(fig,"R1_point_layout.png","One frozen 16-point noise draw, not repeated trials. Dots are executed conditions; lines guide the eye. No error bars or confidence intervals are claimed. Clustered points occupy only 4x4 px; spread points cover 192x192 px.")

    fig,axes=plt.subplots(1,2,figsize=(11,5.1))
    for blur,color in [(0,BLUE),(1.5,ORANGE),(3,GREEN)]:
        rows=[r for r in studies["R2"]["rows"] if r["moving_blur_sigma_px"]==blur]
        axes[0].plot([r["rotation_degrees_opencv"] for r in rows],[r["ratio_pass_matches"] for r in rows],"o-",label=f"Blur sigma {blur} px",color=color)
        axes[1].plot([r["rotation_degrees_opencv"] for r in rows],[r["independent_mean_error_fixed_px"] for r in rows],"o-",label=f"Blur sigma {blur} px",color=color)
    for ax in axes:ax.set(xlabel="Generated rotation (degrees, OpenCV convention)");ax.grid(alpha=.2);ax.legend(fontsize=9)
    axes[0].set(ylabel="Ratio-filtered tentative matches (count)",title="R2 | Actual ORB, not simulated features")
    axes[1].set(ylabel="25-point independent mean error (fixed px)",title="R2 | Accuracy checked separately")
    studies["R2"]["figures"]["comparison"]=figure(fig,"R2_orb_conditions.png","Twelve saved CPU runs: 4 rotations x 3 moving-image blur levels. Blur sigma measures image smoothing, not click noise. A missing fit would remain missing. Counts are not accuracy percentages; no repeated-run uncertainty is estimated.")
    default=studies["R2"]["cases"][0];fixed=cv2.imread(str(ROOT/default["fixed_image"]),0);moving=cv2.imread(str(ROOT/default["moving_image"]),0)
    fig,ax=plt.subplots(figsize=(11,6));ax.imshow(np.hstack([fixed,moving]),cmap="gray",vmin=0,vmax=255)
    for r in default["matches"][:30]:
        a,b=r["fixed_xy"],r["moving_xy"]
        ax.plot([a[0],b[0]+256],[a[1],b[1]],color=GREEN if r.get("returned_ransac_inlier") else RED,alpha=.65)
    ax.set(title=f"R2 | Default actual ORB: {default['row']['ratio_pass_matches']} matches, {default['row']['returned_ransac_inliers']} returned inliers",xlabel="Reference x=0..255 | movable display starts at x=256",ylabel="Image y address (down)")
    studies["R2"]["figures"]["matches"]=figure(fig,"R2_orb_matches.png","Up to 30 saved matched pairs drawn. Green/red show the returned voting mask, not proven identity. Full keypoints, actual 32-byte descriptors, matching ratios and final residuals are saved per case. Browser selectors replay these measured outputs.")

    fig,ax=plt.subplots(figsize=(11,5.2))
    for condition,color in [("clean",BLUE),("noise",ORANGE),("occluded",GREEN),("rotated",RED)]:
        rows=[r for r in studies["R3"]["rows"] if r["condition"]==condition]
        ax.plot([r["upsample_factor"] for r in rows],[r["translation_component_error_px"] for r in rows],"o-",label=condition,color=color)
    ax.set(xscale="log",xticks=[1,10,100],xticklabels=["1 (1 px grid)","10 (0.1 px grid)","100 (0.01 px grid)"],xlabel="Upsampling factor (finer numerical grid)",ylabel="Error of translation component (px)",title="R3 | Finer numerical spacing does not promise the same accuracy")
    ax.legend();ax.grid(alpha=.2)
    studies["R3"]["figures"]["comparison"]=figure(fig,"R3_subpixel.png","Known generated shift=(+5.4,-3.7) in (y,x); correction=(-5.4,+3.7). Rotated condition adds 5 degrees and violates pure translation: this error does not summarize full alignment. Fourier boundaries are periodic. Dots are single controlled conditions, no error bars.")

    scan=studies["R4"]["scans"]["inverted"]
    slice_rows=[r for r in scan if r["sampling_y_px"]==-4]
    fig,axes=plt.subplots(1,3,figsize=(12,5.0))
    for ax,metric,label,direction,name in zip(axes,["mse","signed_ncc","mi_nats"],["MSE (squared 0-1 brightness units)","Signed NCC (no unit)","MI (nats, 32 bins)"],["smaller","larger","larger"],["MSE","signed NCC","MI"]):
        ax.plot([r["sampling_x_px"] for r in slice_rows],[r[metric] for r in slice_rows],"o-",color=BLUE)
        ax.axvline(6,color=GREEN,linestyle="--")
        ax.set(xlabel="Tried sampling x offset (px)",ylabel=label,title=f"R4 | Choose {direction} {name}")
        ax.grid(alpha=.2)
    studies["R4"]["figures"]["inverted_slice"]=figure(fig,"R4_inverted_slice.png","Brightness is inverted, geometry unchanged. This is an x-slice at correct y=-4, not the complete 441-candidate 2-D search. Dashed green=known x=+6. MI can recognize an inverse brightness clue; no method is guaranteed to win on all images.")
    fig,ax=plt.subplots(figsize=(11,5.0))
    for i,metric in enumerate(["mse","signed_ncc","mi_nats"]):
        rs=[r for r in studies["R4"]["rows"] if r["metric"]==metric]
        ax.bar(np.arange(3)+(i-1)*.23,[r["geometric_error_px"] for r in rs],width=.23,label=metric)
    ax.set(xticks=range(3),xticklabels=["same brightness","inverted","nonlinear inverted"],ylabel="Error of best 2-D sampling offset (px)",title="R4 | Judge the selected movement using known truth")
    ax.legend();studies["R4"]["figures"]["comparison"]=figure(fig,"R4_search_errors.png","Each bar is one actual bounded exhaustive search with fixed 3,136 valid samples. Same source image and geometry; only appearance rule changes. Zero-height bars mean correct integer recovery in this controlled setup, not universal robustness.")

    fig,axes=plt.subplots(1,2,figsize=(11,5.1))
    for offset,color in [(0,ORANGE),(8,GREEN),(16,BLUE)]:
        rows=[r for r in studies["R5"]["rows"] if r["sampling_offset_x_px"]==offset]
        for ax,key in zip(axes,["mi_nats","nmi"]):
            ax.plot([r["overlap_width_px"] for r in rows],[r[key] for r in rows],"o-",label=f"Offset {offset:+} px ({'correct' if offset==8 else 'wrong'})",color=color)
    for ax in axes:ax.set(xlabel="Remaining centered overlap width (px)");ax.invert_xaxis();ax.legend(fontsize=9);ax.grid(alpha=.2)
    axes[0].set(ylabel="MI (nats, 32 bins)",title="R5 | Ordinary mutual information")
    axes[1].set(ylabel="NMI (entropy ratio, no unit)",title="R5 | Normalized mutual information")
    studies["R5"]["figures"]["comparison"]=figure(fig,"R5_overlap.png","Read left to right as the crop narrows: 96 px down to 6 px, height stays 96. Cropping changes sample count AND image content. MI and NMI heights use different units; compare behavior within a panel, not absolute heights across panels. Constant entropy makes NMI undefined.")

    rows=studies["R6"]["rows"];fig,axes=plt.subplots(1,2,figsize=(11,5.1))
    axes[0].plot([r["sampling_offset_x_px"] for r in rows],[r["mse"] for r in rows],"o-",color=BLUE)
    axes[1].plot([r["sampling_offset_x_px"] for r in rows],[r["independent_geometric_error_px"] for r in rows],"o-",color=ORANGE)
    for ax in axes:
        ax.axvline(5,color=GREEN,linestyle="--",label="Known truth +5")
        ax.axvline(13,color=RED,linestyle=":",label="Lookalike +13")
        ax.set(xlabel="Tested sampling x offset (px)");ax.grid(alpha=.2);ax.legend(fontsize=9)
    axes[0].set(ylabel="MSE (squared brightness units)",title="R6 | Many shifts have perfect appearance")
    axes[1].set(ylabel="Independent geometric error (px)",title="R6 | Only the known shift has zero ruler error")
    studies["R6"]["figures"]["comparison"]=figure(fig,"R6_similarity_vs_geometry.png","Period=8 pixels. Correct +5 and wrong +13 have equal MSE=0, NCC=+1 and MI=ln(2); the wrong shift misses by 8 px. This mathematical counterexample illustrates an evaluation warning. It does not reproduce the paper's 3-D clinical experiment.")


def slide_evidence(studies):
    """Distill actual saved rows into readable tables; never invent headline values."""
    records=[]
    r1rows=[r for r in studies["R1"]["rows"] if r["sigma_per_coordinate_px"] in [.5,2]]
    records.append({"id":"R1","title":"Point spread matters beyond fit agreement",
        "headers":["Layout / sigma (px)","Fit residual (moving px)","Unused-point error (fixed px)"],
        "rows":[[f"{r['layout']} / {r['sigma_per_coordinate_px']:g}",f"{r['mean_fit_residual_moving_px']:.3f}",f"{r['independent_mean_error_fixed_px']:.3f}"] for r in r1rows],
        "caption":"Mean Euclidean distances; one frozen 16-point click-noise realization. Twenty-five check points never fitted.",
        "purpose":"Test whether equally small fitting residuals ensure accurate recovery away from a clustered fit region.",
        "settings":"16 known correspondences; spread 192 x 192 px versus cluster 4 x 4 px; similarity fit; sigma 0, 0.5, 2 per moving coordinate.",
        "interpretation":"At the same sigma, fitting residuals are almost identical but clustered correspondences extrapolate poorly.",
        "own_limitations":"New 2-D points, one draw, no wrong matches; no robustness or original numerical benchmark replication.","citation_ids":[13]})
    selected=[r for r in studies["R2"]["rows"] if r["rotation_degrees_opencv"] in [0,75] and r["moving_blur_sigma_px"] in [0,3]]
    records.append({"id":"R2","title":"Actual ORB under rotation and image blur",
        "headers":["Rotation / blur sigma","Matches / inliers","Unused-point error (px)"],
        "rows":[[f"{r['rotation_degrees_opencv']} deg / {r['moving_blur_sigma_px']:g} px",f"{r['ratio_pass_matches']} / {r['returned_ransac_inliers']}",f"{r['independent_mean_error_fixed_px']:.3f}"] for r in selected],
        "caption":"Saved OpenCV ORB + Hamming ratio + similarity RANSAC. Errors are mean fixed-pixel distances on 25 unused exact points.",
        "purpose":"Observe how a recognizable-place pipeline changes when the movable picture turns or becomes smoother.",
        "settings":"256 px public camera; maximum 1,000 keypoints; WTA_K=2; ratio <0.75; threshold 3 moving px; 4 angles x 3 blur levels.",
        "interpretation":"Strong blur reduced match counts and increased independent geometric error in these measured conditions.",
        "own_limitations":"One public photo; synthetic movement; no detector benchmark, real camera acquisition or timing comparison. Returned inlier masks precede final refinement.","citation_ids":[14,3]})
    selected=[next(r for r in studies["R3"]["rows"] if r["condition"]==name and r["upsample_factor"]==u) for name,u in [("clean",1),("clean",100),("occluded",100),("rotated",100)]]
    records.append({"id":"R3","title":"Subpixel spacing is not an accuracy promise",
        "headers":["Condition","Upsampling","Translation-component error (px)"],
        "rows":[[r["condition"],str(r["upsample_factor"]),f"{r['translation_component_error_px']:.3f}"] for r in selected],
        "caption":"Known correction=(-5.4,+3.7) in (y,x). Finer grid improves this clean example; rotation violates the translation-only model.",
        "purpose":"Separate numerical search spacing from measured recovery accuracy and the transform model's assumptions.",
        "settings":"256 px periodic Fourier shift; upsample 1/10/100; clean, noise sigma 0.03, occlusion, extra 5-degree rotation.",
        "interpretation":"The clean decimal shift is exactly represented on a 0.1 px grid; the rotated condition remains wrong on a 0.01 px grid.",
        "own_limitations":"Periodic boundary; one image and noise draw. Rotated-case error measures the translation component, not full geometric alignment.","citation_ids":[5]})
    selected=[r for r in studies["R4"]["rows"] if r["contrast"]=="inverted"]
    records.append({"id":"R4","title":"An appearance rule can fool a registration score",
        "headers":["Score optimized","Selected sampling offset (px)","Known-offset error (px)"],
        "rows":[[r["metric"],f"({r['best_sampling_x_px']:+d},{r['best_sampling_y_px']:+d})",f"{r['geometric_error_px']:.3f}"] for r in selected],
        "caption":"Inverted brightness; true sampling offset=(+6,-4). Every candidate compares the same 3,136 real pixels.",
        "purpose":"Check why equal brightness and statistical dependence are different registration objectives.",
        "settings":"32-bin histogram MI; 441 integer (x,y) candidates; same, v->1-v, v->1-v^0.7; 96 px photo.",
        "interpretation":"MI recovered the known integer shift in all three appearances. Signed NCC and MSE chose wrong shifts after inversion.",
        "own_limitations":"Teaching adaptation, not Viola/Wells Parzen estimation or optimizer; simulated contrasts are not acquired modalities; bounded translation only.","citation_ids":[7]})
    selected=[next(r for r in studies["R5"]["rows"] if r["overlap_width_px"]==width and r["sampling_offset_x_px"]==offset) for width,offset in [(96,8),(6,8),(6,0)]]
    table=[[f"{r['overlap_width_px']} px crop / offset {r['sampling_offset_x_px']:+d}",f"{r['mi_nats']:.3f}",f"{r['nmi']:.3f}"] for r in selected]
    table.append(["both arrays constant","0.000","undefined (0 denominator)"])
    records.append({"id":"R5","title":"Changing overlap changes the evidence",
        "headers":["Compared area / alignment","MI (nats)","NMI (entropy ratio)"],"rows":table,
        "caption":"NMI=(H(F)+H(M))/H(F,M); 32 bins. Crops change both sample count and foreground content. Flat-pair NMI is undefined.",
        "purpose":"Observe ordinary and normalized information scores while the compared field of view narrows.",
        "settings":"128 px camera; widths 96,72,48,24,12,6; height 96; correct offset 8 and wrong offsets 0/16; natural logarithms.",
        "interpretation":"Exact aligned equal values keep NMI=2 here while MI changes with crop content; wrong alignments also change. No universal advantage follows.",
        "own_limitations":"A perfect same-contrast relation is an easy special case, not a 3-D multimodal replication or proof of overlap invariance. Crop size and content change together.","citation_ids":[15]})
    selected=[next(r for r in studies["R6"]["rows"] if r["sampling_offset_x_px"]==offset) for offset in [5,13,-3]]
    records.append({"id":"R6","title":"Perfect similarity can hide the wrong correspondence",
        "headers":["Sampling offset (px)","MSE / NCC / MI","Geometric error (px)"],
        "rows":[[f"{r['sampling_offset_x_px']:+d}",f"{r['mse']:.0f} / {r['signed_ncc']:+.0f} / {r['mi_nats']:.3f}",f"{r['independent_geometric_error_px']:.0f}"] for r in selected],
        "caption":"MI uses nats; NCC has no unit; MSE uses squared brightness units. Period 8 px; known movement +5 px. Equal appearance, different geometry.",
        "purpose":"Show why a similarity score is not a substitute for an independent geometric answer key.",
        "settings":"Synthetic periodic dark/bright stripes; period 8; generated shift 5; 41 offsets (-20..20), 2-bin MI.",
        "interpretation":"Offsets +5, +13 and -3 have identical perfect similarity, but the latter two each miss known physical positions by 8 px.",
        "own_limitations":"Constructed 2-D counterexample illustrating Rohlfing's warning, not a reproduction of the 3-D clinical experiment or a universal frequency of failure.","citation_ids":[9]})
    save_json(RESULTS/"slide_evidence.json",records)
    return records


def run_all():
    studies={}
    functions={"R1":r1,"R2":r2,"R3":r3,"R4":r4,"R5":r5,"R6":r6}
    mapping={"R1":[53,54,33,34],"R2":[55,56,35,36],"R3":[57,58,37,38],"R4":[59,60,39,40],"R5":[61,62,41,42],"R6":[63,64,43,44]}
    output={"schema_version":1,"seed":SEED,"versions":{"python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__,"scikit_image":skimage.__version__,"opencv":cv2.__version__,"matplotlib":matplotlib.__version__},"studies":studies}
    for name,function in functions.items():
        studies[name]=clean(function());studies[name]["slide_map"]={"beginner":mapping[name][:2],"original":mapping[name][2:]}
        # Make completed studies readable while later CPU runs continue.
        save_json(RESULTS/"study_results.json",output)
    figures(studies)
    slide_evidence(studies)
    assert not studies["R1"]["degenerate_check"]["success"]
    assert max(r["independent_mean_error_fixed_px"] for r in studies["R1"]["rows"] if r["sigma_per_coordinate_px"]==0)<1e-8
    assert len(studies["R2"]["rows"])==12
    assert all(r["status"]=="measured" for r in studies["R2"]["rows"])
    assert next(r for r in studies["R3"]["rows"] if r["condition"]=="clean" and r["upsample_factor"]==100)["translation_component_error_px"]<1e-9
    assert all(r["geometric_error_px"]==0 for r in studies["R4"]["rows"] if r["metric"]=="mi_nats")
    assert studies["R5"]["constant_failure"]["nmi"] is None
    stripe=[r for r in studies["R6"]["rows"] if r["sampling_offset_x_px"] in [5,13]]
    assert all(r["mse"]==0 and abs(r["signed_ncc"]-1)<1e-12 for r in stripe)
    assert stripe[1]["independent_geometric_error_px"]==8
    output["validation"]={"status":"passed","scope":"known noiseless similarity; degenerate-point failure; 12 actual ORB runs; clean subpixel recovery; fixed-valid MI search; undefined constant NMI; equal similarity with wrong-period geometry"}
    output["camera_provenance"]={"license":"CC0","credit":"Lav Varshney / scikit-image camera",
                                 "url":"https://scikit-image.org/docs/stable/api/skimage.data.html#skimage.data.camera",
                                 "sha256":hashlib.sha256((DATA/"camera.png").read_bytes()).hexdigest()}
    (DATA/"PROVENANCE.md").write_text("# Public source and controlled derivatives\n\nCamera photograph: Lav Varshney, provided by scikit-image; CC0.\nhttps://scikit-image.org/docs/stable/api/skimage.data.html#skimage.data.camera\n\nCopied from the existing bundled source; no downloads at runtime. R2--R5 use resized/transformed copies. All movements, blur, noise, occlusion and brightness remapping are researcher-created controlled conditions. R1 point sets and R6 stripes are synthetic. These are not clinical acquisitions or original paper benchmarks. Fourier-shift experiments explicitly use periodic boundaries.\n",encoding="utf-8")
    save_json(RESULTS/"study_results.json",output)
    save_json(RESULTS/"study_browser.json",output)
    return output


if __name__=="__main__":
    answers=run_all()
    print(answers["validation"])
    for name,study in answers["studies"].items():print(name,len(study["rows"]),"conditions",study["method_status"])
