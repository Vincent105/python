names = ['Vincent','Esther','John']
print("I can invite " + names[0] + "," + names [1] + " and " + names[2] + " to my party.")
print(names[2] + " will not attand the party today.") 

#修改,替换
names[2] = "Scott"
print("I can invite " + names[0] + "," + names [1] + " and " + names[2] + " to my party.")

#新增
names.insert(1,"Luke")	
names.insert(3,"Allen")
names.append("Kevin")
print("I can invite " + names[0] + "," + names [1] + " and " + names[2] + " and " +
names[3] + "," + names [4] + " and " + names[5] + " to my party.")

#縮減
del_1 = names.pop()
print("Sorry for " + del_1.title() + ",I can't invite you to the party.")
del_2 = names.pop()
print("Sorry for " + del_2.title() + ",I can't invite you to the party.")
del_3 = names.pop()
print("Sorry for " + del_3.title() + ",I can't invite you to the party.")
del_4 = names.pop()
print("Sorry for " + del_4.title() + ",I can't invite you to the party.")
print("You still in the party," + names[0] + ".")
print("You still in the party," + names[1] + ".")
del names[1]
del names[0]
print(names)
