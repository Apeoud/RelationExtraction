import tensorflow as tf


class Network(object):

    def __init__(self, num_classes, word_embedding_initializer):
        # hyper parameter
        self.num_classes = num_classes
        num_steps = 0
        pos_num = 0
        pos_size = 0

        # input & placeholder
        self.input_word = tf.placeholder(dtype=tf.int32, shape=[None, num_steps], name='input_word')
        self.input_pos1 = tf.placeholder(dtype=tf.int32, shape=[None, num_steps], name='input_pos1')
        self.input_pos2 = tf.placeholder(dtype=tf.int32, shape=[None, num_steps], name='input_pos2')
        self.input_y = tf.placeholder(dtype=tf.float32, shape=[None, num_classes], name='input_y')

        # embedding

        word_embed = tf.get_variable(name="word_embedding", initializer=word_embedding_initializer)
        pos1_embed = tf.get_variable(name="pos1_embedding", shape=[pos_num, pos_size])
        pos2_embed = tf.get_variable(name="pos2_embedding", shape=[pos_num, pos_size])

        # forward network

        return
