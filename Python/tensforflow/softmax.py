import tensorflow as tf

logit_data = tf.Variable([2, 1, .1])

soft_max = tf.nn.softmax(logit_data)

tf.print(soft_max)
tf.print(tf.argmax(soft_max))
