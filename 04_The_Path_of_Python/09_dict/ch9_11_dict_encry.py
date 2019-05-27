abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(subText,abc))
print(encry_dict)

msgTest = 'python'
cipher = []
for i in msgTest:
    v = encry_dict[i]
    cipher.append(v)
cipherText = ''.join(cipher)

print('原始 :',msgTest)
print('加密 :',cipherText)