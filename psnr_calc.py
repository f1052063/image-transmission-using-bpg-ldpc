import cv2
import numpy as np

def calculate_psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 10 * np.log10(max_pixel**2 / mse)
    return psnr

# 读取原始图像和压缩后的图像
original_img = cv2.imread('original02.png', cv2.IMREAD_GRAYSCALE)
compressed_img = cv2.imread('output.png', cv2.IMREAD_GRAYSCALE)

# 计算 PSNR
psnr = calculate_psnr(original_img, compressed_img)
print(f"PSNR: {psnr}")
