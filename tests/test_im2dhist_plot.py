from im2dhist import  im2dhist
import cv2
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def plot2DHistogram(Hist2D, title):
    # plot 2D-Histogram
    [K, _] = Hist2D.shape
    x = np.outer(np.arange(0, K), np.ones(K))
    y = x.copy().T 
    # ln-ing Hist2D makes its details more prominent.
    Hist2D_ln = Hist2D.copy()
    Hist2D_ln[np.where(Hist2D_ln<=0)] = 1e-15
    z = np.log(Hist2D_ln)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
    ax.set_title(title)
    plt.show()

def main():
    image_name = '../assets/Plane.jpg'
    image = cv2.imread(image_name)
    # convert rgb image to gray
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2*w_neighboring+1 is width of the square window around each pixel, when counting neiboring pixels
    # calculate 2 dimensional histogram of gray_image
    v_image_2DHisteq = im2dhist(gray_image, w_neighboring=6)
    np.save(f'{image_name}-2D-Histogram', v_image_2DHisteq)
    # v_image_2DHisteq_cmpr = np.load(f'{image_name}-2D-Histogram.npy')
    plot2DHistogram(v_image_2DHisteq, title="2D Histogram of Plane.jpg") 

if __name__ == '__main__': main()
