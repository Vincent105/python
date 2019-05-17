msg1 = "人機對話測試"
msg2 = '輸入q可以退出'
msg = msg1 + '\n' + msg2 + '\n'
   
input_msg =''     
while input_msg !='q':
    input_msg = input(msg)
    if input_msg != 'q':
        print(input_msg)
