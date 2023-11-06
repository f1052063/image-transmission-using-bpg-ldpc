# **version 0.0**

本项目用于windows系统下实现bpg和ldpc的图像压缩传输。其中bpg编解码器采用github上的第三方库实现，[具体可以参考](https://github.com/mirrorer/libbpg)。ldpc编码采用的库是[pyldpc](https://pypi.org/project/pyldpc/)，直接pip就行了
使用的图片数据我存在onedrive里就是kodak数据集下载完直接丢在根目录下就行了（https://1drv.ms/f/s!As298sdrMHIMi02lVHxHsW9YUMuu?e=teh1F1）
kodak文件夹下的original_data为kodak数据集原始图像中的22张，还有两张俺之前忘记放了就懒得补了。。。

文件drive.py和sample1.py为单张图像的BPG编码器调用+LDPC编码、信道传输+LDPC解码+BPG解码调用的代码，文件show_bpg_numpy.py和bpgdec_by_psnr.py是针对某个文件夹下所有图像进行全自动PG编码器调用+LDPC编码、信道传输+LDPC解码+BPG解码的操作，其中bpgdec_by_psnr.py运行之后会展示计算出的平均psnr值。

ldpc信道编码这个东西很抽象，我一开始用的短信源发现效果不好捏，后面发现n=50 k=22 大概是个比较合理的区间，不论是解码时间还是最后的结果都较为不错，这里面的优化选择感觉可以搞个本科毕设出来。



后续会尝试更新一下更规范的版本，现在直接把代码一窝蜂丢进编解码器的根目录下忙着写中期报告懒得倒腾了
