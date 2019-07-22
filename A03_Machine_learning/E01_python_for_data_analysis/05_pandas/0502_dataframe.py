import pandas as pd
import numpy as np

# 直接传入一个由等长列表或NumPy数组组成的字典：
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)

print("取頭前五筆資料")
print(frame.head())

print("調整列排列順序")
frame_1 = pd.DataFrame(data, columns=['year', 'state', 'pop'])
print(frame_1)

print("列缺值將在結果產生缺少值NaN")
frame_2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=[
                       'one', 'two', 'three', 'four', 'five', 'six'])
print(frame_2)

print("通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series：")
print(frame_2['state'])
print(frame_2.year)

print("行也可以通过位置或名称的方式进行获取，比如用loc属性")
print(frame_2.loc['three'])


print("列可以通过赋值的方式进行修改。例如，我们可以给那个空的'debt'列赋上一个标量值或一组值：")
frame_2['debt'] = 16.5
print(frame_2)
frame_2['debt'] = np.arange(6.)
print(frame_2)

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])

frame_2['debt'] = val
print(frame_2)

frame_2['eastern'] = frame_2.state == 'Ohio'
print(frame_2)

print("透過del進行列刪除")
del frame_2['eastern']
print(frame_2)
print('列出欄位Index', frame_2.columns)

print("套字典传给DataFrame，pandas就会被解释为：外层字典的键作为列，内层键则作为行索引：")
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame_3 = pd.DataFrame(pop)
print(frame_3)

print("你也可以使用类似NumPy数组的方法，对DataFrame进行转置（交换行和列）：")
print(frame_3.T)

print("内层字典的键会被合并、排序以形成最终的索引。如果明确指定了索引，则不会这样：")
print(pd.DataFrame(pop, index=[2001, 2002, 2003]))

print("由Series组成字典的用法：")
pdata = {'Ohio': frame_3['Ohio'][:-1],
         'Nevada': frame_3['Nevada'][:2]}

print(pd.DataFrame(pdata))

print("可針對dataframe的index以及columns設定name屬性")
frame_3.index.name = 'year'; frame_3.columns.name = 'state'
print(frame_3)

print("values屬性將以二緯ndarray形式返回dataframe數據")
print(frame_3.values)
print(frame_2.values)
