"""Module defining basic interface for recognition functionality using Keras NN.
      
Web application uses this module for its purpose.
"""
from __future__ import print_function
import keras as kr
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import recognition.fileLoc as loc
import recognition.mnist_fread as mread
import matplotlib.pyplot as plt

batch_size = 128
num_classes = 10
epochs = 6
img_rows, img_cols = 28, 28
input_shape = (img_rows, img_cols, 1)

def get_default_model():
  """Compile default Keras model.

  Convolutional Keras model adopted from https://keras.io/examples/mnist_cnn/
  
  Returns:
    keras model: compiled default keras model.

  """
  model = Sequential()
  model.add(Conv2D(32, kernel_size=(3, 3),
                  activation='relu',
                  input_shape=input_shape))
  model.add(Conv2D(64, (3, 3), activation='relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.25))
  model.add(Flatten())
  model.add(Dense(128, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(num_classes, activation='softmax'))

  model.compile(loss=kr.losses.categorical_crossentropy,
                optimizer=kr.optimizers.Adadelta(),
                metrics=['accuracy'])
  return model

def get_model(location = 'recognition/cnn99.h5'):
  model = kr.models.load_model(location)
  return model

def load_train_data(img, lbl):
  """Load training images and labels.
  
  Params:
     img: path to training images
     lbl: path to labels
  Returns:
     images, labels: a tuple of images and labels in a format which is ready for feeding to NN.
  """
  train_img = mread.dig_images(img)
  train_lbl = mread.labels(lbl)
  train_lbl =  kr.utils.to_categorical(train_lbl, num_classes)
  return train_img, train_lbl
  
def load_test_data( img, lbl):
  """Load test images and labels.
  
  Params:
     img: path to test images
     lbl: path to test labels
  Returns:
     images, labels: a tuple of images and labels in a format which is ready for feeding to NN.
  """
  test_img = mread.dig_images(img)
  test_lbl = mread.labels(lbl)
  test_lbl = kr.utils.to_categorical(test_lbl, num_classes)
  return test_img, test_lbl
  
def train_model(model = get_default_model()):
  """Train default or provided as function parameter model.

  Function takes compiled keras model as parameter(or loads default). 
  Loads MNIST training/testing data and trains model.
  Returns trained model.

  Params:
    model: a compiled Keras model(or default if none provided)

  Returns:
    model: model trained against MNIST collection

  """ 
  train_img, train_lbl = load_train_data(loc['train_img'], loc['train_lbl'])
  test_img, test_lbl = load_test_data(loc['test_img'], loc['test_lbl'])
  
  model.fit(train_img, train_lbl,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(test_img, test_lbl))
  score = model.evaluate(test_img, test_lbl, verbose=0)

  print('Test loss:', score[0])
  print('Test accuracy:', score[1])
  return model
