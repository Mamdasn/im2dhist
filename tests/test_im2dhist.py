from im2dhist import im2dhist
import cv2
import numpy as np

def test_im2dhist_with_param():
    image_name = '../assets/Plane.jpg'
    image = cv2.imread(image_name)
    # convert rgb image to gray
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2*w_neighboring+1 is width of the square window around each pixel, when counting neiboring pixels
    # calculate 2 dimensional histogram of gray_image
    v_image_2DHisteq = im2dhist(gray_image, w_neighboring=6)
    # np.save(f'{image_name}-2D-Histogram', v_image_2DHisteq)
    v_image_2DHisteq_cmpr = np.load(f'{image_name}-2D-Histogram.npy')
    assert np.all(v_image_2DHisteq == v_image_2DHisteq_cmpr)
    
