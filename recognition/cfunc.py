"""Ctypes function module.
    
C functions wrapped for usage.
"""
import ctypes  as ctype
from ctypes import *
# import clibs
#libc = None
# Get reference to C library
def loadLibc():
  libc = ctype.CDLL('clibs/mnistread.so')
  return libc

def strToCh(s):
  """Convert python string to char array, for C native functions.
  
  Parameters:
    string: python string to be converted.
  
  Returns:
    char[]: array of characters for C  functions.

  """
  return ctype.create_string_buffer(str.encode(s))


def fopen(filepath, mode):
  """Get a C FILE type pointer to a file.

  Parameters:
    filepath: path to the file.
  
  Returns:
    FILE*: C pointer to the file.

  """
  fopen = wrap_function(loadLibc(), 'fopen', ctype.c_void_p, [
                        ctype.c_char_p, ctype.c_char_p])
  # fopen = wrap_function(libc, 'fopen', ctype.c_void_p, [
  #                       ctype.c_char_p, ctype.c_char_p])
  return fopen(filepath, mode)


def fclose(file_pointer):
  """Close C file.

  Parameters:
    file pointer: pointer with FILE address.
  
  Returns:
    int: value indicating if closing was succesfull.

  """
  f = wrap_function(loadLibc(), 'fclose', ctype.c_int, [ctype.c_void_p])
  return f(file_pointer)


def free(address):
  """Free memory address.

  C function to empty memory address.

  Parameters:
    pointer: pointer to the address.

  """
  f = wrap_function(loadLibc(), 'free', ctype.c_void_p, None)
  return f(address)


def img_data(file_pointer):
  """C library function to read image data from file.

  Function implemented in C to efficiently read MNIST image data format file.

  Parameters:
    file pointer: C pinter to the file.
  
  Returns:
    binary file contents.

  """
  f = wrap_function(loadLibc(), 'img_data',  ctype.POINTER(
      ctype.c_uint8), [ctype.c_void_p])
  return f(file_pointer)


def label_data(file_pointer):
  """C function to read MNIST fortmat label file.

  Efficiently reads file using C native functions.

  Parameters:
    file pointer: C pinter to the file.
  
  Returns:
    binary file contents.

  """
  f = wrap_function(loadLibc(), 'label_data',  ctype.POINTER(
      ctype.c_uint8), [ctype.c_void_p])
  return f(file_pointer)


def process_bytes(uint_bytes_arr, magic_num, item_count):
  """C function to process bytes data file.

  Takas raw MNIST binary file contents and processes them to 2d matrix for each image.

  Returns:
    array of 2D arrays for each image.

  """
  f = wrap_function(loadLibc(), 'process_bytes', ctype.POINTER(
      (ctype.c_uint8 * 28) * 28), [ctype.POINTER(ctype.c_ubyte), ctype.c_long, ctype.c_int])
  return f(uint_bytes_arr, magic_num, item_count)


def wrap_function(lib, funcname, restype, argtypes):
  """C function wrpper to create pointers to C functions."""
  func = lib.__getattr__(funcname)
  func.restype = restype
  func.argtypes = argtypes
  return func
