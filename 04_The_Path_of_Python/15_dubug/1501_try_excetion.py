import traceback

# Case 1
def division(x, y):
    try:
        ans = x / y
    except ZeroDivisionError as e:
        errlog = open('04_The_Path_of_Python\\15_dubug\\log2.txt','a')
        errlog.write(traceback.format_exc())
        errlog.close()
        print('除數不可為0 ', e)
    except TypeError as e:
        errlog = open('04_The_Path_of_Python\\15_dubug\\log2.txt','a')
        errlog.write(traceback.format_exc())
        errlog.close()        
        print('資料型別錯誤', e)
    except:
        print('...')        
    else:
        return ans
    finally:
        print('程式執行完成\n')        

print(division(10, 2))
print(division('a', 'b'))
print(division(0, 0))
print(division(5, 2))

# Case 2
fn = 'unicode.txt'
try:
    with open(fn, encoding='utf-8') as obj:
        data = obj.read()
except FileNotFoundError:
    print('File %s Not Found.' % fn)
else:
    print(data)
