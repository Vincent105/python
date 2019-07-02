src = 'E:\\python\\04_The_Path_of_Python\\14_write_read\\atq9305.jpg'
dst = 'E:\\python\\04_The_Path_of_Python\\14_write_read\\atq9305_1.jpg'

with open(src, 'rb') as file_rd:
    temp = file_rd.read()
    with open(dst, 'wb') as file_wr:
        file_wr.write(temp)
