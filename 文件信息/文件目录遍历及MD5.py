import os
import time
import sys
import hashlib
import pandas as pd


def check_md5(file_name):  # 计算MD5
    checksum = hashlib.md5()
    with open(file_name, 'rb') as fp:
        while True:
            buffer = fp.read(51200)  # 分块读MD，速度快
            if not buffer:
                break
            checksum.update(buffer)
    return checksum.hexdigest()


def get_total_size(file_path):  # 获取文件夹内所有文件大小
    file_size = 0
    for roots, dirs, file_names in os.walk(file_path):
        for name in file_names:
            file_name = os.path.join(roots, name)  # 含路径的文件名
            file_size += os.path.getsize(file_name)
    return file_size


def Time_localtime(timestamp):  # 日期格式转换
    stime = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', stime)


def Get_CreatTime(fpath):  # 获取文件创建时间
    t = os.path.getctime(fpath)
    return Time_localtime(t)


def Get_ModifyTime(fpath):  # 获取文件修改时间
    t = os.path.getmtime(fpath)
    return Time_localtime(t)


def get_file_info(file_path, save_path):
    # 信息表头
    df = pd.DataFrame(columns=('长文件名', '文件名', '后缀',
                      '大小', 'MD5', '创建时间', '修改时间'))
    total_size = get_total_size(file_path)
    file_sizes = 0
    for roots, dirs, file_names in os.walk(file_path):
        for name in file_names:
            file_name = os.path.join(roots, name)  # 含路径的文件名
            file_suf = os.path.splitext(name)[1]  # 文件后缀
            file_size = os.path.getsize(file_name)
            file_md5 = check_md5(file_name)
            df.loc[len(df)] = file_name, name, file_suf, file_size, file_md5,\
                Get_CreatTime(file_name), Get_ModifyTime(file_name)
            # 进度条
            file_sizes += file_size
            percent = int(file_sizes/total_size*100/2)
            print('\r', end='')
            print(percent*2, "%", '■'*percent, '>', len(df), end="")
            # sys.stdout.flush()

    df.sort_values(by='文件名', ascending=False, inplace=True)  # 按文件名排序
    df.index = range(len(df))  # 重新编号
    df['重复文件'] = df.duplicated(subset='MD5', keep=False)
    df['文件相同'] = df.duplicated(subset='文件名', keep=False)
    df.to_excel(save_path)


file_path = r'D:\File_Restore-20221003'  # 需要查找的根目录
save_path = r'C:\Users\Kevin\Documents\所有文件信息.xlsx'  # 结果保存
get_file_info(file_path, save_path)
