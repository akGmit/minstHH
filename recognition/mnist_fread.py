#!/usr/bin/python3
""" Read MNIST training and test files """
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from recognition import cfunc

#Open bin data file for reading, using C stdio I/O library funcrion
fptr = cfunc.fopen(cfunc.strToCh("../rough_work/t10k-images.idx3-ubyte"), cfunc.strToCh('rb'))

#Load raw data to memory
bin_data = cfunc.img_data(fptr)
#Process binary file data and return array of each digi matrices
matrix = cfunc.process_bytes(bin_data, int.from_bytes(bin_data[0:4], byteorder='big'), int.from_bytes(bin_data[4:8], byteorder='big'))

#Free mem, close file
cfunc.free(bin_data)
cfunc.fclose(fptr)

#Plot image
image = ~np.array(matrix[0]).reshape(28,28).astype(np.uint8)
plt.imshow(image, cmap='gray')
plt.show()
