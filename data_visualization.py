from skimage import io
from numpy import *
import os
import warnings
warnings.filterwarnings("ignore")

# 将应用层payload的十六进制字节流转为二进制比特流，然后再将其转为图像
def data_visual(path):
    file_name = os.listdir(path)
    for name in file_name:
        file_path = os.path.join(path, name)
        name = name.split('.')[0]
        dir_path = path + '\\' + name + '_img'
        os.mkdir(dir_path)                         # 创建路径

        file = open(file_path, 'r')
        num = 0
        for line in file:
            line = bin(int('1' + line, 16))[3:]    # 将十六进制字节流转为二进制比特流
            n = len(line)
            m = math.ceil(n ** 0.5)
            m = m ** 2

            if (m != n):                           # 转为正方形的图像，若不能开方则补零
                line = line + '0' * (m - n)
            line = array([int(c) for c in list(line)])
            line[line == 1] = 255
            m = int(m ** 0.5)
            line = line.reshape(m, m)
            num = num + 1

            print('save no.' + str(num) + ' image')
            io.imsave(dir_path + '\\' + 'image' + str(num) + '.jpg', line)                # 保存图像
            if(num == 150):
                break


if __name__ == '__main__':
    data_visual(r'C:\Users\i-caijingxuan\Desktop\流量分析\比特流')
