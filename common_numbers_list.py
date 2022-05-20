import pandas

with open("txt1") as file:
    data = file.readlines()
    # print(data)
with open("txt2") as file2:
    data2 = file2.readlines()
    # print(data2)

list_1 = [n for n in data if n != '\n']
res_new_list1 = list(map(int, list_1))
print(res_new_list1)

list_2 = [n2 for n2 in data2 if n2 != '\n']
res_new_list2 = list(map(int, list_2))
print(res_new_list2)

common_list = list(dict.fromkeys([x for x in list_1 if x in list_2]))
final_common_list = list(map(int, common_list))
print(final_common_list)

# Doctor Angela Code For Doing This Task
# with open("file1.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
# result = [int(num) for num in list1 if num in list2]
# print(result)
