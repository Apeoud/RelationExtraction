import tensorflow as tf


class Network(object):

    def __init__(self, num_classes):
        # hyper parameter
        self.num_classes = num_classes

        # input & placeholder
        self.input_word = tf.placeholder(dtype=tf.int32, shape=[None, num_steps], name='input_word')
        self.input_pos1 = tf.placeholder(dtype=tf.int32, shape=[None, num_steps], name='input_pos1')
        self.input_pos2 = tf.placeholder(dtype=tf.int32, shape=[None, num_steps], name='input_pos2')
        self.input_y = tf.placeholder(dtype=tf.float32, shape=[None, num_classes], name='input_y')

        # embedding

        word_embedding = tf.get

        return
