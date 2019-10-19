import keras as kr
import numpy as np
import sklearn.preprocessing as pre
import mnist_fread as mread

def get_default_model():
  model = kr.models.Sequential()
  model.add(kr.layers.Dense(units=600, activation='linear', input_dim=784))
  model.add(kr.layers.Dense(units=400, activation='relu'))
  model.add(kr.layers.Dense(units=10, activation='softmax'))
  model.compile(loss=kr.losses.categorical_crossentropy, optimizer='adam',metrics=['accuracy'])
  return model
  
def load_train_data(img, lbl):
  train_img = mread.dig_images(img)
  train_lbl = mread.labels(lbl)
  train_lbl = transform_labels(train_lbl)
  return train_img, train_lbl
  
def load_test_data( img, lbl):
  test_img = mread.dig_images(img)
  test_lbl = mread.labels(lbl)
  test_lbl = transform_labels(test_lbl)
  return test_img, test_lbl
  
def transform_labels( lbls):
  encoder = pre.LabelBinarizer()
  encoder.fit(lbls)
  return encoder.transform(lbls)

def get_prediction( img):

  model = kr.models.load_model('../recognition/3.h5')
  img = ~np.asarray(img).reshape((1,784)).astype(np.uint8) / 255.0
  return np.argmax(model.predict(img))
