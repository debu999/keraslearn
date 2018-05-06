# Verify that tensorflow is working.
import tensorflow as tf
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1" # LEVEL 0: INFO, LEVEL 1: WARNING
# print version 
print("Tensorflow version is " + str(tf.__version__))

#verify session works

hello = tf.constant("Hello from Tensorflow")
sess = tf.Session()
print(sess.run(hello))

