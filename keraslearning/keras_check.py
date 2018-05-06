"""Keras check verify keras is installed properly"""

import numpy as np
from keras import backend as kbe
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1" # LEVEL 0: INFO, LEVEL 1: WARNING

# Test keras - Backend interaction
data = kbe.variable(np.random.random((4, 2))) # create a 4*2 tensor of random numbers

zero_data = keb.zeros_like(data) # create zeros tensor of same size as data

print(keb.eval(zero_data))