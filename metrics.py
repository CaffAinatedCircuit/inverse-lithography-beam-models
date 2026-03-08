# metrics.py

import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.filters import sobel

def compute_metrics(pred, target):
    pred = pred.detach().cpu().numpy()
    target = target.detach().cpu().numpy()

    mse = np.mean((pred-target)**2)
    ssim_val = ssim(target, pred, data_range=1.0)

    edge_t = sobel(target)
    edge_p = sobel(pred)
    edge_overlap = np.sum((edge_t>0.1)&(edge_p>0.1)) / np.sum(edge_t>0.1)

    fft_t = np.abs(np.fft.fftshift(np.fft.fft2(target)))
    fft_p = np.abs(np.fft.fftshift(np.fft.fft2(pred)))
    spectral_match = np.corrcoef(fft_t.flatten(), fft_p.flatten())[0,1]

    return mse, ssim_val, edge_overlap, spectral_match