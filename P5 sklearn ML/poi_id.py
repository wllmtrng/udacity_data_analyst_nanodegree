#!/usr/bin/python

import os
import sys
import pickle
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.grid_search import GridSearchCV

sys.path.append(os.getcwd() + "/tools/")
from tester import dump_classifier_and_data

# Load the dictionary containing the dataset
with open("./final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

# Replace "Nan" with 0 in the data
for columns in data_dict.itervalues():
    for k, v in columns.iteritems():
        if type(v) is str and v.lower() == "nan":
            columns[k] = 0

# Convert to pandas dataframe for easy feature creation
enron_df = pd.DataFrame.from_dict(data_dict, orient="index")

# Drop outliers
enron_df.drop('TOTAL', inplace=True)
enron_df.drop("THE TRAVEL AGENCY IN THE PARK", inplace=True)
enron_df.drop("LOCKHART EUGENE E", inplace=True)

# Drop email_address column
enron_df.drop('email_address', axis=1, inplace=True)

# Create Features
enron_df['from_poi_ratio'] = enron_df['from_poi_to_this_person'] / enron_df['from_messages']
enron_df['to_poi_ratio'] = enron_df['from_this_person_to_poi'] / enron_df['to_messages']
enron_df['bonus_ratio'] = enron_df['bonus'] / enron_df['salary']
enron_df.fillna(0, inplace=True)

# Separate labels and features
enron_df_labels = enron_df['poi']
enron_df_features = enron_df[enron_df.columns.difference(['poi'])]

# Use SelectKBest and GaussianNB
pipeline = Pipeline([
    ('kbest', SelectKBest()),
    ('gnb', GaussianNB())])

folds = 100
cv = StratifiedShuffleSplit(enron_df_labels, n_iter=folds, random_state=42, test_size=0.20)
parameters = {"kbest__k": [1, 2, 3, 5, 8, 13, 19], "kbest__score_func": [f_classif]}
clf = GridSearchCV(pipeline, param_grid=parameters, cv=cv, scoring='f1')
clf.fit(enron_df_features, enron_df_labels)

# Select Features
kbest = clf.best_estimator_.steps[0][1]
kbest.get_support()
features = sorted(zip(enron_df_features.columns, kbest.scores_, kbest.get_support()), key=lambda x: x[1])
my_list = [x[0] for x in features if x[2] == True]
my_list = ['poi'] + my_list

my_dataset = enron_df[my_list].transpose().to_dict()

dump_classifier_and_data(clf.best_estimator_.steps[1][1], my_dataset, my_list)
