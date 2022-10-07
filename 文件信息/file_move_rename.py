import os
import shutil

# base_dir = r'C:\Users\Kevin\Pictures\Saved Pictures\所有文件信息.xlsx'
# file_path = r'C:\Users\Kevin\Pictures\Saved Pictures'
# for roots, dirs, file_names in os.walk(base_dir):
#     for name in file_names:
#         file_path_name = os.path.join(roots, name)  # 含路径的文件名
#         file_dir = os.path.split(file_path_name)[0]  # 文件dir
#         file_name = os.path.split(file)[1]  # 文件名
#         file_left = os.path.splitext(name)[0]  # 文件名不含后缀
#         file_suf = os.path.splitext(name)[1]  # 文件后缀
#         file_size = os.path.getsize(file_path_name)
#         file_left = file_left.replace('（', '_')
#         insert_srt = 'SIM'+str(num)+'--'  # 文件名插入的字符
#         new_file_name = insert_srt + name_left[:] + name_right  # 文件名加减字符
#         new_file_path = os.path.join(file_dir, new_file_name)
#         try:
#             new_file_name = file_left + file_suf  # 文件名加减字符
#             new_file_path = os.path.join(roots, new_file_name)
#             os.rename(file_path_name, new_file_path)  # ⭐!!!重命名文件
#         except:
#             new_file_name = file_left+'_1' + file_suf  # 文件名加减字符
#             new_file_path = os.path.join(roots, new_file_name)
#             os.rename(file_path_name, new_file_path)  # ⭐!!!重命名文件


def del_dir(file_path):
    for roots, dirs, file_names in os.walk(file_path):
        for dir in dirs:
            file_path_name = os.path.join(roots, dir)
            try:
                os.rmdir(file_path_name)
                print('删除空文件夹：', file_path_name)
            except:
                # print('非空文件夹：', file_path_name)
                pass


def recvery_dir(file_path):
    for roots, dirs, file_names in os.walk(file_path):
        for name in file_names:
            file_path_name = os.path.join(roots, name)  # 含路径的文件名
            if roots != file_path:
                try:
                    shutil.move(file_path_name, file_path)  # ⭐!!!移动文件
                except Exception as e:
                    print('失败：',  file_path_name, type(e), e)


# file_path = r'D:\File_Restore-20221006'
# file_path = r'C:\Users\Kevin\Pictures\Saved Pictures'

recvery_dir(r'C:\Users\Kevin\Pictures\Saved Pictures')
del_dir(r'C:\Users\Kevin\Pictures\Saved Pictures')

# recvery_dir(r'D:\File_Restore-20221006')
# del_dir(r'D:\File_Restore-20221006')
