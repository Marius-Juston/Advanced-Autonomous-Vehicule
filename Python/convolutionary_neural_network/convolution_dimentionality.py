def output_dimension(input_size, K, filter_size, stride, padding):
    new_height = int((input_size[0] - filter_size[0] + 2 * padding) / stride + 1)
    new_width = int((input_size[1] - filter_size[1] + 2 * padding) / stride + 1)
    return new_height, new_width, K


if __name__ == '__main__':
    output = output_dimension((32, 32, 3), 20, (8, 8, 3), 2, 1)
    print('x'.join(map(str, output)))
