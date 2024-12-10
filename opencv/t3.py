import cv2

image = cv2.imread('../img/dog_run.jpg')

img0 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow('color', img0)

cv2.waitKey(0)
cv2.destroyAllWindows()
