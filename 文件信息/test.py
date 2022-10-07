
from cProfile import label


sim_list = [{1, 2, 3}, {4, 5, 6}, {7, 8}, {
    3, 11, 13}, {15, 16}, {7, 19}, {20, 1, 2, 3}]

for m in range(len(sim_list)):  # 取列表中的一个集合；
    for n in range(len(sim_list)):
        if sim_list[m] & sim_list[n]:  # 如何两个集合有交集
            sim_list[n] = sim_list[m] | sim_list[n]  # 则等于并集
temp = []
for item in sim_list:  # 去掉重复元素
    if item not in temp:
        temp.append(item)
sim_list = temp

print(sim_list)
