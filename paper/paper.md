# Scikit-learn :wave: :exclamation: fa18-523-63

| Mark Miller
| mgm3@iu.edu
| Indiana University Bloomington
| hid:fa18-523-63
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-523-63/edit/master/paper/paper.md)



Keywords: HID fa18-523-63, Scikit Learn, Machine Learning Methods, Python, Artificial Intelligence

Scikit-learn [@www-fa18-523-63-scikit-learn-developers] is Python's inherent machine learning library. It is a robust library that intends uses object oriented programming to implement commonly used machine learning algorithms effectively, efficiently, pythonically, and swiftly. While, for specific purposes, many experts are able to implement their own algorithms that may improve upon the Scikit-learn library, it has sufficient tools and robustness that enable it to be the leading library for machine learning topics within Python.

There are built in libraries to Python that can make these tasks much simpler to understand and to implement, Scikit-learn provides one such solution [@www-fa18-523-63-scikit-learn-developers]. Junior machine learning experts are gaining footing in the industry and are able to gain reputation, thanks to the help of many of these libraries.

As data becomes larger and larger with time, experts in the field are needed to perform this operation. Or, better stated, experts are needed to be able to program computers to perform these operations for them. A computer can process streamlined and well-defined data faster than humans in some instances, especially when reviewing the data becomes increasingly tedious. While algorithms may never be as good at recognizing what is in an image quite like a human can, they will become closer and closer to the point where advertizing will be even more targeted, devices will understand the wants of their human masters clearly, and effective decisions can be made with minimal error. Scikit-learn is not the most sophisticated a capable machine learning algorithm out there, but it is effective and easily implemented via Python, which will make it the workhorse of my semester project.

## The supervised algorithms (some of them)

+ Nearest Neighbors: Nearest neighbors is a machine learning algorithm that makes the decision of one input variable based on training data (making it a supervised algorithm) that most similarly matches itself. Once one of the training sets is identified as the closest match of inputs, it will assign the same category for the test instance. With careful parameter tuning, some scholars believe this to be a better classification method than random forests [@www-fa18-523-63-knn]
+ Naive Bayes: Naive Bayes takes a look at Baysian statistics and makes one majorly naive assumption: all of the inputs are independent of each other. While this is a glaring assumption, due to ease of implementations, most issues that would arise from generally erroneous assumption are not impactful [@www-fa18-523-63-naive-bayes]. 
+ Decision trees: Separating on different attributes of the input data, decision trees are one of the more robust machine learning algorithms in that they are able to handle a wide variety of inputs and still maintain their quality [@www-fa18-523-63-decision-trees]. Splitting on each attributes (usually on traits that maximize the entropy of the model, to enhance effectiveness). A branch off algorithm to decision trees are random forests which use many small, randomly chosen (with replacement) trees that can use small subsets of the data to formulate better opinions in a less computationally intensive way.
+ Neural network models (supervised) {@www-fa18-523-64-sup-nn] are algorithms that are particularly good at image classification. They obtain different neurons, each of which contributes in the decision making. They are based off of the way a human neural network would work if it could be modeled accurately via code. each neural network has different levels which contribute to the decision making process.

## The unsupervised algorithms (some of them)

There are many unsupervised learning algorithms supported by Scikit, here is highlighted two of them.

+ Clustering [@www-fa18-523-63-km-init]: Stemming from the k-means clustering, this is designed to group the datapoints based on similarity to others in in the same dataset. The inputs are generally strictly numerical but can be n-dimmensional. Clustering converges quickly via iterative methods but is highly sensitive to initialization, making it very important to have domain knowledge and valuable visualization strategies when the data is 3-dimmensional and higher.
+ Neural Network (unsupervised) [@www-fa18-523-63-4084683]: much like the aforementioned neural networks, sklearn has libraries for unsupervised machine learning algorithms, which don't require training data to make decisions. In this sense, it becomes more of a clustering algorithm than a group identification.

## Other Method groupings within sklearn

+ Dataset transformations [www-fa18-523-63-scikit-learn-developers]: Oftentimes, data comes mangled and hard to use, requiring the need for effective data wrangling. scikit-learn has methods for feature extraction, preprocessing, random projection, dimmensionality reduction, and more. This makes it a valuable library for more aspects than just the machine learning algorithms themselves. 
+ Dataset loading utilities [www-fa18-523-63-scikit-learn-developers]: Scikit-learn has the utilities needed to load data as well as read it. There are Application Programming Interfaces for training datasets, real-world datasets, generated-datasets, and the tools needed to use them effectively.

## Further functionalities to Scikit
There are more uses and tools in scikit-learn than what I have mentioned here. I couldn't just copy the user guide or man pages for these articles, even though they are good. The user guide contains valuable examples and assists with syntax. You will need basic machine learning understanding to be able to use any of these methods in this library. Once the understanding is there and basic implementations are used, microtuning and enhancing of the algorithms comes quickly and simply to an expert with a good eye. I didn't mention every individual method because there are plenty that I have no experience using and don't understand the nature of the machine learning or other algorithm. 

## Real world applications for scikit learn

The real world applications are nearly as endless as are the applications for machine learning and artificial intelligence. The trick is getting the data to work together, whether that be through internet of things, internet of computers, internet of people, etc. I have personally used this tool in many ways, ranging from sports analytics to automation of analysis of the stock exchange. Expert knowledge of this library alone can bring six-figure salaries as a machine learning engineer, which many major and minor companies alike choose to employ. 

