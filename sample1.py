import numpy as np
import pyldpc
import time
# 读取二进制数据文件，并进行0-1比特化
with open('D:\\bpgmaster\\kodak\\encode\\kodim01.bin', 'rb') as f:
    data = np.unpackbits(np.fromfile(f, dtype=np.uint8))
print(data.shape)
n = 15
d_v = 3
d_c = 5
snr = 10
encode_start_time = time.time()
seed = np.random.RandomState(42)
H, G = pyldpc.make_ldpc(n, d_v, d_c, seed=seed, systematic=True, sparse=True)
print(H)
print(G)
# 将数据分成块，并按照k的大小进行划分



#n,k = G.shape
#n_blocks = len(data) // k
#data_blocks = np.reshape(data[:n_blocks * k], (-1, k))
#print(data_blocks.shape)

n, k = G.shape
n_blocks = len(data) // k
remainder = len(data) % k

# 如果有剩余数据，将其填充到长度为 k 的新数据块中
if remainder > 0:
    padding_len = k - remainder
    last_block = np.pad(data[n_blocks * k:], (0, padding_len), mode='constant')
    data_blocks = np.vstack((data[:n_blocks * k].reshape(-1, k), last_block))
else:
    data_blocks = data[:n_blocks * k].reshape(-1, k)
    padding_len = 0

print(data_blocks.shape)


# 对每个块进行LDPC编码
#encoded_data_blocks = np.empty((n_blocks, n), dtype=np.uint8)
#decoded_data_blocks = np.empty((n_blocks, k), dtype=np.uint8)
#print(data_blocks[1])
encoded_data_blocks = pyldpc.encode(G, data_blocks.T, snr, seed=seed)
# 记录编码结束时间
encode_end_time = time.time()

# 计算编码耗时
encoding_time = encode_end_time - encode_start_time
print(f"编码耗时：{encoding_time} 秒")

decode_start_time = time.time()
#print(encoded_data_blocks)
y = pyldpc.decode(H, encoded_data_blocks, snr, maxiter=1000)

#for i in range (data_blocks.shape[0]):
#    decoded_data_blocks = pyldpc.get_message(G, y.T[i])
#    print(decoded_data_blocks)
# 将编码后的数据保存为二进制文件
decoded_data_blocks_all = np.concatenate([pyldpc.get_message(G, y.T[i]) for i in range(data_blocks.shape[0])])

# 记录解码结束时间
decode_end_time = time.time()

# 计算解码耗时
decoding_time = decode_end_time - decode_start_time
print(f"解码耗时：{decoding_time} 秒")
# 将01比特流打包成uint8类型
print(decoded_data_blocks_all)

if padding_len > 0:
    decoded_data_blocks_all = decoded_data_blocks_all[:-padding_len]

decoded_data_blocks_all = np.packbits(decoded_data_blocks_all)



# 将解码后的数据写入二进制文件
with open('decoded_data_kodim02.bin', 'wb') as f:
    decoded_data_blocks_all.tofile(f)

