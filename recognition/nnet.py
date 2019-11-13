"""Module defining basic interface for recogintion functionality using Keras NN.
      
Web application uses this module for its purpose.
"""
import keras as kr
import numpy as np
import sklearn.preprocessing as pre
import recognition.fileLoc as floc
import recognition.mnist_fread as mread

def get_default_model():
  """Compile basic Keras model.

  Default structure of model is 3 layers with 1000 hidden units.
  Returns:
    keras model: compiled default keras model.

  """
  model = kr.models.Sequential()
  model.add(kr.layers.Dense(units=600, activation='linear', input_dim=784))
  model.add(kr.layers.Dense(units=400, activation='relu'))
  model.add(kr.layers.Dense(units=10, activation='softmax'))
  model.compile(loss=kr.losses.categorical_crossentropy, optimizer='adam',metrics=['accuracy'])
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
  train_lbl = transform_labels(train_lbl)
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
  test_lbl = transform_labels(test_lbl)
  return test_img, test_lbl
  

def transform_labels( lbls):
  """Transform label data to a binary format needed for multi-class NN."""
  encoder = pre.LabelBinarizer()
  encoder.fit(lbls)
  return encoder.transform(lbls)


def get_prediction( img):
  """Get predicted value of provided image.
  
  Loading pre-trained keras model to feed provided image and get result.
  Input image array is converted to suitable structure and fed to NN.
  
  Params:
    img: a 28x28 image array.
  Returns:
    prediction: a most probable number.
    
  """
  model = kr.models.load_model('recognition/acc99.h5', None, True)
  img = ~np.asarray(img).reshape((1,784)).astype(np.uint8) / 255.0
  return np.argmax(model.predict(img))
