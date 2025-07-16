import cv2

image = cv2.imread(r'E:\22UCS030\bappa1.jpg')

if image is None:
    print("Image not properly uploaded.")
else:
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height, width = img_gray.shape
    for y in range(height):
        for x in range(width):
            print(f"Pixel at ({x},{y}): {img_gray[y, x]}")
