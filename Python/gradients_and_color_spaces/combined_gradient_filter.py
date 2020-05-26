import cv2
import numpy as np


def abs_sobel_thresh(img, orient='x', sobel_kernel=3, thresh=(0, 255)):
    # Calculate directional gradient
    # Apply threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    orientation = orient == 'x'
    sobel = cv2.Sobel(gray, cv2.CV_64F, orientation, not orientation, ksize=sobel_kernel)
    sobel = np.abs(sobel)
    sobel = np.uint8(255 * sobel / sobel.max())

    return (sobel >= thresh[0]) & (sobel <= thresh[1])


def mag_thresh(image, sobel_kernel=3, mag_thresh=(0, 255)):
    # Calculate gradient magnitude
    # Apply threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    mag = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    mag = np.uint8(255 * mag / mag.max())

    return (mag >= mag_thresh[0]) & (mag <= mag_thresh[1])


def dir_threshold(image, sobel_kernel=3, thresh=(0, np.pi / 2)):
    # Calculate gradient direction
    # Apply threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    theta = np.arctan2(np.abs(sobel_y), np.abs(sobel_x))

    return (theta >= thresh[0]) & (theta <= thresh[1])


def combine(gradx, grady, magnitude, direction):
    return (gradx & grady) | (magnitude & direction)


def convert_to_image(mask):
    return mask.astype(np.uint8) * 255.


if __name__ == '__main__':
    # Read in an image and grayscale it
    image = cv2.imread('signs_vehicles_xygrad.png')

    # Choose a Sobel kernel size
    ksize = 13  # Choose a larger odd number to smooth gradient measurements

    # Apply each of the thresholding functions
    gradx = abs_sobel_thresh(image, orient='x', sobel_kernel=ksize, thresh=(20, 100))
    grady = abs_sobel_thresh(image, orient='y', sobel_kernel=ksize, thresh=(30, 75))
    mag_binary = mag_thresh(image, sobel_kernel=ksize, mag_thresh=(30, 100))
    dir_binary = dir_threshold(image, sobel_kernel=ksize, thresh=(np.pi / 4, np.pi / 2.5))
    combined_binary = combine(gradx, grady, mag_binary, dir_binary)

    cv2.imshow('Gradx', convert_to_image(gradx))
    cv2.imshow('Grady', convert_to_image(grady))
    cv2.imshow('Magnitude', convert_to_image(mag_binary))
    cv2.imshow('Direction', convert_to_image(dir_binary))
    cv2.imshow('Combined', convert_to_image(combined_binary))

    cv2.waitKey()
    cv2.destroyAllWindows()
