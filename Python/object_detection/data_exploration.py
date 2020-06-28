import glob
import os

import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def data_look(car_list, notcar_list):
    data_dict = {"n_cars": len(car_list), "n_notcars": len(notcar_list)}
    test_image = cv2.imread(car_list[0])

    data_dict["image_shape"] = test_image.shape
    data_dict["data_type"] = test_image.dtype
    return data_dict


def read_image_folder(image_folder):
    images = glob.glob(os.path.join(image_folder, '*.png'))
    return images


if __name__ == '__main__':
    cars = read_image_folder('vehicules')
    not_cars = read_image_folder('non_vehicules')

    data_info = data_look(cars, not_cars)

    print('Your function returned a count of', data_info["n_cars"], ' cars and', data_info["n_notcars"], ' non-cars')
    print('of size: ', data_info["image_shape"], ' and data type:', data_info["data_type"])

    car_ind = np.random.randint(0, len(cars))
    notcar_ind = np.random.randint(0, len(not_cars))

    # Read in car / not-car images
    car_image = mpimg.imread(cars[car_ind])
    notcar_image = mpimg.imread(not_cars[notcar_ind])

    # Plot the examples
    fig = plt.figure()
    plt.subplot(121)
    plt.imshow(car_image)
    plt.title('Example Car Image')
    plt.subplot(122)
    plt.imshow(notcar_image)
    plt.title('Example Not-car Image')
    plt.show()
