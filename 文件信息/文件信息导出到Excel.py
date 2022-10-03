import os
import hashlib
import pandas as pd


def check_md5(file_name):
    checksum = hashlib.md5()
    with open(file_name, 'rb') as fp:
        while True:
            buffer = fp.read(51200)  # 分块读MD，速度快
            if not buffer:
                break
            checksum.update(buffer)
    return checksum.hexdigest()


base_dir = r'D:\mate20\mate20音乐'  # 需要查找的根目录
save_path = r'C:\Users\Kevin\Documents\文件信息.xlsx'  # 结果保存
df = pd.DataFrame(columns=('长文件名', '文件名', '后缀', '大小', 'MD5'))

for roots, dirs, file_names in os.walk(base_dir):
    for name in file_names:
        file_name = os.path.join(roots, name)  # 含路径的文件名
        file_suf = os.path.splitext(name)[1]  # 文件后缀
        file_size = os.path.getsize(file_name)
        file_md5 = check_md5(file_name)
        df.loc[len(df)] = file_name, name, file_suf, file_size, file_md5

song = df['文件名'].str.split('-')
df['歌手'] = song.str[0].str.strip()
df['歌名'] = song.str[1].str.strip()
df.sort_values(by='歌名', ascending=False, inplace=True)  # 排序
df.index = range(len(df))  # 重新编号
df['歌手重复'] = df.duplicated(subset='歌手', keep=False)
df['歌名重复'] = df.duplicated(subset='歌名', keep=False)
# df['重复文件'] = df.duplicated(subset='MD5', keep=False)
df.to_excel(save_path)
