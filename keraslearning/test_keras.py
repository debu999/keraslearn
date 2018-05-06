# Verify that tensorflow is working.
import tensorflow as tf

# print version 
print("Tensorflow version is " str(tf.__version__))

#verify session works

hello = tf.constand("Hello from Tensorflow")
sess = tf.Session()
print(sess.run(hello))

