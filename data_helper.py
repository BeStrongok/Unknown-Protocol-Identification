from scapy.all import *
import pandas as pd
import os


# 读取pcap文件，并返回其应用层payload部分对应的十六进制字符串，然后生成csv文件进行后续的特征工程
def dataset_cre(path):
    file_list = os.listdir(path)
    # 读取文件夹中的每个pcap文件
    for file_name in file_list:
        file_path = os.path.join(path, file_name)
        file_name = file_name.split('.')[0]
        print('read ' + file_name + ' pcap file')
        pkts = rdpcap(file_path)
        # 定义一个的列表保存读取pcap文件得到的结果
        results = []
        # 读取txt文件，没有的话就创建一个，'a'表示再次写入时不覆盖之前的内容
        f = open(file_name + '.txt', 'a')

        # 读取当前pcap文件中的每个数据包
        for i in range(len(pkts)):
            pkt = pkts[i]
            result = []
            # 定位到应用层payload部分并提取出十六进制字符串
            pkt_load = pkt.payload.payload.payload
            pkt_strs = hexdump(pkt_load, True)
            # 将十六进制字符串按照换行符进行分隔并返回一个字符串列表
            pkt_strs = pkt_strs.split('\n')

            for j in range(len(pkt_strs)):
                pkt_str = pkt_strs[j]
                pkt_str = pkt_str[6: 53].split(' ')
                # 对最后一行字符串进行去掉空字符处理，因为最后一行如果不是标准的16个十六进制字符的话，那么
                # pkt_str的长度一定是大于16的
                if(len(pkt_str) > 16):
                    pkt_str = list(filter(None, pkt_str))
                result.append(pkt_str)

            result = "".join(itertools.chain(*result))
            f.write(result)
            f.write('\n')
        f.close()


if __name__ == '__main__':
    dataset_cre(r'C:\Users\i-caijingxuan\Desktop\流量分析\数据集')