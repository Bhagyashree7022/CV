import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("tom.jpg")   
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ----------------------------
# 1. First Derivative Methods
# ----------------------------

# Sobel Operator on each channel
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Prewitt Operator (manually defined kernel) on each channel
kernel_prewitt_x = np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
kernel_prewitt_y = np.array([[-1,-1,-1], [0,0,0], [1,1,1]])

prewitt_x = cv2.filter2D(img, -1, kernel_prewitt_x)
prewitt_y = cv2.filter2D(img, -1, kernel_prewitt_y)
prewitt_combined = cv2.magnitude(prewitt_x.astype(float), prewitt_y.astype(float))

# ----------------------------
# 2. Second Derivative (Laplacian)
# ----------------------------
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# ----------------------------
# 3. Sharpening with Laplacian
# ----------------------------
sharpened = cv2.convertScaleAbs(img - 0.7 * laplacian)

# ----------------------------
# Display Results
# ----------------------------
titles = ['Original (Color)',
          'Sobel (Gradient)', 'Prewitt (Gradient)',
          'Laplacian (2nd Derivative)', 'Sharpened (Laplacian)']

images = [img, sobel_combined, prewitt_combined, laplacian, sharpened]

plt.figure(figsize=(12, 8))
for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i].astype(np.uint8))
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()
