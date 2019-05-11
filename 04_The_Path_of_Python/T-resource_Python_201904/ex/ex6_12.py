# ex6_11.py
guests = ["Mary", "Josh", "Tracy"]
print("目前宴會名單", guests)
print("1:增加名單")
print("2:刪除名單")
select = input(" = ")

name = input("請輸入名字 : ")
if select == "1":
    guests.append(name)
    print("新的宴會名單 : ", guests)
elif select == "2":
    if name in guests:
        guests.remove(name)
        print("新的宴會名單 : ", guests)
    else:
        print("名單輸入錯誤")









    
