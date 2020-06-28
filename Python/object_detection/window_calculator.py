def number_of_windows(image_length, window_length, overlap_proportion):
    return 1 + (image_length - window_length) / (window_length * overlap_proportion)


def total_windows(image_shape, window_shape, overlap_proportion):
    windows_h = number_of_windows(image_shape[0], window_shape[0], overlap_proportion)
    windows_w = number_of_windows(image_shape[1], window_shape[1], overlap_proportion)

    return windows_h * windows_w


if __name__ == '__main__':
    image_shape = (960, 1280)
    window_shape = (64, 64)
    overlap = 0.5

    print(total_windows(image_shape, window_shape, overlap))
