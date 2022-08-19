# 批量删除指定后缀的文件
from pathlib import Path
import os

fileList = r'D:\python\data\已删除文件列表.txt'

filepath = Path(r'D:\python\data')  # 需要删除文件所在的目录
with open(fileList, 'w') as f:
    f.write('======已删除文件列表=====\n')

for filename in filepath.rglob('*.tmp'):  # *.后缀：文件名用星号表示，点后面是后缀名
    try:
        with open(fileList, "a+") as f:
            f.write(str(filename) + "\n")
        os.remove(filename)
    except:
        print(str(filename) + '文件打开错误')
        os.remove(filename)
