import keras
from tensorflow.python.keras import layers
from tensorflow.python.framework import ops


keras.layers.Dense(512, activation='relu')


def native_relu(x):
    assert len(x.shape) == 2
    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i, j], 0)
    return x            

from keras import layers
from keras import models

layers = layers.Dense(32, input_shape=(784,))

model = model.Sequential()
model.add(layers.Dense(32, input_shape=(784,)))
model.add(layers.Dense(32))