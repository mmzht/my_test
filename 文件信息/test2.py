import cv2
import os
import pickle
import pandas as pd
import numpy as np

file_path = r'C:\Users\Kevin\Pictures\Saved Pictures\test'  # 需要查找的根目录
file_dir = os.path.split(file_path)[0]
new_path = os.path.join(file_dir, str(12))  # 新路径

if not os.path.exists(new_path):
    os.mkdir(new_path)
    print('创建目录')
# shutil.move(file, new_path)
print(new_path)