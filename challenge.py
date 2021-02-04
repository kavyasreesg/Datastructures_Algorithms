# list1 = [1, 2, 0, 3, 0, 4]
list1 = [2, 0, 0, 1, 0]
new_list = []
count_1 = list1.count(0)
count_2 = 0
for ele in list1:
    if ele > 0:
        new_list.append(ele)
        count_2 += 1

j = 0
if count_1 > count_2:
    while count_1 != j:
        new_list.insert(count_1, 0)
        j = j + 1
else:
    new_list[count_2:] = count_1 * [0]

print(new_list)
