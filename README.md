# im2dhist
This small piece of code is intended to help researchers, especially in field of image processing, to easily calculate two dimensional histogram of a given image.

## How it works
A moving window of WxW moves through out the given image, and as its center places on each pixel, number of encounters with same and other brightness intensities is counted seperately. This package basically outputs a normalized two dimensional numpy array of brightness intensity encounters.  
![How moving window works](https://raw.githubusercontent.com/Mamdasn/im2dhist/main/assets/how-it-works-window-kernel-title.jpg "How moving window works")
w_neighboring=1 corresponds to a square of 3x3.

## Installation

Run the following to install:

```python
pip install im2dhist
```

## Usage

```python
from im2dhist import im2dhist
import cv2
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def main():
    image_name = 'Plane.jpg'
    image = cv2.imread(image_name)
    # converts rgb image to gray
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2*w_neighboring+1 is width of the square window around each pixel, when counting neiboring pixels
    # calculate 2 dimensional histogram of gray_image
    v_image_2DHisteq = im2dhist(gray_image, w_neighboring=6)

    # plots 2D-Histogram
    [K, _] = v_image_2DHisteq.shape
    x = np.outer(np.arange(0, K), np.ones(K))
    y = x.copy().T 
    # ln-ing v_image_2DHisteq makes its details more prominent.
    Hist2D_ln = v_image_2DHisteq.copy()
    Hist2D_ln[np.where(Hist2D_ln<=0)] = 1e-15
    z = np.log(Hist2D_ln)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
    ax.set_title(f'2D-Histogram of {image_name}')
    plt.show()
if __name__ == '__main__': main()
```

## Showcase
This is a sample image
![Plane.jpg Image](https://raw.githubusercontent.com/Mamdasn/im2dhist/main/assets/Plane.jpg "Plane.jpg Image")
Two dimensional histogram of the sample image
![Two Dimensional Histogram](https://raw.githubusercontent.com/Mamdasn/im2dhist/main/assets/Plane-big-2D-Histogram.jpeg "Two Dimensional Histogram")
