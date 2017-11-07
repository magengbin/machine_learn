# Introduction to How TensorFlow Graphs Work

TensorFlow has a unique way of solving problems. This unique way allows for solving of machine learning problems very efficiently.  There are a few common steps to most TensorFlow algorithms.

1. Import data, generate data, or setup a data-pipeline through placeholders.
2. Feed data through computational graph.
3. Evaluate output on loss function.
4. Use backpropagation to modify the variables.
5. Repeat until stopping condition.
