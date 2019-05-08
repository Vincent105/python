title = 'Alice in Wonderland'
titles = title.split()
print(titles)
print(len(titles))

#編寫計算字數的變數
def countword(filename):   
    '''計算一個文件檔包含多少單字''' 
    try:
        with open(filename) as fileobject:
            contents = fileobject.read()
    except FileNotFoundError:
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
        pass                    #若有錯誤訊息時，進行pass
    else:
        words = contents.split()
        num_words = len(words)
        print("This file has " + str(num_words) + ' words.')

filenames = ['01_Python_Crash_Course\\1001_file_exception\\Alice in Wonderland.txt',
            '01_Python_Crash_Course\\1001_file_exception\\pi_digits.txt',
            'pi_digits.txt'                
        ]

for filename in filenames:
    countword(filename)

