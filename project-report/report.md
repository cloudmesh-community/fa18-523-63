# Sample Project Report :hand: fa18-523-000 fa18-523-001

| Mark Miller | mgm3@indiana.edu | Indiana University | hid: fa18-523-63 |
github: [:cloud:](https://github.com/cloudmesh-community/fa18-523-63/edit/master
/project-report/report.md) | code: [:cloud:](https://github.com/cloudmesh-
community/fa18-523-63/tree/master/project-code)



Keywords: TensorFlow, RoboAdvisor, Machine Learning



## Abstract

Machine learning [@fa18-523-63-www-machine-learning-wash] has affected many
aspects of many industries, with the expectation that this will continue to
grow. Financial advice [@fa18-523-63-www-fintech-ai] are one such industry that
has been heavily impacted by artificial intelligence and machine learning
concepts. This project explores ways that Tensorflow [@fa18-523-63-www-
tensorflow] methods can be used in a Python 3.6 [@fa18-523-63-www-python-36]
environment. We will cover many of the algorithms inherent to Tensorflow
libraries [@fa18-523-63-www-tensorflow] and use cases for them. The storage for
this project will occur externally, enabling this project to be performed using
cloud computing [@fa18-523-63-www-machine-learning-cloud]. Data sources are
pulled from the Google Finance [@fa18-523-63-www-google-finance]. The code is
used from the aforementioned sources and code as written by the author of this
paper  [@www-fa18-523-63-project-code]. The goal of any financial advisor is to
make decisions that beat the rate of inflation. There are large amounts of
uncertainty with any decision made regarding the New York Stock Exchange
[@fa18-523-63-www-nyse]. An intelligently built and well-diversified investment
portfolio can prove to be very lucrative.



## Introduction

As machine learning has continued its expansion into many industries, different
groups have made ease of access and use with much haste and care.

> "The Google Photos search engine... is enormously impressive - so impressive
that O'Reilly couldn't understand why Google didn't sell access to its AI engine
via the Internet" [@fa-523-63-www-tensorflow-wired]


Not to be outdone by anyone, Google released an Apache 2 license on their
artificial intelligence engine [@fa-523-63-www-tensorflow-wired], which means
that the machine learning methods that were used by Google, were not publicly
available. Tensor flow consists of 3144 methods with the intent of machine
learning, parallel processing, and more. As the impressive Tensorflow library
continues its development and usage in many industries, one of the largest and
most complex industries in the world, the financial sector on Wall Street
[@fa-523-63-www-wall-street-ml], is taking advantage of this opportunity.

Tools that use automation and machine learning to help make investment decisions
are commonly called robo-advisors [@fa-523-63-www-robo-advisor-invest].
Successful investing is among the most complicated problems in existence. This
is due to the seemingly sporadic successes or failures, unpredictability of
market entities, and the inherent high risk of poor decisions.

The goal of this project is to identify ways to implement the gift that Google
gave to the big-data world in Tensorflow [@fa-523-63-www-tensorflow-wired] in
making a robo-advisor that will out-pace the rate of inflation, enabling
someones money to grow faster than inflation. Machine learning methods from
Tensorflow will be used, specifically the Neural Network, Logistic Regression,
and K-means libraries [@fa18-523-63-www-tensorflow].


## Requirements

## Design

### Topology

This project is built on a CentOS server [@fa18-523-63-www-centos]. On this
server, Python 3.6 [@fa18-523-63-www-python-36] will be used as the language.
The Python wrapper for Tensorflow is installed independently [@fa18-523-63-www-
tensorflow]. The following methods from the Tensorflow library are used:
tf.contrib.factorization.KMeans, tf.contrib.factorization.KMeansClustering,
tf.contrib.learn.LinearRegressor, tf.contrib.learn.LogisticRegressor,
tf.contrib.nn. These methods are used to take the input data from the Google
Finance tool [@fa18-523-63-www-google-finance] and perform their operations to
classify whether a given stock is a strong sell, sell, neutral, buy, or strong
buy. This operation is then run daily to make a decision with such granularity
whether a given stock is worth the risk.

### Neural Networks

Neural Networks are used with deep learning principles and capabilities. Neural
networks are second to none when it comes to image classification, deep
learning, and more [@fa18-523-63-www-nn-dl]. Based loosely on the human neural
network, a layered network of neurons take input values, perform mathematical
computations to find trends and relevancy, and output that is typically a
classification, based on the inputs [@fa18-523-63-www-ann-human].

![Artificial Neural Network Inputs to
![Outputs](https://github.com/mgm3IU/fa18-523-63/blob/master/project-
![pictures/ANN.PNG)

In supervised methods, training datasets are required to make neural networks
function. In unsupervised methods and with careful tuning, artificial neural
networks can be used as a clustering algorithm, without classification
assignment [@fa18-523-63-www-unsup-ann].

### Logistic Regression In its simpler forms, logistic regression [@fa18-523-63
-www-logreg] takes input values and uses those to provide a classification based
on the variables to the data. It is robust to highly correlated variables,
concise representation, and high explanatory value with probability estimation
[@fa18-523-63-emc-big-data]. Logistic regression is a supervised learning model,
meaning that it depends on training data to provide results accurately and
efficiently. Tensorflow methods contain the needed utilities to perform logistic
regression with high efficiency [@fa18-523-63-www-tensorflow].

### K-Means Clustering

K-means is an unsupervised clustering algorithm [@fa18-523-63-www-msu-kmeans].
It uses a distance algorithm, typically Euclidean, to determine clusters based
on numerical data. The goal is to maximize the distance between clusters while
minimizing the distance between the data points and the centroid of each cluster
[@fa18-523-63-emc-big-data]. This is an iterative process which tends to
converge quickly. It is, however, senstive to initilization which is the largest
downfall of the K-mean algorithm [@fa18-523-63-emc-big-data].

## Architecture

## Dataset

## Implementation

## Benchmark

## Conclusion

## Acknowledgement

