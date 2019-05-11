# ex25_7.py
import pandas as pd
import matplotlib.pyplot as plt

colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv('iris.csv', names = colName)

# 擷取不同品種的鳶尾花
iris_setosa = iris[iris['species'] == 'Iris-setosa']
iris_versicolor = iris[iris['species'] == 'Iris-versicolor']
iris_virginica = iris[iris['species'] == 'Iris-virginica']
# 繪製散點圖
plt.plot(iris_setosa['petal_len'],iris_setosa['petal_wd'],
         '*',color='g',label='setosa')
plt.plot(iris_versicolor['petal_len'],iris_versicolor['petal_wd'],
         'x',color='b',label='versicolor')
plt.plot(iris_virginica['petal_len'],iris_virginica['petal_wd'],
         '.',color='r',label='virginica')
# 標註軸和標題
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Iris Petal length and width anslysis')
plt.legend()
plt.show()











