import os
import shutil
import pandas as pd
import pickle
import imagehash
from PIL import Image
# 效果Whash>Hist>pHash


def get_file(file_path):
    df = pd.DataFrame(columns=('长文件名', '文件名', '后缀', '大小'))  # 信息表头
    img_df = pd.DataFrame(columns=('长文件名', 'HASH'))  # 信息表头
    for roots, dirs, file_names in os.walk(file_path):
        for name in file_names:
            file_path_name = os.path.join(roots, name)  # 含路径的文件名
            file_suf = os.path.splitext(name)[1]  # 文件后缀
            file_size = os.path.getsize(file_path_name)
            if file_suf.lower() == '.jpg':
                df.loc[len(df)] = file_path_name, name, file_suf, file_size
                img = Image.open(file_path_name)  # 中文文件名和路径会报错
                phash = imagehash.phash(img)  # phash
                img_df.loc[len(img_df)] = file_path_name, phash
    print('文件预处理完成，文件数：', len(df))
    df['文件名相同'] = df.duplicated(subset='文件名', keep=False)
    df.to_excel(os.path.join(file_path, '文件信息.xlsx'))
    with open(os.path.join(file_path, 'Img_phash_Data.dat'), 'wb') as f:
        pickle.dump(img_df, f)  # 预处理数据保存
    return img_df


def img_similarity(img_df):  # pd '长文件名', '缩微图片数据'
    file_list = img_df['长文件名']
    img_data = img_df['HASH']
    file_num = len(file_list)
    sim_df = pd.DataFrame(index=file_list, columns=file_list)
    for i in range(file_num):
        img_i = img_data[i]
        for j in range(i):
            img_j = img_data[j]
            sim_df.iloc[i, j] = int(
                (1 - (img_i - img_j)/len(img_i.hash)**2)*100)
            # 进度条
            print('\r', end='')
            bar = int((i*(i-1)/2+j+2)/(file_num*(file_num-1)/2)*100)
            print(bar, "%", '■'*bar, end="")
    print('\n相似度计算完成')
    return sim_df


def sim_result(sim_df, sim_degree=70):
    sim_list = []
    for i in range(len(sim_df)):
        sim_set = set()
        for j in range(i):
            if sim_df.iloc[i, j] > sim_degree:  # 默认相似度
                sim_set.update([sim_df.index[i], sim_df.columns[j]])
        if sim_set:
            if sim_list:
                for item in sim_list:  # 取列表中的一个集合；
                    if item & sim_set:  # 如何两个集合有交集
                        item.update(sim_set)  # 则等于并集
                        break
                else:
                    sim_list.append(sim_set)  # 没有找到交集的，则直接添加
            else:
                sim_list.append(sim_set)

    for m in range(len(sim_list)):  # 取列表中的一个集合；
        for n in range(len(sim_list)):
            if sim_list[m] & sim_list[n]:  # 如何两个集合有交集
                sim_list[n] = sim_list[m] | sim_list[n]  # 则等于并集
    sim_list_no_repeat = []
    for item in sim_list:  # 去掉重复元素
        if item not in sim_list_no_repeat:
            sim_list_no_repeat.append(item)
    return sim_list_no_repeat


def file_rename_move(sim_list, file_path):
    num = 100
    group_list = []
    for sim_files in sim_list:
        for file in sim_files:
            file_dir = os.path.split(file)[0]  # 文件dir
            # 修改文件名
            # file_name = os.path.split(file)[1]  # 文件名
            # name_left = os.path.splitext(file_name)[0]  # 不含后缀的文件名
            # name_right = os.path.splitext(file_name)[1]  # 文件后缀
            # insert_srt = 'SIM'+str(num)+'--'  # 文件名插入的字符
            # new_file_name = insert_srt + name_left[:] + name_right  # 文件名加减字符
            # new_file_path = os.path.join(file_dir, new_file_name)
            # os.rename(file, new_file_path)  # ⭐!!!重命名文件
            group_list.append((num, file))
            # 移动同组文件
            insert_dir = 'P'+str(num)  # 创建子文件名
            new_path = os.path.join(file_path, insert_dir)  # 新路径
            if not os.path.exists(new_path):  # 文件夹不存在
                os.mkdir(new_path)  # 新建文件夹
            if file_dir != new_path:
                try:
                    shutil.move(file, new_path)  # ⭐!!!移动名文件
                except Exception as e:
                    print('失败：',  new_path, type(e), e)
        num += 1
    group_df = pd.DataFrame(group_list, columns=('分组', '文件名'))
    group_df.to_excel(os.path.join(file_path, '相似文件分组.xlsx'))


# file_path = r'D:\File_Restore-20221006'  # 需要查找的根目录
file_path = r'C:\Users\Kevin\Pictures\Saved Pictures'  # 需要查找的根目录
img_df = get_file(file_path)

sim_df = img_similarity(img_df)
# with open(os.path.join(file_path, 'Img_phash_Data.dat'), 'wb') as f:
#     img_df = pickle.load(f)  # 读取预处理数据

sim_list = sim_result(sim_df, sim_degree=75)
file_rename_move(sim_list, file_path)
sim_df.to_excel(os.path.join(file_path, '图片相似度数据.xlsx'))
