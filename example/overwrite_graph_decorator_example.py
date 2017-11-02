import sys
import tensorflow as tf
sys.path.append('.')
from util import overwrite_graph


@overwrite_graph
def main():
    # Define your placeholders, model, etc.
    data = tf.placeholder(tf.float32)
    target = tf.placeholder(tf.float32)
    # model = Model()


if __name__ == "__main__":
    main()
