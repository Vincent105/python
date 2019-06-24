# 載入IMDB資料集
from keras.datasets import imdb
import numpy as np

(train_data, train_labels), (test_data,
                             test_labels) = imdb.load_data(num_words=10000)
# print(train_data[0])
# print(train_labels[0])
# print(max([max(sequence) for sequence in train_data]))

word_index = imdb.get_word_index()
reverse_word_index = dict([(value, key)
                           for (key, value) in word_index.items()])
decoded_review = ' '.join(reverse_word_index.get(i-3, '?')
                          for i in train_data[0])
# print(decoded_review)

# 將二層的整數List編碼成二元矩陣
def vectorize_sequence(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequences in enumerate(sequences):
        results[i, sequences] = 1.
    return results

x_train = vectorize_sequence(train_data)
x_test = vectorize_sequence(test_data)

# print(x_train[0])

y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(train_labels).astype('float32')