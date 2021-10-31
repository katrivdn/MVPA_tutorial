#!/usr/bin/env python
# coding: utf-8

# # Whole brain MVPA
# This sample script will perform a whole-brain MVPA. ADD SOME MORE ON WHOLE BRAIN MVPA HERE. 

# In[1]:


# import necessary modules
import nilearn
import os
import numpy as np

from nilearn import datasets ## this can be removed when performing your own MVPA (just imports sample data)

# import data
subjects_id = ['01','02','03','04'] # insert list of subjects
fmri_path   = datasets.fetch_haxby(subjects=[int(i) for i in subjects_id]).func ## replace path with own data (*)

#(*) if in BIDS format: 
#path_to_BIDS = r'S:\bbl\NTR\NEAR_BIDS' ## replace with path to BIDS
#path_to_subj = [path_to_BIDS+'\sub-'+sub+'\\func' for sub in subjects_id] ## this will create a list with the path to each subj
#functional   = [f for file in [os.listdir(sub) for sub in path_to_subj] for f in file if 'sub' and 'bold' in f]
#fmri_path    = [path + '\\'+file for path, file in zip(np.repeat(path_to_subj,len(functional)/len(subjects_id)),functional)]

print('These files will be loaded:');print(*fmri_path,sep='\n')

# 



