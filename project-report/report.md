# Financial Robo-Advisor Using Tensorflow :hand: fa18-523-63

| Mark Miller 
| mgm3@indiana.edu 
| Indiana University 
| hid: fa18-523-63 
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-523-63/edit/master/project-report/report.md) 
| code: [:cloud:](https://github.com/cloudmesh-community/fa18-523-63/tree/master/project-code)



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
that the machine learning methods that were used by Google, were then publicly
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
This project required Python 3.6 [@fa18-523-63-www-python-36]. 4 GB of
usable memory (Used for the data stored from the Google Finance API
[@fa18-523-63-www-google-finance] and two cores of CPU for the
virtual machine. The Tensorflow library is also required 
[@fa18-523-63-www-tensorflow]. 8 GB of hard drive space should be allocated.

## Design

The code design is simple. Firstly, we will query the Google API
[@fa18-523-63-www-google-finance] for the needed information from companies
that exist in the S&P 500 [@www-fa18-523-63-sp-500]. Once the data
is collected and stored locally, methods from the Tensorflow library
[@fa18-523-63-www-tensorflow] will be used to determind appropriate scores
to be evaluated using the K-means algorithm [@fa18-523-63-emc-big-data].
Once these steps have been taken, a cluster will be assigned one of the
following five (5) categories: strong sell, sell, neutral, buy, strong buy.

### Topology

This project is built using Anaconda Python services [@fa18-523-63-www-ana-pyt]. On this
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

![Artificial Neural Network Inputs to Outputs](images/ANN.PNG) *Pg 89.ANN
Layered-network example*

[@fa18-523-63-www-nn-dl]



In supervised methods, training datasets are required to make neural networks
function. In unsupervised methods and with careful tuning, artificial neural
networks can be used as a clustering algorithm, without classification
assignment [@fa18-523-63-www-unsup-ann].

### Logistic Regression 
In its simpler forms, logistic regression
[@fa18-523-63-www-logreg] takes input values and uses those to provide
a classification based on the variables to the data. It is robust to
highly correlated variables, concise representation, and high
explanatory value with probability estimation
[@fa18-523-63-emc-big-data]. Logistic regression is a supervised
learning model, meaning that it depends on training data to provide
results accurately and efficiently. Tensorflow methods contain the
needed utilities to perform logistic regression with high efficiency
[@fa18-523-63-www-tensorflow].

### K-Means Clustering

K-means is an unsupervised clustering algorithm [@fa18-523-63-www-msu-kmeans].
It uses a distance algorithm, typically Euclidean, to determine clusters based
on numerical data. The goal is to maximize the distance between clusters while
minimizing the distance between the data points and the centroid of each cluster
[@fa18-523-63-emc-big-data]. This is an iterative process which tends to
converge quickly. It is, however, senstive to initilization which is a
downfall of the K-means algorithms [@fa18-523-63-emc-big-data].

## Architecture

The architecture is a simple usage of Anaconda Python [@fa18-523-63-www-ana-pyt] services. Portions of the
datasets will be saved locally on the virtual hard drive for simpler reading.
This file will have the ability to be updated daily with the information
that is presented from the Google Finance API [@fa18-523-63-www-google-finance]

## Dataset

As previously mentioned, the data sources will come from the Google Finance API
[@fa18-523-63-www-google-finance]. Data from a Wikipedia API for the companies
that exist in the S&P 500 [@www-fa18-523-63-wiki-sp-500]. This data comes
in a .csv file (comma delimmited) forming a table consisting of the following
metrics for each ticker: Date, Open, High, Low, Close, Volume.
* Date - The date which the information represents
* Open - The opening price of stocks for a given ticker
* High - The highest price of stock in that day for a given ticker
* Low - The lowest price of stock in that day for a given ticker
* Close - The closing price of stocks for a given ticker

This data is publicly available and would be categorized as web-scraping
for the purposes of this project [@www-fa18-523-63-web-scraping].
The data is used after being stored locally on the virtual hard disk.
It is piped through the aforementioned machine learning algorithms
in order to decide whether a given stock is worth buying or whether it
should be sold.

## Implementation
The code implementations are saved in the project code files. Implementing this
code depends on the Tensorflow [@fa18-523-63-www-tensorflow] libraries and 
other methods that exist in the Python 3.6 standard library 
[@fa18-523-63-www-python-36]. Once initialized, the virtual machine will
need to have Python 3.6 installed and the Tensorflow library installed
through their prescribed installation mediums. A directory will be created
in which the needed data files, pulled from the Google Finance API
[@fa18-523-63-www-google-finance] will be stored.


## Benchmark
There is no shortage of existing work on financial robo-advisors
[@fa-523-63-www-robo-advisor-top5]. The goal of this project is not
to outperform these many tools but to learn about ways that they could
improve, automate, and undestand ways that machine learning can be
implemented in the financial district. Because one of the project's
goals is to improve upon my existing efforts (1.5 percent growth over
a six-month period), I do not yet have sufficient evidence to claim
that this current model outperforms my existing model.


## Conclusion
Due to the developments and growth of machine learning popularity over
the last decade, Financial robo-advisors are here to stay. Their ease
of purchase or usage varies, as does their deployment. Using these
simple methods from Tensorflow [@fa18-523-63-www-tensorflow], I have
developed my own personal robo-advisor that is able to use comma
separated values as inputs and make output decisions intelligently.

I have learned a lot about current machine learning models, 
implementations, case studies, and usage scenarios. From this,
I conclude that machine learning is the simplest way to make intelligent
, data driven decisions based on the copious data that exists in the
finance sector. I also conclude that using artificial neural networks
[@fa18-523-63-www-nn-dl], along side logistic regression 
[@fa18-523-63-www-logreg], can yield effective robo-advisors, using the
simple implementation as is provided by machine learning engines such
as Tensorflow [@fa18-523-63-www-tensorflow].

As is mentioned in the Benchmark Section, metrics regarding whether
this model improves my previously created model will not be available
for months, due to the nature of the project and the problem it is
attempting to solve.

## Acknowledgements
Some principals for the web-scraping and data usage were adapted from
pythonprogramming.net [@www-fa18-523-63-python-finance]. The analytics
are the result of the project.

