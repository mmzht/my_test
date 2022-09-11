from pathlib import Path
import os
import pandas as pd
# 删除的文件名写入txt中
'''
fileList = r'C:\Users\Kevin\Documents\删除文件列表.txt'
filepath = Path(r'C:\Users\Kevin\Documents')  # 需要删除文件所在的目录
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
'''

# 删除Excel中的文件列表
fileList = r'C:\Users\Kevin\Documents\删除文件列表.xlsx'
df = pd.read_excel(fileList)
for file in df:
    try:
        os.remove(file)
        print(file)
    except:
        print(file, '删除失败')
