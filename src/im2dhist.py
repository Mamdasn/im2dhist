import numpy as np
import numba

@numba.njit()
def imhist(arr):
    hist, _ = np.histogram(arr, bins=256, range=(0, 255))
    return np.asarray(hist)

@numba.njit()
def im2dhist(image, w_neighboring = 6):
    V = image.copy()
    [h, w] = V.shape
    V_hist = imhist(V.reshape(1, -1))
    
    X = (V_hist>0) * np.arange(1, 257)
    X = X[X>0]
    K = len(X)

    Hist2D = np.zeros((K, K))
    
    X_inv = np.zeros((X[-1], 1), dtype=np.uint8).reshape(-1)
    X_inv[X-1] = np.arange(1, K+1)
    
    for i in range(K):
        [xi, yi] = np.where(V==(X[i]-1))
        
        xi_tile = np.zeros((xi.size, 2*w_neighboring+1), dtype=np.int16)
        yi_tile = np.zeros((yi.size, 2*w_neighboring+1), dtype=np.int16)
        for ii in range(2*w_neighboring+1):
            xi_tile[:, ii] = xi
            yi_tile[:, ii] = yi
        xi_n = xi_tile + np.outer(np.ones(xi.size, dtype=np.int16), np.arange(-w_neighboring, w_neighboring+1))
        yi_n = yi_tile + np.outer(np.ones(yi.size, dtype=np.int16), np.arange(-w_neighboring, w_neighboring+1))
    
        xi_n = np.where(xi_n<h, xi_n, -1*np.ones_like(xi_n))
        yi_n = np.where(yi_n<w, yi_n, -1*np.ones_like(yi_n))
        
        for i_row in range(xi_n.shape[0]):
            xi_nr = xi_n[i_row, :] 
            yi_nr = yi_n[i_row, :] 
            xi_nr = xi_nr[np.where(xi_nr>=0)] 
            yi_nr = yi_nr[np.where(yi_nr>=0)] 
            
            neighboring_intens = V[xi_nr[0]:xi_nr[-1]+1, yi_nr[0]:yi_nr[-1]+1].copy().reshape(-1).astype(np.int16)
            
            for neighboring_inten in neighboring_intens:
                Hist2D[i, X_inv[neighboring_inten]-1] += np.abs(neighboring_inten+1-X[i]) +1
    Hist2D_normalized = Hist2D/np.sum(Hist2D)
    # return Hist2D_normalized
    return Hist2D_normalized