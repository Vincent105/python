import copy

def getstring(list2):
    list1 = copy.copy(list2)
    list1.insert(-1,'and')
    last1 = list1.pop()
    last2 = list1.pop()
    last12 = last2 + ' ' + last1
    spam = list1[0]               #先取出Index第一位

    j = 1
    
    for i in range(len(list1)):
        spam = spam + ',' + list1[j]
        j = j + 1              
        if j == len(list1):
            break
    print(spam + ',' + last12)

spam = ['apple','bananas','tofu','cats','grape']

getstring(spam)

def grid1(list1):
    for i in range(len(list1[0])):
        for j in range(len(list1)):
            print(list1[j][i],end=' ')
            if j ==len(list1)-1:
                print('\n')

grid = [ ['.', '.', '.', '.', '.','.'],
         ['.', '0', '0', '.', '.','.'],
         ['0', '0', '0', '0', '.','.'],
         ['0', '0', '0', '0', '0','.'],
         ['.', '0', '0', '0', '0','0'],
         ['0', '0', '0', '0', '0','.'],
         ['0', '0', '0', '0', '.','.'],
         ['.', '0', '0', '.', '.','.'],
         ['.', '.', '.', '.', '.','.']]
 