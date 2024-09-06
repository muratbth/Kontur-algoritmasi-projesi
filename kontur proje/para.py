import cv2


img = cv2.imread(r"D:\picture\2\coins3.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


threshold_value = 60


_, thresholded_img = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)


contours, _ = cv2.findContours(thresholded_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)


cv2.imshow("org", img)
cv2.imshow("Thresholded Image", thresholded_img)
cv2.imshow("Contours", contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


