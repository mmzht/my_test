import cv2
import os
import pandas as pd
import numpy as np

# def calculate(image1, image2):  # 直方图比较图片单通道相似度
#     # 灰度直方图算法, 计算单通道的直方图的相似值
#     hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
#     hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
#     # 计算直方图的重合度
#     degree = 0
#     for i in range(len(hist1)):
#         if hist1[i] != hist2[i]:
#             degree += (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
#         else:
#             degree += 1
#     return degree / len(hist1)


# def hist_similarity_2(image1, image2, size=(256, 256)):
#     # RGB每个通道的直方图相似度
#     # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
#     # image1 = cv2.resize(image1, size)
#     # image2 = cv2.resize(image2, size)
#     sub_image1 = cv2.split(image1)
#     sub_image2 = cv2.split(image2)
#     sub_data = 0
#     for im1, im2 in zip(sub_image1, sub_image2):
#         sub_data += calculate(im1, im2)
#     sub_data = sub_data / 3
#     return sub_data


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


def get_file_info(file_path):
    file_list = []
    df = pd.DataFrame(columns=('长文件名', '文件名', '后缀', '大小'))  # 信息表头
    for roots, dirs, file_names in os.walk(file_path):
        for name in file_names:
            file_path_name = os.path.join(roots, name)  # 含路径的文件名
            file_suf = os.path.splitext(name)[1]  # 文件后缀
            file_size = os.path.getsize(file_path_name)
            if file_suf.lower() == '.jpg':
                df.loc[len(df)] = file_path_name, name, file_suf, file_size
                file_list.append(file_path_name)
    # df['重复文件']=df.duplicated(subset='大小', keep=False)
    df.to_excel(os.path.join(file_path, '所有文件信息.xlsx'))
    return file_list


def img_similarity(file_path):  # file_list文件路径列表
    file_list = get_file_info(file_path)
    file_num = len(file_list)
    df = pd.DataFrame(index=file_list, columns=file_list)
    for i in range(file_num):
        img_i = cv2.imread(file_list[i])  # 中文会报错
        # 缩放到长边256
        height = img_i.shape[0]
        width = img_i.shape[1]
        if height < width:
            size = (256, int(height/width*256))
        else:
            size = (int(width/height*256), 256)

        img_1 = cv2.resize(img_i, size)
        for j in range(i):
            img_j = cv2.imread(file_list[j])
            if img_i.shape == img_j.shape:
                img_2 = cv2.resize(img_j, size)
                df.iloc[i, j] = hist_similarity(img_1, img_2)
            # 进度条
            print('\r', end='')
            bar = int((i*i/2+j+1)/(file_num*file_num/2)*100)
            print(bar, "%", '■'*bar, end="")
    df.to_excel(os.path.join(file_path, '图片相似度.xlsx'))
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


def sim_file_rename(file_path):
    sim_files_list = sim_result(file_path)
    num = 1
    rename_list = []
    for sim_files in sim_files_list:
        for file in sim_files:
            file_dir = os.path.split(file)[0]  # 文件dir
            file_name = os.path.split(file)[1]  # 文件名
            name_left = os.path.splitext(file_name)[0]  # 不含后缀的文件名
            name_right = os.path.splitext(file_name)[1]  # 文件后缀
            insert_srt = 'SIM'+str(num)+'--'  # 插入的字符
            new_file_name = insert_srt + name_left[:] + name_right  # 文件名加减字符
            new_file_path = os.path.join(file_dir, new_file_name)
            # os.rename(file, new_file_path)  # ⭐!!!重命名文件
            rename_list.append((file, new_file_path))
            print(file_name, new_file_name)
        num += 1
    df = pd.DataFrame(rename_list, columns=('旧文件名', '新文件名'))
    df.to_excel(os.path.join(file_path, '图片重命名.xlsx'))


file_path = r'C:\Users\Kevin\Pictures\Saved Pictures'  # 需要查找的根目录
sim_file_rename(file_path)
