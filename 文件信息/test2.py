import os

base_dir = r'C:\Users\Kevin\Pictures\Saved Pictures\所有文件信息.xlsx'
for roots, dirs, file_names in os.walk(base_dir):
    for name in file_names:
        file_path_name = os.path.join(roots, name)  # 含路径的文件名
        file_left = os.path.splitext(name)[0]  # 文件后缀
        file_suf = os.path.splitext(name)[1]  # 文件后缀
        file_size = os.path.getsize(file_path_name)
        file_left = file_left.replace('（', '_')
        file_left = file_left.replace('）', '')
        file_left = file_left.replace(' ', '')

        try:
            new_file_name = file_left + file_suf  # 文件名加减字符
            new_file_path = os.path.join(roots, new_file_name)
            os.rename(file_path_name, new_file_path)  # ⭐!!!重命名文件
        except:
            new_file_name = file_left+'_01' + file_suf  # 文件名加减字符
            new_file_path = os.path.join(roots, new_file_name)
            os.rename(file_path_name, new_file_path)  # ⭐!!!重命名文件
