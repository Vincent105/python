fn = '04_The_Path_of_Python\\14_write_read\\ch14_15.txt'
try:
    with open(fn, encoding='utf-8') as file_obj:
        data = file_obj.read()
except FileNotFoundError:
    print('找不到所需要的檔案')        
else:
    wordlist = data.split()    
    print(wordlist)
    print(fn,'文章字數是',len(wordlist))    

def wordsSum(fn):
    """設計一個計算字數的函式，適合使用在英文文章當中，中文文章不適合"""
    try:
        with open(fn, encoding='utf-8') as file_obj:
            data = file_obj.read()
    except FileNotFoundError:
        print('找不到所需要的檔案')        
    else:
        wordlist = data.split()    
        print(wordlist)
        print(fn,'文章字數是',len(wordlist))        

wordsSum('04_The_Path_of_Python\\14_write_read\\ch14_15.txt')
wordsSum('04_The_Path_of_Python\\14_write_read\\unicode.txt')

files = ['04_The_Path_of_Python\\14_write_read\\ch14_15.txt','04_The_Path_of_Python\\14_write_read\\unicode.txt']
for file in files:
    wordsSum(file)