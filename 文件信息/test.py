import cv2
import os
import shutil
import pandas as pd
import numpy as np
import pickle


def hist_similarity(img1, img2, hist_size=256):
    img1_hist_b = cv2.calcHist([img1], [0], None, [hist_size], [0, 256])
    img1_hist_g = cv2.calcHist([img1], [1], None, [hist_size], [0, 256])
    img1_hist_r = cv2.calcHist([img1], [2], None, [hist_size], [0, 256])
    img1_hist_b = img1_hist_b/np.sum(img1_hist_b)
    img1_hist_g = img1_hist_g/np.sum(img1_hist_g)
    img1_hist_r = img1_hist_r/np.sum(img1_hist_r)
    img2_hist_b = cv2.calcHist([img2], [0], None, [hist_size], [0, 256])
    img2_hist_g = cv2.calcHist([img2], [1], None, [hist_size], [0, 256])
    img2_hist_r = cv2.calcHist([img2], [2], None, [hist_size], [0, 256])
    img2_hist_b = img2_hist_b/np.sum(img2_hist_b)
    img2_hist_g = img2_hist_g/np.sum(img2_hist_g)
    img2_hist_r = img2_hist_r/np.sum(img2_hist_r)
    distance_b = cv2.compareHist(img1_hist_b, img2_hist_b, cv2.HISTCMP_CORREL)
    distance_g = cv2.compareHist(img1_hist_g, img2_hist_g, cv2.HISTCMP_CORREL)
    distance_r = cv2.compareHist(img1_hist_r, img2_hist_r, cv2.HISTCMP_CORREL)
    return (distance_b + distance_g + distance_r)/3


def get_file(file_path):
    df = pd.DataFrame(columns=('长文件名', '文件名', '后缀', '大小'))  # 信息表头
    img_df = pd.DataFrame(columns=('长文件名', '缩微图片数据'))  # 信息表头
    for roots, dirs, file_names in os.walk(file_path):
        for name in file_names:
            file_path_name = os.path.join(roots, name)  # 含路径的文件名
            file_suf = os.path.splitext(name)[1]  # 文件后缀
            file_size = os.path.getsize(file_path_name)
            if file_suf.lower() == '.jpg':
                df.loc[len(df)] = file_path_name, name, file_suf, file_size
                # 压缩图片到长边256
                img = cv2.imread(file_path_name)  # 中文文件名和路径会报错
                height = img.shape[0]
                width = img.shape[1]
                if height < width:
                    size = (256, int(height/width*256))
                else:
                    size = (int(width/height*256), 256)
                img = cv2.resize(img, size)
                img_df.loc[len(img_df)] = file_path_name, img
    print('文件预处理完成，文件数：', len(df))
    df['文件名相同'] = df.duplicated(subset='文件名', keep=False)
    df.to_excel(os.path.join(file_path, '文件信息.xlsx'))
    with open(os.path.join(file_path, 'Img_Data.dat'), 'wb') as f:
        pickle.dump(img_df, f)  # 预处理数据保存
    return img_df


def img_similarity(file_path):
    file_data = get_file(file_path)
    file_list = file_data['长文件名']
    img_data = file_data['缩微图片数据']
    file_num = len(file_list)

    df = pd.DataFrame(index=file_list, columns=file_list)
    for i in range(file_num):
        img_i = img_data[i]
        for j in range(i):
            img_j = img_data[j]
            if img_i.shape == img_j.shape:
                df.iloc[i, j] = hist_similarity(img_i, img_j)
            # 进度条
            print('\r', end='')
            bar = int((i*(i-1)/2+j+2)/(file_num*(file_num-1)/2)*100)
            print(bar, "%", '■'*bar, end="")
    print('\n相似度计算完成')
    df.to_excel(os.path.join(file_path, '图片相似度数据.xlsx'))
    return df


def sim_result(file_path, sim_degree=0.9):
    df = img_similarity(file_path)
    sim_list = []
    for i in range(len(df)):
        sim_set = set()
        for j in range(i):
            if df.iloc[i, j] > sim_degree:  # 默认相似度0.9
                sim_set.update([df.index[i], df.columns[j]])
        for item in sim_list:
            if item & sim_set:  # 集合有交集
                item.update(sim_set)
                break
        else:
            if sim_set:
                sim_list.append(sim_set)
    return sim_list


def file_rename_move(file_path):
    sim_files_list = sim_result(file_path)
    num = 100
    group_list = []
    for sim_files in sim_files_list:
        for file in sim_files:
            file_dir = os.path.split(file)[0]  # 文件dir
            file_name = os.path.split(file)[1]  # 文件名
            name_left = os.path.splitext(file_name)[0]  # 不含后缀的文件名
            name_right = os.path.splitext(file_name)[1]  # 文件后缀
            # 修改文件名
            # insert_srt = 'SIM'+str(num)+'--'  # 文件名插入的字符
            # new_file_name = insert_srt + name_left[:] + name_right  # 文件名加减字符
            # new_file_path = os.path.join(file_dir, new_file_name)
            # os.rename(file, new_file_path)  # ⭐!!!重命名文件
            group_list.append((num, file))
            # 移动同组文件
            insert_dir = 'SIM'+str(num)  # 创建子文件名
            new_path = os.path.join(file_path, insert_dir)  # 新路径
            if not os.path.exists(new_path):  # 文件夹不存在
                os.mkdir(new_path)  # 新建文件夹
            shutil.move(file, new_path)  # ⭐!!!移动名文件
        num += 1
    df = pd.DataFrame(group_list, columns=('分组', '文件名'))
    df.to_excel(os.path.join(file_path, '相似文件分组.xlsx'))


file_path = r'D:\File_Restore-20221003'  # 需要查找的根目录
file_rename_move(file_path)
