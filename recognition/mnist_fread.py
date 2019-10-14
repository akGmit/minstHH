#!/usr/bin/python3
""" Read MNIST training and test files """
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from recognition import cfunc

#Open bin data file for reading, using C stdio I/O library funcrion
fptr = cfunc.fopen(cfunc.strToCh("../rough_work/train-images.idx3-ubyte"), cfunc.strToCh('rb'))

#Load raw data to memory
bin_digits = cfunc.img_data(fptr)

fptr = cfunc.fopen(cfunc.strToCh("../rough_work/train-labels.idx1-ubyte"), cfunc.strToCh('rb'))
bin_labels = cfunc.label_data(fptr)
#Process binary file data and return array of each digi matrices
#Store labels
matrix = cfunc.process_bytes(bin_digits, int.from_bytes(bin_digits[0:4], byteorder='big'), int.from_bytes(bin_digits[4:8], byteorder='big'))
labels_train = cfunc.label_data(fptr)

#Free mem, close file
cfunc.free(bin_digits)
cfunc.fclose(fptr)

#Plot image
image = ~np.array(matrix[1]).reshape(28,28).astype(np.uint8)
print(int.from_bytes(labels_train[10:11], byteorder='big'))
for l in range(7,100): print(int.from_bytes(labels_train[l:l+1], byteorder='big'), end='-')
plt.imshow(image, cmap='gray')
plt.show()
