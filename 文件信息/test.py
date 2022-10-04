from skimage.metrics import structural_similarity
import cv2
import os
import pandas as pd


def calculate(image1, image2):  # 直方图比较图片单通道相似度
    # 灰度直方图算法, 计算单通道的直方图的相似值
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + \
                (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


def classify_hist_with_split(image1, image2, size=(256, 256)):
    # RGB每个通道的直方图相似度
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data


img1 = cv2.imread(r'C:\Users\Kevin\Pictures\Saved Pictures\1.JPG')
img2 = cv2.imread(r'C:\Users\Kevin\Pictures\Saved Pictures\2.JPG')
# sim_score = classify_hist_with_split(img1, img2)

# SSIM（结构相似度度量)是一种全参考的图像质量评价指标，
# 分别从亮度、对比度、结构三个方面度量图像相似性。SSIM取值范围[0, 1]，值越大，表示图像失真越小。
# img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
# ssim_score = structural_similarity(img1, img2, data_range=255, channel_axis=2)


# 比较照片，如果相似度大于0.8则保留文件名和相似值
def get_file_info(file_path):
    file_list = []
    df = pd.DataFrame(columns=('长文件名', '文件名', '后缀', '大小'))  # 信息表头
    for roots, dirs, file_names in os.walk(file_path):
        for name in file_names:
            file_name = os.path.join(roots, name)  # 含路径的文件名
            file_suf = os.path.splitext(name)[1]  # 文件后缀
            file_size = os.path.getsize(file_name)
            if file_suf.lower() == '.jpg':
                df.loc[len(df)] = file_name, name, file_suf, file_size
                file_list.append(file_name)
    # df['重复文件']=df.duplicated(subset='MD5', keep=False)
    df.to_excel(os.path.join(file_path, '所有文件信息.xlsx'))
    return file_list


file_path = r'C:\Users\Kevin\Pictures\Saved Pictures'  # 需要查找的根目录
file_list = get_file_info(file_path)


def pre_read_img(img_path, img_base):  # img_base提前读取好，减少反复，提升速度
    if os.path.splitext(img_path)[1].lower() == '.jpg':  # 兼容大小写
        img = cv2.imread(r'C:\Users\Kevin\Pictures\Saved Pictures\1.JPG')  # 读取
        img = cv2.resize(img, (img_base.shape[1], img_base.shape[0]))  # 调整大小
        return img
