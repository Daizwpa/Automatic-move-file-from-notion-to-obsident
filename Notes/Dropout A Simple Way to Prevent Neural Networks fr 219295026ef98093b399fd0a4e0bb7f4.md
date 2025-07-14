# Dropout: A Simple Way to Prevent Neural Networks from Overfitting

Author: Nitish Srivastava
DataSet: MNIST; SVHN; CIFAR-10/100; ImageNet;  TIMIT;  Reuters-RCV1;  Alternative Splicing
Date published: 01/01/2014
Key word: Deep Learning, model combination, neural networks, regularization
Status: In progress
Task: Not categorized
Data type : imagery data, speech data, text data
Type of paper: Experimental article

Some solution for overfitting:

- These include stopping the training as soon as performance on a validation set starts to get worse (early stopper).
- Introducing weight penalties of various kinds such as L1 and L2 regularization.
- Soft weight sharing.

With unlimited computation, the best way to “regularize” a fixed-sized model is to average the predictions of all possible settings of the parameters, weighting each settings by its posterior probability given the training data. This can sometimes be approximated quite well for simple or small models, but we would like to approach the performance of the Bayesian gold standard using considerably less computation.

Dropout is a technique that addresses both these issues. It prevents overfitting and provides a way of approximately combining exponentially many different neural network architectures efficiently.

The term  “dropout” refers to dropping out units in a neural network. by dropping a unit out, we mean temporarily removing it from the network, along with  all its incoming and outgoing connection. 

The choice of which units to drop is random. 

Applying dropout to a neural network amounts to sampling a “thinned" network from it