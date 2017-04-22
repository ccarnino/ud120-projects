#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print "People contained in the dataset: ", len(enron_data)

featuresCount = len(enron_data["SKILLING JEFFREY K"])
print "Features count: ", featuresCount

personsOfInterest = {k: v for k, v in enron_data.iteritems() if v["poi"] }
print "Number of persons of interest: ", len(personsOfInterest)

print "Number of total payment for Skilling: ", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Number of total payment for Lay: ", enron_data["LAY KENNETH L"]["total_payments"]
print "Number of total payment for Fastow: ", enron_data["FASTOW ANDREW S"]["total_payments"]

peopleWithDefinedSalary = {k: v for k, v in enron_data.iteritems() if v["salary"] != "NaN" }
print "Number of people with a defined salary: ", len(peopleWithDefinedSalary)

peopleWithDefinedEmail = {k: v for k, v in enron_data.iteritems() if v["email_address"] != "NaN" }
print "Number of people with a defined email address: ", len(peopleWithDefinedEmail)

peopleWithMissingTotalPayments = {k: v for k, v in enron_data.iteritems() if v["total_payments"] == "NaN" }
peopleWithMissingTotalPaymentsPercentage = (float(len(peopleWithMissingTotalPayments)) / len(enron_data)) * 100
print "Number of people with missing total payments: {} ({}% overall)".format(len(peopleWithMissingTotalPayments), peopleWithMissingTotalPaymentsPercentage)

poisWithMissingTotalPayments = {k: v for k, v in personsOfInterest.iteritems() if v["total_payments"] == "NaN" }
poisWithMissingTotalPaymentsPercentage = (float(len(poisWithMissingTotalPayments)) / len(personsOfInterest)) * 100
print "Number of POIs with missing total payments: {} ({}% overall)".format(len(poisWithMissingTotalPayments), poisWithMissingTotalPaymentsPercentage)
