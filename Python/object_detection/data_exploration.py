import glob
import os

import cv2


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
    car_list = read_image_folder('vehicules')
    not_car_list = read_image_folder('non_vehicules')

    data_info = data_look(car_list, not_car_list)

    print('Your function returned a count of', data_info["n_cars"], ' cars and', data_info["n_notcars"], ' non-cars')
    print('of size: ', data_info["image_shape"], ' and data type:', data_info["data_type"])
