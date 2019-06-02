def kitchen(unserved, served):
    '''unserved to served'''
    print("===處理中===")
    while unserved:
        current_meal = unserved.pop()
        print("處理中菜單:", current_meal)
        served.append(current_meal)


def show_order_meal(unserved):
    '''show_order_meal'''
    print("===以下是所點的餐點===")
    if not unserved:
        print("沒有任何尚未服務的餐點", '\n')
    for unserved_meal in unserved:
        print("所點的菜單:", unserved_meal)


def show_served_meal(served):
    '''show_order_meal'''
    print("===以下是已經服務的餐點===")
    if not served:
        print("沒有任何已經服務的餐點", '\n')
    for served_meal in served:
        print("已處理菜單:", served_meal)


order_list = ['大麥客', '雙牛堡', '麥克雞塊']
served = []
# 列出廚房處理前出餐現況
show_order_meal(order_list)
show_served_meal(served)
# 列出廚房處理中出餐現況
kitchen(order_list[:], served)
print("\n","廚房已處理完畢!!!!","\n")
# 列出廚房處理後出餐現況
show_order_meal(order_list)
show_served_meal(served)

#參數串列的預設空串列
def insertChar(letter,mylist=[]):
    mylist.append(letter)
    print(mylist)

insertChar('x')
insertChar('y')
insertChar('z')

#參數串列的預設空串列，每次重設初始值
def insertChar_2(letter,mylist=None):
    if mylist == None:
        mylist=[]        
    mylist.append(letter)
    print(mylist)

insertChar_2('x')
insertChar_2('y')
insertChar_2('z')


