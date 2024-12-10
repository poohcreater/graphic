import cv2


def main():
    image = cv2.imread('../img/dog_run.jpg')

    blurred = cv2.blur(image, (5, 5))

    cv2.imshow('blurred', blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
