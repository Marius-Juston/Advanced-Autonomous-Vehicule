import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

image = mpimg.imread('bbox-example-image.jpg')


# Here is your draw_boxes function from the previous exercise
def draw_boxes(img, bboxes, color=(0, 0, 255), thick=6):
    # Make a copy of the image
    imcopy = np.copy(img)
    # Iterate through the bounding boxes
    for bbox in bboxes:
        # Draw a rectangle given bbox coordinates
        cv2.rectangle(imcopy, bbox[0], bbox[1], color, thick)
    # Return the image copy with boxes drawn
    return imcopy


def number_of_windows(image_length, window_length, overlap_proportion):
    return 1 + (image_length - window_length) / (window_length * overlap_proportion)


# Define a function that takes an image,
# start and stop positions in both x and y,
# window size (x and y dimensions),
# and overlap fraction (for both x and y)
def slide_window(img, x_start_stop=None, y_start_stop=None, xy_window=(64, 64), xy_overlap=(0.5, 0.5)):
    if x_start_stop is None:
        x_start_stop = (0, img.shape[1])
    elif None in x_start_stop:
        x_start_stop = (
            0 if x_start_stop[0] is None else x_start_stop[0],
            img.shape[1] if x_start_stop[1] is None else x_start_stop[1])
    if y_start_stop is None:
        y_start_stop = (0, img.shape[0])
    elif None in y_start_stop:
        y_start_stop = (
            0 if y_start_stop[0] is None else y_start_stop[0],
            img.shape[0] if y_start_stop[1] is None else y_start_stop[1])

    x_w = number_of_windows(x_start_stop[1] - x_start_stop[0], xy_window[0], xy_overlap[0])
    y_w = number_of_windows(y_start_stop[1] - y_start_stop[0], xy_window[1], xy_overlap[1])
    nx_pix_per_step = int(xy_window[0] * (1 - xy_overlap[0]))
    ny_pix_per_step = int(xy_window[1] * (1 - xy_overlap[1]))

    x_w = int(x_w)
    y_w = int(y_w)

    print(x_w, y_w)

    window_list = []

    for ys in range(y_w):
        for xs in range(x_w):
            # Calculate window position
            startx = xs * nx_pix_per_step + x_start_stop[0]
            endx = startx + xy_window[0]
            starty = ys * ny_pix_per_step + y_start_stop[0]
            endy = starty + xy_window[1]
            # Append window position to list
            window_list.append(((startx, starty), (endx, endy)))

    return window_list


windows = slide_window(image, xy_window=(128, 128), xy_overlap=(0.5, 0.5))

window_img = draw_boxes(image, windows, color=(0, 0, 255), thick=6)
plt.imshow(window_img)
plt.show()
