fn = "E:\\python\\04_The_Path_of_Python\\14_write_read\\write_test.txt"
fn1 = "E:\\python\\04_The_Path_of_Python\\14_write_read\\write_test1.txt"
string = "I lOVE pYTHON"
string1 = "I lOVE pYTHON too"
x = 100

with open(fn, 'w', encoding="utf-8") as file_obj:
    file_obj.write(string)
    print("傳回資料長度")
    print(file_obj.write(string))

with open(fn, 'a', encoding="utf-8") as file_obj:
    print("寫數值須轉為字串")
    file_obj.write(str(x))
    print(file_obj.write(str(x)))

with open(fn1, 'a', encoding="utf-8") as file_obj:
    print("多行輸出換行")
    file_obj.write(string + '\n')
    file_obj.write(string1 + '\n')


