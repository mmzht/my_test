import os
import hashlib
import pandas as pd

base_dir = r'D:\mate20'  # 需要查找的根目录
save_path = r'C:\Users\Kevin\Documents\文件信息.xlsx'  # 结果保存
df = pd.DataFrame(columns=('长文件名', '文件名', '后缀', '大小', 'MD5'))


def check_md5(file_name):
    checksum = hashlib.md5()
    with open(file_name, 'rb') as fp:
        while True:
            buffer = fp.read(51200)  # 分块读MD，速度快
            if not buffer:
                break
            checksum.update(buffer)
    return checksum.hexdigest()


file_num = 0
for roots, dirs, file_names in os.walk(base_dir):
    for name in file_names:
        file_name = os.path.join(roots, name)  # 含路径的文件名
        file_suf = os.path.splitext(name)[1]  # 文件后缀
        file_size = os.path.getsize(file_name)
        file_md5 = check_md5(file_name)
        df.loc[file_num] = file_name, name, file_suf, file_size, file_md5
        file_num += 1


df.sort_values(by='长文件名', ascending=False, inplace=True)  # 排序
df.index = range(file_num)  # 重新编号
# df['歌手', '歌名'] = df['文件名'].str.split('-')
df['重复文件'] = df.duplicated(subset='MD5', keep=False)
df.to_excel(save_path)
