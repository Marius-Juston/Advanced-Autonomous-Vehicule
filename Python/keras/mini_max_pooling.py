import pickle

import numpy as np
# Load pickled data
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Conv2D, Flatten, Dense, MaxPooling2D

with open('small_train_traffic.p', mode='rb') as f:
    data = pickle.load(f)

# split data
X_train, y_train = data['features'], data['labels']

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(5, activation='softmax'))

# Preprocess data
X_normalized = np.array(X_train / 255.0 - 0.5)

from sklearn.preprocessing import LabelBinarizer

label_binarizer = LabelBinarizer()
y_one_hot = label_binarizer.fit_transform(y_train)

# compile and train model
# Training for 3 epochs should result in > 50% accuracy
model.compile('adam', 'categorical_crossentropy', ['accuracy'])
history = model.fit(X_normalized, y_one_hot, epochs=3, validation_split=0.2)
