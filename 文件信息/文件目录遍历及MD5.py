import os
import hashlib
import pandas as pd

root_dir = r'D:\手机文档'  # 需要查找的根目录
save_path = r'D:\python\data\所有文件信息MD5.xlsx'  # 结果保存
df = pd.DataFrame(columns=('长文件名', '文件名', '后缀', '大小', 'MD5'))


def check_md5(file):
    checksum = hashlib.md5()
    with open(file, 'rb') as fp:
        while True:
            buffer = fp.read(65536)  # 计算MD5分块读MD，速度快
            if not buffer:
                break
            checksum.update(buffer)
    return checksum.hexdigest()

file_num = 0
for roots, dirs, files in os.walk(root_dir):
    for name in files:
        file_name = os.path.join(roots, name)  # 含路径的文件名
        file_suf = os.path.splitext(name)[1]  # 文件后缀
        file_size = os.path.getsize(file_name)
        file_md5 = check_md5(file_name)
        df.loc[file_num] = file_name, name, file_suf, file_size, file_md5
        file_num += 1

df['重复文件'] = df.duplicated(subset='MD5', keep=False)
df.to_excel(save_path)
