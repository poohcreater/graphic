import cv2

# 画像読み込みと色変換
image = cv2.imread('../img/opencv_test_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("画像を変換しました")

# 画像表示
cv2.imshow('Default Image', image)
cv2.imshow('Gray Image', gray_image)

# キー入力
cv2.waitKey(0)
cv2.destroyAllWindows()
