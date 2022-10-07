import cv2
import os
import shutil
import pandas as pd
import pickle
# 效果Whash>Hist>pHash


def hist_similarity(img1, img2, hist_size=256):
    img1_hist_b = cv2.calcHist([img1], [0], None, [hist_size], [0, 256])
    img1_hist_g = cv2.calcHist([img1], [1], None, [hist_size], [0, 256])
    img1_hist_r = cv2.calcHist([img1], [2], None, [hist_size], [0, 256])

    img2_hist_b = cv2.calcHist([img2], [0], None, [hist_size], [0, 256])
    img2_hist_g = cv2.calcHist([img2], [1], None, [hist_size], [0, 256])
    img2_hist_r = cv2.calcHist([img2], [2], None, [hist_size], [0, 256])
    distance_b = cv2.compareHist(
        img1_hist_b, img2_hist_b, cv2.HISTCMP_BHATTACHARYYA)
    distance_g = cv2.compareHist(
        img1_hist_g, img2_hist_g, cv2.HISTCMP_BHATTACHARYYA)
    distance_r = cv2.compareHist(
        img1_hist_r, img2_hist_r, cv2.HISTCMP_BHATTACHARYYA)
    return 1-(distance_b + distance_g + distance_r)/3


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
                size = (256, 256)  # 缩放到相同
                img = cv2.resize(img, size)
                img_df.loc[len(img_df)] = file_path_name, img
    print('文件预处理完成，文件数：', len(df))
    df['文件名相同'] = df.duplicated(subset='文件名', keep=False)
    df.to_excel(os.path.join(file_path, '文件信息.xlsx'))
    # with open(os.path.join(file_path, 'Img_hist_Data.dat'), 'wb') as f:
    #     pickle.dump(img_df, f)  # 预处理数据保存
    return img_df


def img_similarity(img_df):  # pd '长文件名', '缩微图片数据'
    file_list = img_df['长文件名']
    img_data = img_df['缩微图片数据']
    file_num = len(file_list)

    sim_df = pd.DataFrame(index=file_list, columns=file_list)
    for i in range(file_num):
        img_i = img_data[i]
        for j in range(i):
            img_j = img_data[j]
            if img_i.shape == img_j.shape:
                degree = hist_similarity(img_i, img_j)
                sim_df.iloc[i, j] = int(degree*100)
            # 进度条
            print('\r', end='')
            bar = int((i*(i-1)/2+j+2)/(file_num*(file_num-1)/2)*100)
            print(bar, "%", '='*bar, '-'*(100-bar), end="")
    print('\nHist相似度计算完成')
    with open(os.path.join(file_path, 'Img_hist_sim.dat'), 'wb') as f:
        pickle.dump(sim_df, f)  # 相似度数据保存
    return sim_df


def sim_result(sim_df, sim_degree=85):
    sim_list = []
    for i in range(len(sim_df)):
        sim_set = set()
        for j in range(i):
            if sim_df.iloc[i, j] > sim_degree:
                # 把行相似度满足要求的路径加入同行集合
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
            # 移动同组文件
            insert_dir = 'H'+str(num)  # 创建子文件名
            new_path = os.path.join(file_path, insert_dir)  # 新路径
            if not os.path.exists(new_path):  # 文件夹不存在
                os.mkdir(new_path)  # 新建文件夹
            if file_dir != new_path:
                try:
                    shutil.move(file, new_path)  # ⭐!!!移动文件
                except Exception as e:
                    print('失败：',  new_path, type(e), e)
            group_list.append((num, file, new_path))
        num += 1
    df = pd.DataFrame(group_list, columns=('分组', '文件名', '新位置'))
    df.to_excel(os.path.join(file_path, '相似文件分组hist.xlsx'))


# file_path = r'D:\File_Restore-20221006'  # 需要查找的根目录
file_path = r'C:\Users\Kevin\Pictures\Saved Pictures'  # 需要查找的根目录

img_df = get_file(file_path)
# with open(os.path.join(file_path, 'Img_hist_Data.dat'), 'rb') as f:
#     img_df = pickle.load(f)  # 读取预处理数据

sim_df = img_similarity(img_df)
# 读取之前需要还原文件位置
# with open(os.path.join(file_path, 'Img_hist_sim.dat'), 'rb') as f:
#     sim_df = pickle.load(f)  # 读取预相似度数据
#     print('Img_hist_sim.dat文件加载')
sim_df.to_excel(os.path.join(file_path, '图片相似度数据hist.xlsx'))
sim_list = sim_result(sim_df, sim_degree=85)
print('根据相似度分组完成')
file_rename_move(sim_list, file_path)
