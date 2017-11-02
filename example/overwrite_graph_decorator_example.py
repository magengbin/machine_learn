import tensorflow as tf
import sys
sys.path.append('.')
from util import overwrite_graph
from lazy_property_decorator_example import Model

@overwrite_graph
def main():
    # Define your placeholders, model, etc.
    print("main run")
    data = tf.placeholder(tf.float32)
    target = tf.placeholder(tf.float32)
    model = Model(data=data, target=target)


if __name__ == '__main__':
    main()
