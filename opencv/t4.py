import cv2
import numpy as np

image = cv2.imread('../img/dog_run.jpg')

# 画像の移動量を決定し変数に格納
img3 = np.float32([[1, 0, 50], [0, 1, 30]])

# 画像の平行移動
move = cv2.warpAffine(image, img3, (500, 300))

# show
cv2.imshow('move', move)

cv2.waitKey(0)
cv2.destroyAllWindows()
