#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=42)

classifier = tree.DecisionTreeClassifier()
classifier.fit(train_features, train_labels)

score = classifier.score(test_features, test_labels)
predictions = classifier.predict(test_features)

precision = precision_score(test_labels, predictions)
recall = recall_score(test_labels, predictions)

print "Score: ", score, "; Precision: ", precision, "; Recall: ", recall


poi_count = 0
for prediction in predictions:
    if (prediction):
        poi_count += 1

print poi_count, " predicted POIs, over ", len(predictions)


true_positives_count = 0
for index in (0, len(predictions) - 1):
    is_predicted_poi = predictions[index]
    is_true_positive = predictions[index] == test_labels[index]
    if (is_predicted_poi and is_true_positive):
        true_positives_count += 1

print true_positives_count, " true positives"
