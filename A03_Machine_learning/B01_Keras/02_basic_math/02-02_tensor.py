import numpy as np
from keras.datasets import mnist
import matplotlib.pyplot as plt

# 0D ndim 張量                          #1D向量
x = np.array(12)
print('屬於', x.ndim, '階張量', x)

# 1D ndim 張量
x = np.array([13, 1, 3, 5, 9])  # 5D向量
print('屬於', x.ndim, '階張量', x)

# 2D ndim 張量
x = np.array([
    [13, 1, 3, 5, 9],
    [13, 1, 3, 5, 9],
    [13, 1, 3, 5, 9]])
print(x, '屬於', x.ndim, '階張量')

# 3D ndim 張量
x = np.array(

    [[[13, 1, 3, 5, 9],
      [13, 1, 3, 5, 9],
      [13, 1, 3, 5, 9]],
     [[13, 1, 3, 5, 9],
      [13, 1, 3, 5, 9],
      [13, 1, 3, 5, 9]],
     [[13, 1, 3, 5, 9],
      [13, 1, 3, 5, 9],
      [13, 1, 3, 5, 9]]
     ])
print(x, '屬於', x.ndim, '階張量')

(train_imgs, train_labels), (test_imgs, test_labels) = mnist.load_data()
print('屬於', train_imgs.ndim, '階張量')
print('形狀', train_imgs.shape)
print('類型', train_imgs.dtype)
print('8位元整數的3階張量')

# 顯示第四個資料
digits = train_imgs[4]
plt.imshow(digits, cmap=plt.cm.binary)
plt.show()

# 張量切片運算
my_slice = train_imgs[10:100]
print(my_slice.shape)

my_slice = train_imgs[10:100, :, :]
print(my_slice.shape)

my_slice = train_imgs[10:100, 0:28, 0:28] #選出像素28 x 28
print(my_slice.shape)

my_slice = train_imgs[10:100, 0:14, 0:14] #選出像素14 x 14
print(my_slice.shape)

my_slice = train_imgs[10:100, 7:-7, 7:-7] #選出像素14 x 14
print(my_slice.shape)


# print('形狀', train_imgs[4])

batch = train_imgs[:128]