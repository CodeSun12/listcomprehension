
name = "shakeeb"
students_name = ["Shakeeb", "Hassan", "Zain", "Mahad"]
students_name.append("dskfaj")


name_list = [new for new in name]
print(name_list)

new_students_name_list = [namelist.upper() for namelist in students_name if len(namelist) < 5]
print(new_students_name_list)


num_list = [num * 2 for num in range(1,5)]
print(num_list)