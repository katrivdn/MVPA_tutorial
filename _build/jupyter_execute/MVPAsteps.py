#!/usr/bin/env python
# coding: utf-8

# # How to perform Multivoxel Pattern analysis
# Just like any statistical technique, MVPA is 'just' a tool - there are many many ways in which you can use it; the best way to use it really depends on your research question. Most of the time, it's best to even use it in several ways to check if the pipeline you are using does not bias your results! 
# 
# We will here first go through the basic steps involved when doing MVPA. These include: feature selection, choosing a classifier, training and testing the classifier and finally examining the results. (+ I also want to put something about whole brain decoding, ICA, searchlight etc. but I'm not sure of how i'll do this... maybe another section that focusses more closely on each...? + then add some code?)

# ## Feature selection
# Once you have **pre-processed** your data - *this is really important!* - you can (and preferably should) do feature selection (although we will demonstrate here as well how you can use the pre-processed raw data to perform MVPA). 
# 
# **Why do feature selection?** fMRI data typically has (much!) more features (= voxels) than outcomes (= experimental conditions typically, or groups etc.). This problem is called the ['curse of dimensionality'](https://www.youtube.com/watch?v=DyxQUHz4jWg) which will make it super hard for our model to classify succesfully! 
# 
# That being said, MVPA can be applied on raw data - but the accuracy of your model will typically be lower compared to a model in which feature selection is applied. 
# 
# Feature selection can be done by:
# - subselecting a range of voxels (like in using an ROI)
# - using beta-maps for each trial/condition
# - performing an ICA or a PCA
# - averaging the brain activity for one condition/block
# - ... 

# 
# ## Choosing a classifier

# ## Training and testing the classifier

# ## Examining the results
