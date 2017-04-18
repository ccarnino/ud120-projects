#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

# Just keep 1% of the training set
# features_train = features_train[:len(features_train) / 100]
# labels_train = labels_train[:len(labels_train) / 100]

# Train the classifier
classifier = SVC(kernel='rbf', C=10000)

trainingTimeBegin = time()
classifier.fit(features_train, labels_train)
trainingTimeEnd = time()

print "Time required for training: ", round(trainingTimeEnd - trainingTimeBegin, 3), "s"

# Make predictions on the test set
predictingTimeStart = time()
predictions = classifier.predict(features_test)

predictingTimeEnd = time()
print "Time required for predicting: ", round(predictingTimeEnd - predictingTimeStart, 3), "s"

# Get accuracy
accuracy = accuracy_score(labels_test, predictions)
print "Accuracty: ", accuracy

# Print the classes of specific test entries
print "Class item 10: ", predictions[10]
print "Class item 26: ", predictions[26]
print "Class item 50: ", predictions[50]

# Count the number of test entries have been classified as Chris (class 1)
print "Number of test entries classified as Chris (class 1): ", (predictions == 1).sum()

#########################################################
