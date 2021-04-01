import numpy as np
from tqdm import tqdm

def imhist(image):
    hist, bins = np.histogram(image.reshape(1, -1), bins=256, range=(0, 255))
    return (np.asarray(hist), np.asarray(bins[0:-1]))
    
def im2dhist(image, w_neighboring = 6, showProgress = False):
    # w_neighboring is the width of the square window: 6*2 + 1 = 13 that moves through the image
    image_arr = np.asarray(image)

    # calculating histogram of input image's value layer
    v_image_hist, bins = imhist(image_arr)
    [h, w] = image_arr.shape

    # get shape of image
    [h, w] = image_arr.shape

    # X converts 1:K to brightness intensity
    X = (v_image_hist>0) * [i for i in range(1, 257)]
    X = X[X>0]
    K = len(X)

    # Create the Hist2D Matrix
    Hist2D = np.zeros((K, K))

    # X_inv converts brightness intensity to 1:k
    X_inv = np.zeros((X[-1], 1), dtype=np.uint8).reshape(-1)
    X_inv[X-1] = np.array([i for i in range(1, K+1)]).reshape(-1)

    for i in tqdm(range(0, K)) if showProgress else range(0, K):
        [xi, yi] = np.where(image_arr==(X[i]-1))
        
        # getting neighboring pixels around xis and yis 
        xi = xi.reshape(-1, 1)
        yi = yi.reshape(-1, 1)
        xi_n = np.tile(xi, 2*w_neighboring+1) + np.outer(np.ones(xi.shape[0], dtype=np.int16), np.arange(-w_neighboring, w_neighboring+1))
        yi_n = np.tile(yi, 2*w_neighboring+1) + np.outer(np.ones(xi.shape[0], dtype=np.int16), np.arange(-w_neighboring, w_neighboring+1))

        xi_n[np.where(xi_n<0)] = -1
        xi_n[np.where(xi_n>=h)] = -1
        yi_n[np.where(yi_n<0)] = -1
        yi_n[np.where(yi_n>=w)] = -1
 
        for i_row in range(0, xi_n.shape[0]):
            xi_nr = xi_n[i_row, :] 
            yi_nr = yi_n[i_row, :] 
            xi_nr = xi_nr[np.where(xi_nr>=0)] 
            yi_nr = yi_nr[np.where(yi_nr>=0)] 

            # making Hist2D
            neighboring_intens = image_arr[xi_nr[0]:xi_nr[-1]+1, yi_nr[0]:yi_nr[-1]+1].reshape(-1).astype(np.int16)
            Hist2D[i, X_inv[neighboring_intens]-1] += abs(neighboring_intens+1-X[i]) + 1

    Hist2D_normalized = Hist2D/np.sum(Hist2D)
    return Hist2D_normalized
