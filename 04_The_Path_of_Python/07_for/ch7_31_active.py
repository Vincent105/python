msg1 = "人機對話測試"
msg2 = "輸入q退出測試"
msg = msg1 + ' ' + msg2

active = True
while active:
    input_msg = input(msg)
    if input_msg != 'q':
        print(input_msg)        
    else:
        active = False

