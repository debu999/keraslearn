"""Keras check verify keras is installed properly"""

import numpy as np
from keras import backend as kbe
import os
import warnings
warnings.filterwarnings('ignore', '.*do not.*',)

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1" # LEVEL 0: INFO, LEVEL 1: WARNING

# Test keras - Backend interaction
data = kbe.variable(np.random.random((4, 2))) # create a 4*2 tensor of random numbers

zero_data = kbe.zeros_like(data) # create zeros tensor of same size as data

print(kbe.eval(zero_data))