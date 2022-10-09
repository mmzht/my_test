import requests
import exifread
import piexif
import os
import pandas as pd
import time
from PIL import Image


class GetPhotoInfo():
    def __init__(self, photo):
        self.photo = photo
        # 百度地图ak  请替换为自己申请的ak
        self.ak = 'nYPs4LQ9a4VhVxj55AD69K6zgsRy9o4z'
        self.location = self.get_photo_info()
        # self.location = self.get_photo_exif()

    def get_photo_info(self):
        with open(self.photo, 'rb') as f:
            tags = exifread.process_file(f)
        try:
            # 打印照片其中一些信息
            print('拍摄时间：', tags['EXIF DateTimeOriginal'])
            print('照相机制造商：', tags['Image Make'])
            print('照相机型号：', tags['Image Model'])
            print('照片尺寸：', tags['EXIF ExifImageWidth'],
                  tags['EXIF ExifImageLength'])
            # 纬度
            lat_ref = tags["GPS GPSLatitudeRef"].printable
            lat = tags["GPS GPSLatitude"].printable[1:-
                                                    1].replace(" ", "").replace("/", ",").split(",")
            lat = float(lat[0]) + float(lat[1]) / 60 + \
                float(lat[2]) / float(lat[3]) / 3600
            if lat_ref != "N":
                lat = lat * (-1)
            # 经度
            lon_ref = tags["GPS GPSLongitudeRef"].printable
            lon = tags["GPS GPSLongitude"].printable[1:-
                                                     1].replace(" ", "").replace("/", ",").split(",")
            lon = float(lon[0]) + float(lon[1]) / 60 + \
                float(lon[2]) / float(lon[3]) / 3600
            if lon_ref != "E":
                lon = lon * (-1)
            print("经纬度：", lat, lon)
            return lat, lon
        except Exception as e:
            print(e, "ERROR:请确保照片包含经纬度等EXIF信息。")
            return None

    # def get_photo_exif(self):
    #     exif_label = ['EXIF DateTimeOriginal',  # '拍摄时间：'
    #                   'Image Make',  # '照相机制造商：'
    #                   'Image Model',  # '照相机型号：'
    #                   'EXIF ExifImageWidth',  # '照片宽：'
    #                   'EXIF ExifImageLength'  # '照片长：'
    #                   ]
    #     exif = {}
    #     with open(self.photo, 'rb') as f:
    #         tags = exifread.process_file(f)
    #     for item in exif_label:
    #         try:
    #             exif[item] = tags[item]
    #         except KeyError:
    #             exif[item] = None
    #     # print(exif)
    #     return exif

    def get_location(self):
        if self.location == None:
            return '照片无经纬度信息'
        url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak={}&output=json' \
              '&coordtype=wgs84ll&location={},{}'.format(
                  self.ak, *self.location)
        response = requests.get(url).json()
        status = response['status']
        if status == 0:
            address = response['result']['formatted_address']
            print('地址：', address)
            return address
        else:
            # print('baidu_map error')
            return 'baidu_map error'


def Time_localtime(timestamp):  # 日期格式转换
    stime = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', stime)


def Get_CreatTime(fpath):  # 获取文件创建时间
    t = os.path.getctime(fpath)
    return Time_localtime(t)


def Get_ModifyTime(fpath):  # 获取文件修改时间
    t = os.path.getmtime(fpath)
    return Time_localtime(t)


def get_exif(file_name, exif_label):
    # exif_label = ['Image DateTime',
    #               'EXIF ExifImageLength', 'EXIF ExifImageWidth',
    #               'Image Make', 'Image Model']
    with open(file_name, 'rb') as f:
        try:
            tags = exifread.process_file(f)
            exif_info = tags[exif_label]
        except Exception as e:
            exif_info = None
    return exif_info


def get_file_info(file_path):
    exif_label = ['Image DateTime', 'Image Make',
                  'Image Model', 'Length', 'Width']
    #   'EXIF ExifImageLength', 'EXIF ExifImageWidth',  # 长度，宽度
    info = ['文件创建时间', '文件修改时间', '文件大小', '文件名', '位置']
    columns = exif_label + info
    df = pd.DataFrame(columns=columns)  # 信息表头
    for roots, dirs, file_names in os.walk(file_path):
        for name in file_names:
            file_path_name = os.path.join(roots, name)  # 含路径的文件名
            file_suf = os.path.splitext(name)[1]  # 文件后缀
            file_size = os.path.getsize(file_path_name)/1024/1024
            CreatTime = Get_CreatTime(file_path_name)
            ModifyTime = Get_ModifyTime(file_path_name)
            if file_suf.lower() == '.jpg':
                DateTime = get_exif(file_path_name, exif_label[0])
                ImageMake = get_exif(file_path_name, exif_label[1])
                ImageModel = get_exif(file_path_name, exif_label[2])

                image = Image.open(file_path_name)
                Length = image.size[0]
                Width = image.size[1]
                location = GetPhotoInfo(file_path_name).get_location()
                df.loc[len(df)] = DateTime,  ImageMake, ImageModel, Length, Width,\
                    CreatTime, ModifyTime, file_size, name, location
    return df


# img = Image.open(file_path)
# exif_dict = piexif.load(img.info['exif'])
# #Exif   0th  Exif  GPS
# for K,V in exif_dict['Exif'].items():
#     print(K,'=',V)

if __name__ == '__main__':
    #     file_path = r'C:\Users\Kevin\Pictures\Saved Pictures\IMG_20211127_150131.JPG'  # 需要查找的根目录
    #     Main = GetPhotoInfo(file_path)
    #     Main.get_location()

    # file_path = r'C:\Users\Kevin\Pictures\Saved Pictures'  # 需要查找的根目录
    file_path = r'D:\mate20 2019-2022\mate20照片\Camera-2022'  # 需要查找的根目录
    save_path = r'C:\Users\Kevin\Documents\照片文件信息.xlsx'  # 结果保存

    df = get_file_info(file_path)
    df.to_excel(save_path)
