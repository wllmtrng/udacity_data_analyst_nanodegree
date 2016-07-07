
# Identifying Persons of Interests from the Enron Email Dataset and Financial Data
by William Truong, in fulfillment of Udacity's [Data Analyst Nanodegree](https://www.udacity.com/course/nd002), Project 4

## Introduction

In 2000, Enron was one of the largest companies in the United States. By 2002, it had collapsed into bankruptcy due to widespread corporate fraud. In the resulting Federal investigation, a significant amount of typically confidential information entered into the public record, including tens of thousands of emails and detailed financial data for top executives.

In this project, with the dataset containing employees working at Enron, with each employee identified as person of interest (which means individuals who were indicted, reached a settlement or plea deal, or testified), the sklearn toolkit was used to assess the possiblility of building a person of interest identifier.

## Goal

Enron email and financial data has been compiled into a dictionary with the following features for each person:

* **financial features**: ['salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees'] (all units are in US dollars)

* **email features**: ['to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi'] (units are generally number of emails messages; notable exception is ‘email_address’, which is a text string)

* **POI label**: [‘poi’] (boolean, represented as integer)

Machine learning was used to attempt to find out if we can create a person of interest identifier based on these features, derived features, principal component analysis, and by using the Gaussian Naive Bayes and the Decision Tree algorithms.

## Data Exploration and Cleanup

### Summary

* Dataset contains 146 people
* 18 Persons of Interest
* 1352 NaN entries
  * director_fees, loan_advances, and restricted_stock_deferred  contain NaN entries for 90%

### Cleanup

By looking at that the financial information from which the dataset was derived from, most of the NaN data are in fact zero values. All NaN were replaced with zeros as a result.

There was also a column "email_address" that did supply any useful information for the classifier. This column was removed.

### Outlier Investigation

Looking at the people in the dataset, there was one obvious outlier. One entry was "TOTAL", which represented the sums of all the columns for each row. I chose not to remove any other entries such as "THE TRAVEL AGENCY IN THE PARK" (which doesn't sound like an employee) or "LOCKHART EUGENE E" (a person who has mostly NaN entries) because these entries can represent potential test cases and should be accounted for.

If it was definite that these type of entries would never show up as input to be predicted, then it would be removed.

## Feature Engineering and Selection

### Features Created

Three features were created in hopes of creating a better fit for the algorithms being used:

1. Percentage of emails received by a person that were from a poi.
2. Percentage of emails sent to a poi.
3. The bonus to salary ratio.

It would be a plausible hypothesis to state that poi's were more likely to send and receive mails to and from other poi's. Poi's were also suspected to have a higher bonus to salary ratio.

### Feature Selection

SelectKBest was initially used to determine feature importance. The results is as follows:

<table>
<tr><td>exercised_stock_options  </td><td style="text-align: right;">25.0975   </td></tr>
<tr><td>total_stock_value        </td><td style="text-align: right;">24.4677   </td></tr>
<tr><td>bonus                    </td><td style="text-align: right;">21.06     </td></tr>
<tr><td>salary                   </td><td style="text-align: right;">18.5757   </td></tr>
<tr><td>deferred_income          </td><td style="text-align: right;">11.5955   </td></tr>
<tr><td>bonus_ratio              </td><td style="text-align: right;">10.9556   </td></tr>
<tr><td>long_term_incentive      </td><td style="text-align: right;">10.0725   </td></tr>
<tr><td>restricted_stock         </td><td style="text-align: right;"> 9.3467   </td></tr>
<tr><td>total_payments           </td><td style="text-align: right;"> 8.87384  </td></tr>
<tr><td>shared_receipt_with_poi  </td><td style="text-align: right;"> 8.74649  </td></tr>
<tr><td>loan_advances            </td><td style="text-align: right;"> 7.24273  </td></tr>
<tr><td>expenses                 </td><td style="text-align: right;"> 6.2342   </td></tr>
<tr><td>from_poi_to_this_person  </td><td style="text-align: right;"> 5.34494  </td></tr>
<tr><td>from_poi_ratio           </td><td style="text-align: right;"> 5.20965  </td></tr>
<tr><td>other                    </td><td style="text-align: right;"> 4.24615  </td></tr>
<tr><td>to_poi_ratio             </td><td style="text-align: right;"> 4.16908  </td></tr>
<tr><td>from_this_person_to_poi  </td><td style="text-align: right;"> 2.42651  </td></tr>
<tr><td>director_fees            </td><td style="text-align: right;"> 2.10766  </td></tr>
<tr><td>to_messages              </td><td style="text-align: right;"> 1.69882  </td></tr>
<tr><td>deferral_payments        </td><td style="text-align: right;"> 0.217059 </td></tr>
<tr><td>from_messages            </td><td style="text-align: right;"> 0.164164 </td></tr>
<tr><td>restricted_stock_deferred</td><td style="text-align: right;"> 0.0649843</td></tr>
</table>

The number of the best features that was used for a given algorithm were determined by having GridSearchCV go through the different permutation of parameters in the pipeline.

## Classifier Selection

Two algorithms was considered for this problem: Gaussian Naive Bayes and Decision Trees. These two algorithms were chosen due to the short time needed for training.

Due to the unbalanced training set and the limited number of positive classes, stratified shuffle splits was chosen for the cross validation strategy. This strategy also helped keep the distribution of the classes the same for each fold. Scikit Learn's GridSearchCV was also leveraged to find the best parameters for each classifier. For some pipelines, principal component analysis was used instead of the features found in SelectKBest for performance comparison.

Accuracy is not a good measure of how well a classifer can do in this case due to the dataset having an unbalanced class. Therefore f1 scores were used to assess how well a classifer fitted on the dataset.

### Classifer Selection Results

#### Gaussian Naive Bayes, StratifiedShuffleSplit, 100 folds, 80/20 

| Pipeline                 | Precision | Recall    | F1     |
| ---------------------    | --------: | --------: |------: |
| SelectKBest, GNB         |     0.489 |     0.380 | 0.428  |
| StandardScaler, PCA, GNB |  0.289    |   0.288   | 0.289   |


#### Decision Trees, StratifiedShuffleSplit, 100 folds, 80/20 

| Pipeline                 | Precision | Recall     | F1     |
| ---------------------    | --------: | --------:  |------: |
| SelectKBest, DT          |     0.309  |     0.300 | 0.305  |
| StandardScaler, PCA, DT  |  0.248     |   0.246   | 0.247  |


StandardScalar was used prior to PCA to properly scale features so that the mean is 0 and distributed according to standard deviations.

A quick observation to point out is that PCA performed poorly for both classifers. In retrospect PCA was not a good choice for this dataset, since there weren't many features to begin with and the number of data points were not so huge as to warrant the usage of PCA. However, if features were transformed to make them more linear, then maybe it would have been of use.

SelectKBest and Gaussian Naive Bayes through GridSearchCV resulted in the best results with an F1 score of 0.428. The top 5 KBest parameters: 
```
['deferred_income',
 'salary',
 'bonus',
 'total_stock_value',
 'exercised_stock_options']
```
were used in conjunction with Gaussian Naive Bayes.

For Decision Trees, an attempt was made to see if using a subset of the max features as defined by max_features = [None, 'auto', 'log2'] and either the criterion gini or entropy through GridSearchCV would result in a good F1 Score.

## Parameter Tuning and Validation Strategy

The purpose of tuning the parameters of an algorithm thorough pipelines and GridSearchCV is to see if an optimal combination of paramters can be used to create an perfomant classifier. Very limited tuning had to happen for the best classifier (SelectKBest and Gaussian Naive Bayes). For Decision Trees, there were more parameters that could have been tuned to create a more accurate classifier, but that would have increased the time to come up with a good classifier.

Validation is important to ensure that the classifier that has been created with the ideal parameters before testing with the dataset. The lack of a validation set would mean that choosing parameters would be likely to have overfit the training data, making it worse off when predicting data that has not yet been seen by the classifier.

StratifiedShuffleSplit was the validation strategy that was chosen for this dataset due to the small number of entries in the dataset and due to the unbalanced classes. The ability to create random folds with a similar distribution of the classes for the training, validation, and testing data proved beneficial in choosing the best parameters. Doing a tradional 80% training/validation and 20% testing would of potentially split the data in the wrong way or resulted in not enough data to train the classifier.

## Evaluation Metrics

Accuracy was not used to determine the fit of the classifier to the dataset due to it's unbalanced class distribution. Simply saying that everyone was not a person of interest would have resulted in a classifer that is highly accurate. F1 scoring and precision/recall values is a better scoring method for this scenario since the number of true positives, true negatives, false negatives, and false positives are important in creating the best fit for a classifier.

## Resources and References

- [scikit-learn Documentation](http://scikit-learn.org/stable/documentation.html)
- Udacity Forums
