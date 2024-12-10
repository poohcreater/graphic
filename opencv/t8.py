import cv2


def main():
    image = cv2.imread('../img/dog_run.jpg')

    ret, binary = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

    cv2.imshow('image', image)
    cv2.imshow('binary', binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
