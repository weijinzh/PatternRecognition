#Question 1
#Write code to train a multi-class support vector classifier with dot-product kernel and 1-norm soft
#margin using the MNIST training data set. Then report the performance using MNIST test data set.
#There is a hyper-parameter that sets the trade-off between the margin and the training error ---
#tune this hyper-parameter through cross-validation.
import numpy as np
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import gzip
import pickle
ImageFile = 'mnist.pkl.gz'
Images = gzip.open(ImageFile,'rb')
training,validation,testing = pickle.load(Images,encoding = 'latin1')

trainingData,trainingTarget = training[0],training[1]
trainingData = np.concatenate((trainingData,validation[0]),axis=0)
trainingTarget = np.concatenate((trainingTarget,validation[1]),axis=0)

#Performance when C = 0.5
classifier = LinearSVC(C=0.5,class_weight=None,dual=False,fit_intercept=True,
                       intercept_scaling=1,max_iter=1000,multi_class='ovr',
                       penalty='l1',random_state=None, tol=0.0001,
                       verbose=0)
classifier.fit(trainingData,trainingTarget)
classifier.score(testing[0],testing[1])

#Performance when C = 1
classifier2 = LinearSVC(C=1,class_weight=None,dual=False,fit_intercept=True,
                        intercept_scaling=1,max_iter=1000,multi_class='ovr',
                        penalty='l1',random_state=None, tol=0.0001,
                        verbose=0)
classifier2.fit(trainingData,trainingTarget)
classifier2.score(testing[0],testing[1])

#Performance when C = 10
classifier3 = LinearSVC(C=10,class_weight=None,dual=False,fit_intercept=True,
                        intercept_scaling=1,max_iter=1000,multi_class='ovr',
                        penalty='l1',random_state=None, tol=0.0001,
                        verbose=0)
classifier3.fit(trainingData,trainingTarget)
classifier3.score(testing[0],testing[1])

#Performance when C = 100
classifier4 = LinearSVC(C=100,class_weight=None,dual=False,fit_intercept=True,
                        intercept_scaling=1,max_iter=1000,multi_class='ovr',
                        penalty='l1',random_state=None, tol=0.0001,
                        verbose=0)
classifier4.fit(trainingData,trainingTarget)
classifier4.score(testing[0],testing[1])
