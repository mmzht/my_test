from skimage.metrics import structural_similarity
import cv2


def calculate(image1, image2):  # 直方图比较图片单通道相似度
    # 灰度直方图算法
    # 计算单通道的直方图的相似值
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
img2 = cv2.imread(r'C:\Users\Kevin\Pictures\Saved Pictures\5.JPG')
# sim_score = classify_hist_with_split(image1, image2)
# print(sim_score)


# SSIM（结构相似度度量)是一种全参考的图像质量评价指标，
# 分别从亮度、对比度、结构三个方面度量图像相似性。SSIM取值范围[0, 1]，值越大，表示图像失真越小。
if img1.shape[0] < img2.shape[0] or img1.shape[1] < img2.shape[1]:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
else:
    img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
# ssim_score = structural_similarity(img1, img2, data_range=255, multichannel=True)
ssim_score = structural_similarity(img1, img2, data_range=255, channel_axis=2)
print(ssim_score)
