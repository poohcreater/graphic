import cv2


def main():
    image = cv2.imread('../img/dog_run.jpg')

    rows, cols = image.shape[:2]

    change = cv2.getRotationMatrix2D((cols / 2, rows / 2), 60, 0.5)

    rotated = cv2.warpAffine(image, change, (cols, rows))

    # cv2.imshow('base', image)
    cv2.imshow("rotated", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
