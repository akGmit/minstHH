#!/usr/bin/python3
"""Here are function definitions to read MNIST files to memory.
    These functions use ctypes module functionality and calls foreign C functions.
    Using stdio C  library significantly increased efficiancy of reading and processing data files."""
import numpy as np
import cfunc as cfunc

"""Reading to MNIST train and test binnart image files.
    Function takes file path as parameter, gets a pointer to file using C fopen() function.
    Reads binary data file in one go to memory and then calls another custom C function to process raw data into 60000by28by28 array.
    Returns 60000by784 array ready for feeding to NN."""
def dig_images(filepath):
  fptr = cfunc.fopen(cfunc.strToCh(filepath), cfunc.strToCh('rb'))
  bin_digits = cfunc.img_data(fptr)
  matrix = cfunc.process_bytes(bin_digits, int.from_bytes(bin_digits[0:4], byteorder='big'), int.from_bytes(bin_digits[4:8], byteorder='big'))
  train_matrix = ~np.ctypeslib.as_array(matrix, shape=(int.from_bytes(bin_digits[4:8], byteorder='big'),) ).reshape( int.from_bytes(bin_digits[4:8], byteorder='big'), 784) / 255
  # train_matrix = np.ctypeslib.as_array(matrix, (int.from_bytes(bin_digits[4:8], byteorder='big'),784 ))
  # reshape((int.from_bytes(bin_digits[4:8], byteorder='big'), 784))
  # np.reshape(train_matrix, (int.from_bytes(bin_digits[4:8], byteorder='big'), ))
  # train_img = np.array(matrix, 
  cfunc.free(bin_digits)
  cfunc.fclose(fptr)
  return train_matrix

"""Function to read label files.
    Returns 1D array of image labels."""
def labels(filepath):
  fptr = cfunc.fopen(cfunc.strToCh(filepath), cfunc.strToCh('rb'))
  bin_labels = cfunc.label_data(fptr)
  l = np.array(list(bin_labels[8:(int.from_bytes(bin_labels[4:8], byteorder='big')+8)])).astype(np.uint8)
  cfunc.fclose(fptr)
  return l


# test_img = dig_images('../rough_work/t10k-labels.idx1-ubyte')
# train_img = dig_images(fileLoc.fLoc[2])

# test_lbl = labels('../rough_work/t10k-images.idx3-ubyte')
# train_lbl = labels('../rough_work/train-labels.idx1-ubyte')

# print(len(test_img))
# print(len(train_lbl))
# print(len(train_img))
# print(train_lbl[8])

# print(test_img.shape)
# print(test_img[0])
# print(train_img[0])

# print(test_lbl[8])
# print(train_lbl[8])

# with open(fileLoc.fLoc[2], 'rb') as f:
#     test  = f.read()

# t = ~np.array(list(test[16:])).reshape(60000, 784).astype(np.uint8)
# print(t[0])