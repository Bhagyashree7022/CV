import cv2

image=cv2.imread(r'E:\22UCS030\bappa1.jpg')

if image is None:
    print("image not properly uploaded")
else:
    cv2.imshow('Image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
