import cv2

image = cv2.imread('../img/dog_run.jpg')
img0 = cv2.resize(image, (250, 180))

cv2.imshow('Resize', img0)
cv2.imshow('Default', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
