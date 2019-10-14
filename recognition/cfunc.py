''' Ctypes function module.
    C functions wrapped for usage.'''
import ctypes

libc = ctypes.CDLL('../rough_work/mnistread.so')

def strToCh(s):
    return ctypes.create_string_buffer(str.encode(s))

def fopen(filename, mode):
    fopen = wrap_function(libc, 'fopen',ctypes.c_void_p, [ctypes.c_char_p, ctypes.c_char_p])
    return fopen(filename, mode)

def fclose(file_pointer):
    f = wrap_function(libc, 'fclose', ctypes.c_int, [ctypes.c_void_p])
    return f(file_pointer)

def free(address):
    f = wrap_function(libc, 'free', ctypes.c_void_p, None)
    return f(address)

def img_data(file_pointer):
    f =  wrap_function(libc, 'img_data',  ctypes.POINTER(ctypes.c_uint8), [ctypes.c_void_p])
    return f(file_pointer)

def label_data(file_pointer): 
    f = wrap_function(libc, 'label_data',  ctypes.POINTER(ctypes.c_uint8), [ctypes.c_void_p])
    return f(file_pointer)

def process_bytes(uint_bytes_arr, magic_num, item_count): 
    f = wrap_function(libc, 'process_bytes',ctypes.POINTER((ctypes.c_uint8 * 28) *28), [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_long, ctypes.c_int])
    return f(uint_bytes_arr, magic_num, item_count)

""" wrap function to define ctypes functions """
def wrap_function(lib, funcname, restype, argtypes):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

    