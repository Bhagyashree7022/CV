import cv2
import matplotlib.pyplot as plt


img = cv2.imread("tom.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  

# ----------------------------
# Smoothing Techniques
# ----------------------------

# 1. Average Blurring (Mean Filter)
blur_avg = cv2.blur(img, (5, 5))

# 2. Gaussian Blurring
blur_gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# 3. Median Blurring
blur_median = cv2.medianBlur(img, 5)

# 4. Bilateral Filtering (edge-preserving smoothing)
blur_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# Display Results
titles = ['Original', 'Average Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, blur_avg, blur_gaussian, blur_median, blur_bilateral]

plt.figure(figsize=(12, 8))
for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()
