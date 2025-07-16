import cv2
path=r'E:\22UCS030\bappa1.jpg'
image=cv2.imread(path)

if image is None:
    print("image not properly uploaded")
else:
    roteted_img =cv2.rotate(image,  cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Image_90clock",roteted_img)
    cv2.waitKey(0)

    roteted_img =cv2.rotate(image,  cv2.ROTATE_180)
    cv2.imshow("Image _180",roteted_img)
    cv2.waitKey(0)


    roteted_img =cv2.rotate(image,  cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Image_90Aniticlc",roteted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
