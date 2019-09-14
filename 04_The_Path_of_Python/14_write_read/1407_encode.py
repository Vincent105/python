fn_1 = '04_The_Path_of_Python\\14_write_read\\ansi.txt'
file_obj = open(fn_1, encoding='cp950')
data = file_obj.read()
file_obj.close()

print(data)

fn_2 = '04_The_Path_of_Python\\14_write_read\\unicode.txt'
file_obj = open(fn_2, encoding='utf-8')
data = file_obj.read()
file_obj.close()

print(data)

fn_3 = '04_The_Path_of_Python\\14_write_read\\unicode.txt'
with open(fn_3, encoding='utf-8') as file_obj:
    obj_list = file_obj.readlines()
print(obj_list)    

fn_4 = '04_The_Path_of_Python\\14_write_read\\unicode.txt'
file_obj = open(fn_4, encoding='cp950')
data = file_obj.read()
file_obj.close()

print(data)
