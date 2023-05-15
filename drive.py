import os

root_dir = 'D:\\bpgmaster\\kodak\\'
for item in os.listdir(root_dir):   # 遍历root_dir
        name = root_dir + item
        save_dir = 'D:\\bpgmaster\\kodak\\encode\\'   # 存储编码结果
        save_dir1 = 'D:\\bpgmaster\\kodak\\decode\\'   # 存储解码结果
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        if not os.path.exists(save_dir1):
            os.makedirs(save_dir1)

        os.system('.\\bpgenc -m 9 -b 8 -q 35 ' + name + ' -o ' + save_dir + item.split('.')[0] + '.bin')
        os.system('.\\bpgdec -o ' + save_dir1 + item.split('.')[0] + '.png' + ' ' + save_dir + item.split('.')[0] + '.bin')
