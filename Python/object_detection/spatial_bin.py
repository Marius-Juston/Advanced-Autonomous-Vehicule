import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Read in an image
# You can also read cutout2, 3, 4 etc. to see other examples
image = mpimg.imread('cutouts/cutout1.jpg')


# Define a function to compute color histogram features
# Pass the color_space flag as 3-letter all caps string
# like 'HSV' or 'LUV' etc.
# KEEP IN MIND IF YOU DECIDE TO USE THIS FUNCTION LATER
# IN YOUR PROJECT THAT IF YOU READ THE IMAGE WITH
# cv2.imread() INSTEAD YOU START WITH BGR COLOR!
def bin_spatial(img, color_space='RGB', size=(32, 32)):
    if color_space != 'RGB':
        color_conversion = 'cv2.COLOR_RGB2' + color_space

        img = cv2.cvtColor(img, eval(color_conversion))

    img = cv2.resize(img, size)
    # Convert image to new color space (if specified)
    # Use cv2.resize().ravel() to create the feature vector
    features = img.ravel()  # Remove this line!
    # Return the feature vector
    return features


feature_vec = bin_spatial(image, color_space='RGB', size=(32, 32))

# Plot features
plt.plot(feature_vec)
plt.title('Spatially Binned Features')
plt.show()
