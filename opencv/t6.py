import cv2
import numpy as np


def main():
    image = cv2.imread('../img/dog_run.jpg')

    rows, cols = image.shape[:2]

    pts1 = np.float32([[40, 40], [400, 50], [10, 200]])
    pts2 = np.float32([[20, 100], [400, 50], [100, 270]])
    change = cv2.getAffineTransform(pts1, pts2)

    affine = cv2.warpAffine(image, change, (cols, rows))

    cv2.imshow('Affine', affine)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
