import numpy as np
import pyldpc
import math
# 读取二进制数据文件
with open('D:\\bpgmaster\\kodak\\encode\\kodim01.bin', 'rb') as f:
    data = np.fromfile(f, dtype=np.uint8)
print(data)
n = 15
d_v = 4
d_c = 5
snr = 1000
H, G = pyldpc.make_ldpc(n, d_v, d_c, systematic=True, sparse=True)# 将数据分成块
k = G.shape[1]
v = np.random.randint(2, size=k)

n_blocks = len(data) // k
data_blocks = np.reshape(data[:n_blocks*k], (-1, k))

# 对每个块进行LDPC编码
encoded_data_blocks = np.empty((n_blocks, n), dtype=np.uint8)
decoded_data_blocks = np.empty((n_blocks, k), dtype=np.uint8)
for i in range(n_blocks):
    encoded_data_blocks[i] = pyldpc.encode(G, data_blocks[i], snr)
    decoded_data_blocks[i] = pyldpc.get_message(G, pyldpc.decode(H, encoded_data_blocks[i], snr))
print(encoded_data_blocks)
print(decoded_data_blocks)
#x = get_message(G, d)
#assert abs(x - data).sum() == 0
# 将编码后的数据保存为二进制文件
with open('decoded_data.bin', 'wb') as f:
    encoded_data_blocks.tofile(f)

