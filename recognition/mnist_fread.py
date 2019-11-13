
"""Function definitions to read MNIST files to memory.

These functions use ctypes module functionality and calls foreign C functions.
Using stdio C  library significantly increased efficiancy of reading and processing data files.
"""
import numpy as np
import recognition.cfunc as cfunc
def dig_images(filepath):
  """Read  MNIST format train and test binnary image files.

  Function takes file path as parameter, gets a pointer to file using C fopen() function.
  Reads binary data file in one go to memory and then calls another custom C function to process raw data into 60000by28by28 array.
  Returns 60000by784 array ready for feeding to NN.

  Params:
    filepath: a path to a image file.

  Returns:
    img matrix: an array of 2d image matrixes.
    
  """
  fptr = cfunc.fopen(cfunc.strToCh(filepath), cfunc.strToCh('rb'))
  bin_digits = cfunc.img_data(fptr)
  matrix = cfunc.process_bytes(bin_digits, int.from_bytes(bin_digits[0:4], byteorder='big'), int.from_bytes(bin_digits[4:8], byteorder='big'))
  train_matrix = ~np.ctypeslib.as_array(matrix, shape=(int.from_bytes(bin_digits[4:8], byteorder='big'),) ).reshape( int.from_bytes(bin_digits[4:8], byteorder='big'), 784) / 255.0
  cfunc.free(bin_digits)
  cfunc.fclose(fptr)
  return train_matrix

def labels(filepath):
  """Read MNIST format labels file.

  Params:
    filepath: path to label file.

  Returns:
    label: 1D array of image labels.

  """
  fptr = cfunc.fopen(cfunc.strToCh(filepath), cfunc.strToCh('rb'))
  bin_labels = cfunc.label_data(fptr)
  l = np.array(list(bin_labels[8:(int.from_bytes(bin_labels[4:8], byteorder='big')+8)])).astype(np.uint8)
  cfunc.fclose(fptr)
  return l
