# Welcome to this notebook!

This notebook gives a rough overview for using multivoxel pattern analysis. (+ more explanation of how the notebook is structured and what you can find in it // change the resources as well)

<div class="alert alert-block alert-warning">
<b>!Warning! Your data should already be pre-processed before performing MVPA.</b> Nilearn provides only basic pre-processing steps - pre-processing your data using other programs (e.g. fmri-prep, FSL...) is highly recommended. Pre-processed data does not have to be smoothed (whether it is preferable or not is still debated; but if having the choice: do not smooth your data).
</div>

If you want to know more about MVPA generally, you can use the following resources:

Textbooks:
- *Principles of fMRI* by Lindquist & Wager (you can also check their course on Coursera - the principles of fMRI 2 gives an overview of MVPA)
- *Handbook of functional MRI* by Poldrack, Mumford and Nichols (you can also check Mumford's [YouTube channel](https://www.youtube.com/c/mumfordbrainstats))

For using Python in general to analyze fMRI data (including using MVPA): 
- https://dartbrains.org/content/Intro_to_Neuroimaging.html
- https://lukas-snoek.com/NI-edu/index.html

A very good tutorial to practice MVPA: 
- https://brainiak.org/tutorials/

For implementing searchlight analysis in `NiLearn`:
- https://danjgale.github.io/blog/2019/practical-searchlight/

And if you are new to python, you will see: python's easy! You can check out some courses on [coursera](https://www.coursera.org/courses?languages=en&query=getting%20started%20with%20python&page=1&utm_source=bg&utm_medium=sem&utm_campaign=93-BrandedSearch-ROW&utm_content=93-BrandedSearch-ROW&campaignid=415061741&adgroupid=1209463256217810&device=c&keyword=https%3A%2F%2Fwww.coursera.org%2Fcourses%3Flanguages%3Den&matchtype=b&network=o&devicemodel=&adpostion=&creativeid=&hide_mobile_promo&msclkid=9574d5e1edc510a61561b4972924e789&utm_term=https%3A%2F%2Fwww.coursera.org%2Fcourses%3Flanguages%3Den) - but believe me: once you have the basics, you only need to practice to improve!

Our sample scripts are using the [NiLearn](https://nilearn.github.io/stable/index.html) and [Scikit-learn](https://scikit-learn.org/stable/index.html) Python packages. Check out their webpage if you want to learn more!

```python
from IPython.display import HTML
HTML('<img src="./giphy.gif">')
```
