import numpy as np
import numba

@numba.njit()
def imhist(arr):
    hist = np.zeros(256, dtype=np.int32)
    for i in range(arr.shape[0]):
        hist[arr[i]] += 1
    return hist

@numba.njit()
def im2dhist(image, w_neighboring=6):
    V = image.astype(np.int16)
    V_hist = imhist(V)

    X = np.nonzero(V_hist)[0] + 1
    K = len(X)

    Hist2D = np.zeros((K, K), dtype=np.float32)

    X_inv = np.zeros((X[-1],), dtype=np.int32)
    X_inv[X - 1] = np.arange(K)

    for i in range(K):
        xi, yi = np.nonzero(V == (X[i] - 1))

        xi_n = np.zeros((xi.size, 2 * w_neighboring + 1), dtype=np.int32)
        yi_n = np.zeros((yi.size, 2 * w_neighboring + 1), dtype=np.int32)

        for ii in range(2 * w_neighboring + 1):
            xi_n[:, ii] = xi + (ii - w_neighboring)
            yi_n[:, ii] = yi + (ii - w_neighboring)

        xi_n = np.where(xi_n < V.shape[0], xi_n, -1)
        yi_n = np.where(yi_n < V.shape[1], yi_n, -1)

        for i_row in range(xi_n.shape[0]):
            xi_nr = xi_n[i_row, :]
            yi_nr = yi_n[i_row, :]
            xi_nr = xi_nr[xi_nr >= 0]
            yi_nr = yi_nr[yi_nr >= 0]

            neighboring_intens = V[xi_nr[0]:xi_nr[-1]+1, yi_nr[0]:yi_nr[-1]+1].ravel()

            for neighboring_inten in neighboring_intens:
                Hist2D[i, X_inv[neighboring_inten]] += abs(neighboring_inten + 1 - X[i]) + 1

    Hist2D_normalized = Hist2D / np.sum(Hist2D)
    return Hist2D_normalized

