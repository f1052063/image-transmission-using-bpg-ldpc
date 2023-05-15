import os
import numpy as np
import cv2


def calculate_psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 10 * np.log10(max_pixel**2 / mse)
    return psnr

root_dir = 'D:\\bpgmaster\\kodak\\original_data\\'
total_psnr = 0  # 用于累加 PSNR 的变量
image_count = 0  # 记录图像数量的变量

for item in os.listdir(root_dir):   # 遍历 root_dir
    image_count += 1
    name = root_dir + item
    save_dir = 'D:\\bpgmaster\\kodak\\encode\\'   # 存储编码结果
    save_dir1 = 'D:\\bpgmaster\\kodak\\ldpc_decode\\'   # 存储解码结果

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    if not os.path.exists(save_dir1):
        os.makedirs(save_dir1)

    os.system('.\\bpgdec -o ' + save_dir1 + item.split('.')[0] + '.png' + ' ' + save_dir + item.split('.')[0] + '.bin')
    compressed_img  = cv2.imread(save_dir1 + item.split('.')[0] + '.png' , cv2.IMREAD_GRAYSCALE)
    original_img= cv2.imread(root_dir + item.split('.')[0] + '.png', cv2.IMREAD_GRAYSCALE)

    # 计算 PSNR
    psnr = calculate_psnr(original_img, compressed_img)
    total_psnr += psnr
    print(f"PSNR: {psnr}")

# 计算平均 PSNR
average_psnr = total_psnr / image_count
print(f"平均 PSNR: {average_psnr}")
