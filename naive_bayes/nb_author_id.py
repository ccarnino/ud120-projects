#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
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
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Train the classifier
classifier = GaussianNB()

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

#########################################################
