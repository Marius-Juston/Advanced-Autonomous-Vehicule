import cv2

from gradients_and_color_spaces.combined_gradient_filter import convert_to_image, abs_sobel_thresh, mag_thresh, \
    dir_threshold, combine

params = {
    'k_size_x': 3,
    'k_size_y': 3,
    'k_size_mag': 3,
    'k_size_dir': 15,
    'min_x': 20,
    'min_y': 30,
    'min_mag': 30,
    'min_dir': 50,
    'max_x': 100,
    'max_y': 75,
    'max_mag': 100,
    'max_dir': 80
}

angle_resolution = 100


def odd_number_conversion(val):
    return val * 2 + 1


def odd_to_number(val):
    return int((val - 1) / 2)


def new_kernel(kernel_name):
    def converter(val):
        params[kernel_name] = odd_number_conversion(val)
        update_all()

    return converter


def update_all():
    gradx = abs_sobel_thresh(image,
                             orient='x',
                             sobel_kernel=params['k_size_x'],
                             thresh=(params['min_x'], params['max_x'])
                             )
    grady = abs_sobel_thresh(image,
                             orient='y',
                             sobel_kernel=params['k_size_y'],
                             thresh=(params['min_y'], params['max_y'])
                             )
    mag_binary = mag_thresh(image,
                            sobel_kernel=params['k_size_mag'],
                            mag_thresh=(params['min_mag'], params['max_mag'])
                            )
    dir_binary = dir_threshold(image,
                               sobel_kernel=params['k_size_dir'],
                               thresh=(params['min_dir'], params['max_dir'])
                               )
    combined_binary = combine(gradx, grady, mag_binary, dir_binary)

    cv2.imshow('Gradx', convert_to_image(gradx))
    cv2.imshow('Grady', convert_to_image(grady))
    cv2.imshow('Magnitude', convert_to_image(mag_binary))
    cv2.imshow('Direction', convert_to_image(dir_binary))
    cv2.imshow('Combined', convert_to_image(combined_binary))


def create_kernel_track_bar(window_name, trackbar_name, kernel_name):
    cv2.createTrackbar(trackbar_name, window_name, odd_to_number(params[kernel_name]), 15, new_kernel(kernel_name))


if __name__ == '__main__':
    image = cv2.imread('signs_vehicles_xygrad.png')

    settings_windows = 'Settings'

    cv2.namedWindow(settings_windows)
    create_kernel_track_bar(settings_windows, "Kernel X", 'k_size_x')
    create_kernel_track_bar(settings_windows, "Kernel Y", 'k_size_y')
    create_kernel_track_bar(settings_windows, "Kernel Mag", 'k_size_mag')
    create_kernel_track_bar(settings_windows, "Kernel Dir", 'k_size_dir')

    update_all()

    cv2.waitKey()
    cv2.destroyAllWindows()
