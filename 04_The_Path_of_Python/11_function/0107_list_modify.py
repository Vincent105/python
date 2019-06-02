def kitchen(unserved, served):
    '''unserved to served'''
    print("===處理中===")
    while unserved:
        current_meal = unserved.pop()
        print("處理中菜單:", current_meal)
        served.append(current_meal)


def show_unserved_meal(unserved):
    '''show_unserved_meal'''
    print("===以下是尚未服務的餐點===")
    if not unserved:
        print("沒有任何尚未服務的餐點", '\n')
    for unserved_meal in unserved:
        print("未處理菜單:", unserved_meal)


def show_served_meal(served):
    '''show_unserved_meal'''
    print("===以下是已經服務的餐點===")
    if not served:
        print("沒有任何已經服務的餐點", '\n')
    for served_meal in served:
        print("已處理菜單:", served_meal)


unserved = ['大麥客', '雙牛堡', '麥克雞塊']
served = []
# 列出廚房處理前出餐現況
show_unserved_meal(unserved)
show_served_meal(served)
# 列出廚房處理中出餐現況
kitchen(unserved, served)
print("\n","廚房已處理完畢!!!!","\n")
# 列出廚房處理後出餐現況
show_unserved_meal(unserved)
show_served_meal(served)
