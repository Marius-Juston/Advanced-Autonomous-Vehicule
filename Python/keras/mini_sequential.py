import pickle

import numpy as np
# Load pickled data
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Flatten, Dense

with open('small_train_traffic.p', mode='rb') as f:
    data = pickle.load(f)

# split data
X_train, y_train = data['features'], data['labels']

model = Sequential()
model.add(Flatten(input_shape=(32, 32, 3)))
model.add(Dense(128, activation='relu'))
model.add(Dense(5, activation='softmax'))

# preprocess data
X_normalized = np.array(X_train / 255.0 - 0.5)

from sklearn.preprocessing import LabelBinarizer

label_binarizer = LabelBinarizer()
y_one_hot = label_binarizer.fit_transform(y_train)

model.compile('adam', 'categorical_crossentropy', ['accuracy'])
history = model.fit(X_normalized, y_one_hot, epochs=3, validation_split=0.2)
