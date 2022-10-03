import os
import pandas as pd


def del_file(fileList):  # 删除Excel中的文件列表
    df = pd.read_excel(fileList, header=None)
    for file in df[0]:
        try:
            os.remove(file)
            # print('删除成功:', file)
        except:
            print('删除失败:', file)


fileList = r'C:\Users\Kevin\Documents\删除文件列表.xlsx'
# del_file(fileList)


def file_rename(base_dir):  # 文件重命名
    for roots, dirs, file_names in os.walk(base_dir):
        for name in file_names:
            file_path = os.path.join(roots, name)  # 含路径的文件名
            name_left = os.path.splitext(name)[0]  # 不含后缀文件名
            name_right = os.path.splitext(name)[1]  # 文件后缀
            # 把上一级文件夹名称加上
            new_file_name = roots.split('\\')[-1]+'--'+name_left+name_right
            # 二选一，去掉文件名最后10个字符，文件头加上日期
            new_file_name = '202210--'+name_left[0:-10]+name_right

            new_file_path = os.path.join(roots, new_file_name)
            os.rename(file_path, new_file_path)


base_dir = r'C:\Users\Kevin\Documents\文件夹名'  # 根目录
# file_rename(base_dir)
