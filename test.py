import cv2

cat_image = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
cv2.imshow('cat', cat_image)
cv2.waitKey(0)
