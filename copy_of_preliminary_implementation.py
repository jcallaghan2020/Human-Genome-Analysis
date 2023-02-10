# -*- coding: utf-8 -*-
"""Copy of Preliminary_Implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kt3K4OsEv2_B_PSefQVVzmbcW6uYN3vW

# Guide

* **IMPORTS:**

Not all of the imports are neccesary, but it's best not to play around with it. It includes a bunch of regularly used python files, such as numpy and scypi, which may get used without even thinking about it.

The import of interest are scikit-allel, which allows us to read the allel files very easily.

BIG NOTE: There are THREE things you MUST do in order for the code to work.
1. Save a copy to your drive
2. Put that copy inside a folder "Colab Notebooks"
(this may happen automatically, and is best practice)
3. Save the test_sample.vcf to the same folder 
(idk how to attatch it here, so just look for it in the emails somewhere)

* **FUNCTIONS**:

These are all the functions I use throughout the program. I explain what they do a few times throughout the code, but I'll summarize them here:

1. graph_lines

Basically what's on the tin. It takes in a list of values, and graphs them in a basic bar plot. It also optionally takes in a begining value, an end value, and a minimum line. Hense making this function good for debugging and testing.

2. test_below

Takes in a list of values, and finds values that are close to each other that are under a certain given number. 

3. imshow_display

The best thing I could figure out for a display. Not very readable. Why it's called imshow, idk.

* **USELESS FUNCTIONS**

They're useless and we don't like them. 

1. Useless 1 displays the 0 axis which doesn't matter

2. Useless 2 displays what imshow does but incomprehensibly


BIG NOTE: This is a useless and confusing correction which is why I'm putting it here. Some values have "test" in the name, but that's because they're testing for a certain response, not because they're to-be-replaced with better names. Doesn't change anything, but I figured I'd put the clarification somewhere just in case.

* **MAIN CODE**

The place where stuff happens. Contains two ready examples of code function so far. Feel free to play around. 

Colab contains a built-in window where you can play around with things without officially changing the code, but I find it fiddly and hard to use, so I included an experimentation zone below.

BIG NOTE: If you need a new place to put code, or just generally want to make things nicer, you can add code block/section/area thingys and text area thingys by hovering on the line at the bottom of the box. You should see something that says "+ code | + text"

# Imports
"""

# Commented out IPython magic to ensure Python compatibility.
# Imports
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from __future__ import division
import seaborn as sns
sns.set(style='ticks', palette='Set2')
# %matplotlib inline


# import scikit-allel
!pip install scikit-allel
import allel
# check which version is installed
print(allel.__version__)


import os

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')


test_sample = allel.read_vcf('/content/drive/MyDrive/test_sample (1).vcf')

"""# Functions"""

def graph_lines(list_vals, start = 0, end = 0, line = 0):
  """ 
    a graph to look for things visually while testing, to help with
    debugging . red = start, blue = end, orange = value (eg mean)
  """
  x = range(len(list_vals))
  line = [line for i in x]
  plt.plot(x, list_vals, linewidth=0.1)
  plt.plot(x, line)

  # start and end of list of places where genotypes are abnormal
  plt.axvline(x = start, color = 'blue')
  plt.axvline(x = end, color = 'red')

  # titles
  plt.xlabel("heterozygous count")
  plt.ylabel("number of heterozygous pairs")
  plt.title('Anomaly Detection Using Heterozygous Count Average')

  # makes the image way bigger
  fig = plt.gcf()
  fig.set_size_inches(18.5, 10.5)
  fig.savefig('test2png.png', dpi=100)


  plt.show()

def test_below(list_vals, test_val):
  """ this is the thingy that detects anomalies based on test_val (mean, median, etc.)
  # for loop that goes through axis 1 and sees if there are at least 100 instances
  # in a row where the heterozygous count dips below the given value (eg. mean)
  # (measured with "must_be" as in "must_be > 100")
  # skips ten values so we can see a wider range of values that fit the requirement
   (has not been reworked for effeciency)"""
  test_display_list = []
  j = 0;
  must_be = 0
  skip = 0
  i = 0

  # loop through axis 1 (count of rows)
  for i in list_vals:

    # if i is less than the average, note this in must_be
    # if there aren't 100 less than average in a row, restart must_be
    # except we also skip a few for a wider range
    if (i <= test_val):
      must_be = must_be+1
    elif (skip >= 5):
      must_be = 0
      skip = 0
    else:
      skip = skip + 1
    
    if (must_be == 50):
      j = j - 50

    # if there is 100 in a row, note this in an array of indexes
    if (must_be > 50):
      test_display_list.append(j)
    j = j+1

  return test_display_list

def imshow_display(test_list, start, end):
  # gets a bool of where the values inside the given list are hz
  test_display_bool = gt_test[test_list].is_het()

  # displays this with imshow (more about imshow \/ \/ \/)
  # https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.imshow.html
  plt.imshow(test_display_bool, aspect='equal')

  # names n stuff
  plt.title("Heterozygeous Values")

  # makes the image way bigger
  fig = plt.gcf()
  fig.set_size_inches(18.5, 10.5)
  fig.savefig('test2png.png', dpi=100)

  # displays plot
  plt.show()

def get_step(genotypeArray, stepCount):
  # gets the step count of gt_test (eg: [1,2,3,4,5] step 2 = [2, 4])
  return genotypeArray[::stepCount]

"""# Useless Functions"""

# this ended up not being super helpful but keeping it here in case we need it

def graph_ac(ac):
  """ 
    a big ol graph to look for things visually while testing, to help with
    debugging 
  """
  y = [row[1] for row in ac]
  x = range(len(y))
  plt.plot(x, ac, linewidth=0.1)
  plt.plot(x, y)


  # makes the image way bigger
  fig = plt.gcf()
  fig.set_size_inches(18.5, 10.5)
  fig.savefig('test2png.png', dpi=100)


  plt.show()

# useless smh
def temp_display(test_display_bool):
  """
    Temporary display thing based on boolean 2d array until we find smth cooler
  """
  i = j = 0
  while i < len(test_display_bool):
    while j < len(test_display_bool[0]):
      if (test_display_bool[i][j] == True):
        print('⬜', end='')
      else:
        print('⬛', end='')
      j = j+1
    print()
    j = 0
    i = i+1

"""# Main Code"""

gt_test = allel.GenotypeArray(test_sample['calldata/GT'])


# gets the step count of gt_test (eg: [1,2,3,4,5] step 2 = [2, 4])
gt_test = get_step(gt_test, 3)

# this is the count of heterozygeous (hz) files in the fileset
het_count = gt_test.count_het(axis=1)

### EXAMPLE of how code works with mean values
test_mean = np.mean(het_count)

# looks at hz count and finds a concurrent list of values that go below the mean
test_mean_list = test_below(het_count, test_mean)

# graphs the lines where that list starts and ends, and the actual mean line
# (the only required value in this graph is the hz count)
# (used for debugging)

#graph_lines(het_count, line=test_mean, 
#            start=test_mean_list[0], end=test_mean_list[-1])



# displays something that looks cool and good to the user
imshow_display(test_mean_list, start=test_mean_list[0], end=test_mean_list[-1])

### EXAMPLE of how code works with median values
test_med = np.median(het_count)

# looks at hz count and finds a concurrent list of values that go below the mean
test_med_list = test_below(het_count, test_med)
print(test_med_list)

# graphs the lines where that list starts and ends, and the actual mean line
# (the only required value in this graph is the hz count)
# (I only put the optional line value as a different example of how the code could run)
# (very useful for debugging)
plt.xlabel("heterozygous count")
plt.ylabel("number of heterozygous pairs")
plt.title('Anomaly Detection Using Heterozygous Count Median')
graph_lines(het_count, line=test_med, start=test_med_list[0], end=test_med_list[-1])


# displays something that looks cool and good to the user
imshow_display(test_med_list, start=test_med_list[0], end=test_med_list[-1])

## EXPERIMENTATION ZONE