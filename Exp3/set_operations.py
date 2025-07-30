import cv2

image1=cv2.imread(r'E:\22UCS030\Exp3\tom1.jpg')

if image1 is None:
    print("image not properly uploaded")
else:
    img1=cv2.resize(image1,(800,600))
    cv2.imshow("Image",img1)
    cv2.waitKey(0)

import cv2

image2=cv2.imread(r'E:\22UCS030\Exp3\tom2.jpg')

if image2 is None:
    print("image not properly uploaded")
else:
    img2=cv2.resize(image2,(800,600))
    cv2.imshow("Image",img2)
    cv2.waitKey(0)

#union
img3=cv2.bitwise_or(img1,img2)
cv2.imshow("UNION",img3)
cv2.waitKey(0)

#intersection
img4=cv2.bitwise_and(img1,img2)
cv2.imshow("INTERSECTION",img4)
cv2.waitKey(0)

