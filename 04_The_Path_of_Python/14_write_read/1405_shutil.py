import shutil
import send2trash

shutil.copy("04_The_Path_of_Python\\14_write_read\\atq9305.jpg",
            "04_The_Path_of_Python\\14_write_read\\atq93052.jpg")

shutil.copytree("04_The_Path_of_Python\\14_write_read",
                "04_The_Path_of_Python\\141_write_read")

print("移動目錄 或者 檔案更名")
shutil.move("04_The_Path_of_Python\\141_write_read",
            "04_The_Path_of_Python\\14_write_read")

send2trash.send2trash(
    "04_The_Path_of_Python\\14_write_read\\141_write_read\\1401_file.py")

print("刪除目錄")
shutil.rmtree("04_The_Path_of_Python\\14_write_read\\141_write_read")
