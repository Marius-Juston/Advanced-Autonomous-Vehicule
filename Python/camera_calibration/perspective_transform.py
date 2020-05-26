import cv2
import numpy as np

points = []
output_points = []
i = 0
z = 0


def mouse_press(event, x, y, _, param):
    global i, z

    output = np.copy(param['image'])

    if event == cv2.EVENT_LBUTTONUP:
        i += 1

        if i <= 4:
            points.append((x, y))
        else:
            points[i % 4] = (x, y)

    if event == cv2.EVENT_MBUTTONUP:
        y += 1

        if z <= 4:
            output_points.append((x, y))
        else:
            output_points[z % 4] = (x, y)

    if event == cv2.EVENT_RBUTTONUP and len(points) == 4 and len(output_points) == 4:
        M = cv2.getPerspectiveTransform(np.float32(points), np.float32(output_points))
        h, w, _ = output.shape
        output = cv2.warpPerspective(output, M, (w, h), flags=cv2.INTER_LINEAR)
        param['image'] = output
        points.clear()
        output_points.clear()
        i = 0
        z = 0
    else:
        for point in points:
            cv2.drawMarker(output, point, (255, 255, 0), thickness=4)

        for point in output_points:
            cv2.drawMarker(output, point, (255, 0, 255), thickness=4)

    cv2.imshow(window_title, output)


if __name__ == '__main__':
    image = cv2.imread('stop_sign.jpg')
    image = cv2.resize(image, (463, 500))

    window_title = 'Perspective Transform'

    cv2.imshow(window_title, image)
    cv2.setMouseCallback(window_title, mouse_press, param={'image': image})

    cv2.waitKey()
    cv2.destroyAllWindows()
