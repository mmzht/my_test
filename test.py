
import pickle
import json

temp_data = r'C:\Users\Kevin\Documents\test.data'
data_1 = [1, 3, 6, 9, 'end']
# pickle可以读写所有格式数据
with open(temp_data, 'wb') as f:  # 二进制写入变量
    pickle.dump(data_1, f)  # 变量写入temp_data文件中
with open(temp_data, 'rb') as f:  # 二进制读取变量
    read_list = pickle.load(f)
print('读取数据的类型：', type(read_list))

