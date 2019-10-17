# Import keras.
import keras as kr
import sklearn.preprocessing as pre
import numpy as np
from fileLoc import fLoc 
import matplotlib.pyplot as plt
import mnist_fread as mread

# Start a neural network, building it by layers.
model = kr.models.Sequential()

# Add a hidden layer with 1000 neurons and an input layer with 784.
model.add(kr.layers.Dense(units=600, activation='linear', input_dim=784))
model.add(kr.layers.Dense(units=400, activation='relu'))

# Add a three neuron output layer.
model.add(kr.layers.Dense(units=10, activation='softmax'))

# Build the graph.
model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])

train_img = mread.dig_images(fLoc[2])

train_lbs = mread.labels(fLoc[3])

inputs = train_img


encoder = pre.LabelBinarizer()
encoder.fit(train_lbs)
outputs = encoder.transform(train_lbs)

print(train_lbs[0], outputs[0])
for i in range(10):
    print(i, encoder.transform([i]))

model.fit(inputs, outputs, epochs=7, batch_size=100)

test_img = mread.dig_images(fLoc[0])
test_lbl = mread.labels(fLoc[1])

(encoder.inverse_transform(model.predict(test_img)) == test_lbl).sum()

g = model.predict(test_img[5:6])

print(g)
print(test_lbl[5]);
image = np.array(test_img[5]).reshape(28,28)
plt.imshow(image , cmap='gray')
plt.plot()
plt.show()