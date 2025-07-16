import cv2

image=cv2.imread(r'E:\22UCS030\bappa1.jpg')

if image is None:
    print("image not properly uploaded")
else:
    img=cv2.resize(image,(800,600))
    cv2.imshow("Image",img)
    cv2.waitKey(0)
