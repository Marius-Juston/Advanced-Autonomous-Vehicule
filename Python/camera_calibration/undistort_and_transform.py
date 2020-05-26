import pickle

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read in the saved camera matrix and distortion coefficients
# These are the arrays you calculated using cv2.calibrateCamera()
dist_pickle = pickle.load(open("wide_dist_pickle.p", "rb"))
mtx = dist_pickle["mtx"]
dist = dist_pickle["dist"]

# Read in an image
img = cv2.imread('test_image2.png')
nx = 8  # the number of inside corners in x
ny = 6  # the number of inside corners in y


# MODIFY THIS FUNCTION TO GENERATE OUTPUT
# THAT LOOKS LIKE THE IMAGE ABOVE
def corners_unwarp(img, nx, ny, mtx, dist):
    # Pass in your image into this function
    # Write code to do the following steps
    # 1) Undistort using mtx and dist
    # 2) Convert to grayscale
    # 3) Find the chessboard corners
    # 4) If corners found:
    # a) draw corners
    # b) define 4 source points src = np.float32([[,],[,],[,],[,]])
    # Note: you could pick any four of the detected corners
    # as long as those four corners define a rectangle
    # One especially smart way to do this would be to use four well-chosen
    # corners that were automatically detected during the undistortion steps
    # We recommend using the automatic detection of corners in your code
    # c) define 4 destination points dst = np.float32([[,],[,],[,],[,]])
    # d) use cv2.getPerspectiveTransform() to get M, the transform matrix
    # e) use cv2.warpPerspective() to warp your image to a top-down view

    undistorted = cv2.undistort(img, mtx, dist, None, mtx)
    gray = cv2.cvtColor(undistorted, cv2.COLOR_BGR2GRAY)

    grid_size = (8, 6)
    ret, corners = cv2.findChessboardCorners(gray, grid_size, None)

    if ret:
        cv2.drawChessboardCorners(undistorted, (nx, ny), corners, ret)

    up_left = 0
    up_right = grid_size[0] - 1
    down_left = grid_size[0] * (grid_size[1] - 1)
    down_right = down_left + grid_size[0] - 1

    source_points = np.array([corners[up_left][0], corners[up_right][0], corners[down_left][0], corners[down_right][0]],
                             dtype=np.float32)

    offset = 100
    h, w = gray.shape

    dist_points = np.array([[offset, offset], [w - offset, offset], [offset, h - offset], [w - offset, h - offset]], dtype=np.float32)

    M = cv2.getPerspectiveTransform(source_points, dist_points)
    perspective = cv2.warpPerspective(undistorted, M, (w, h), flags=cv2.INTER_LINEAR)

    return perspective, M


top_down, perspective_M = corners_unwarp(img, nx, ny, mtx, dist)
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
f.tight_layout()
ax1.imshow(img)
ax1.set_title('Original Image', fontsize=50)
ax2.imshow(top_down)
ax2.set_title('Undistorted and Warped Image', fontsize=50)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show()
