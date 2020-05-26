import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Load our image
# `mpimg.imread` will load .jpg as 0-255, so normalize back to 0-1
img = mpimg.imread('warped-example.jpg') / 255


def hist(img):
    histogram = np.sum(img[img.shape[0] // 2:, :], axis=0)

    return histogram


# Create histogram of image binary activations
histogram = hist(img)

# Visualize the resulting histogram
plt.plot(histogram)
plt.show()