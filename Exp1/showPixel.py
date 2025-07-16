import cv2

image=cv2.imread(r'E:\22UCS030\bappa1.jpg')

if image is None:
    print("image not properly uploaded")
else:
    height,width,channel=image.shape
    for y in range(height):
     for x in range(width):
        b, g, r = image[y, x] 
        print(f'Pixel at ({x},{y}): B={b}, G={g}, R={r}')
