import cv2

image = cv2.imread(r'E:\22UCS030\bappa1.jpg')

if image is None:
    print("Image not properly uploaded.")
else:
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale Image", img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
