import cv2

params = {
    'k_size_x': 3,
    'k_size_y': 3,
    'k_size_mag': 3,
    'k_size_dir': 15,
    'min_x': 0,
    'min_y': 0,
    'min_mag': 0,
    'min_dir': 0,
    'max_x': 0,
    'max_y': 0,
    'max_mag': 0,
    'max_dir': 0
}

angle_resolution = 100


def odd_number_conversion(val):
    return val * 2 + 1


def odd_to_number(val):
    return int((val - 1) / 2)


def new_kernel(kernel_name):
    def converter(val):
        params[kernel_name] = val
        update_all()

    return converter


def update_all():
    pass


if __name__ == '__main__':
    settings_windows = 'Settings'

    cv2.namedWindow(settings_windows)
    cv2.createTrackbar("Kernel Sobel X", settings_windows, odd_to_number(params['k_size_x']), 10,
                       new_kernel('k_size_x'))

    cv2.waitKey()
    cv2.destroyAllWindows()
