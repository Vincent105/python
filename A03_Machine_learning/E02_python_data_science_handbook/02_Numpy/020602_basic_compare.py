import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x < 3, np.less(x, 3))
print(x > 3, np.greater(x, 3))
print(x <= 3, np.less_equal(x, 3))
print(x >= 3, np.greater_equal(x, 3))
print(x != 3, np.not_equal(x, 3))
print(x == 3, np.equal(x, 3))
z = (2 * x) == (x ** 2)
print(z)

print('RandomState固定穩定產生隨機array ')
rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
print(x)
print(x > 6)
print(np.greater(x, 6))

print('統計紀錄的個數')
print(x)
print('有多少值小於6?=', np.count_nonzero(x < 6))
print('有多少值小於6?=', np.sum(x < 6),'(False会被解释成 0， True 会被解释成1：)')
print('有多少值小於6?=', np.sum(x < 6,axis=0),'行統計')
print('有多少值小於6?=', np.sum(x < 6,axis=1),'列統計')

