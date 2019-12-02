import numpy as np
def center_of_mass(pixels): 

  left = np.zeros((20,4))
  centered = np.concatenate((left, pixels),axis=1)
  
  top = np.zeros((4,24))
  centered = np.concatenate((top, centered), axis=0)

  right = np.zeros((24,4))
  centered = np.concatenate((centered, right), axis=1)

  bottm = np.zeros((4, 28))
  centered = np.concatenate((centered, bottm), axis=0)
  
  return centered
