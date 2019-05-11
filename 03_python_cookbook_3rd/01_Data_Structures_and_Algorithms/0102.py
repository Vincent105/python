#Case 1 
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, mail, *phone_numbers = record
print(name)
print(phone_numbers)                #解壓出的*變量永遠都是列表類型，不管解壓的電話號碼數量是多少（包括 0 個）。



