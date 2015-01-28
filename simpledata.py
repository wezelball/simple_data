#!/usr/bin/env python
# Read CSV data into an array
import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy import signal
from pylab import *

# Load the data into dataSet array
dataSet = genfromtxt('./sampledata/smallset.asc', \
                     dtype=float, usecols = (0, 1), delimiter=' ')

# print some statistics
print dataSet.shape
print dataSet.size
print dataSet.ndim
print dataSet.dtype.name

# print 1st line in data set
print dataSet[0]
# print last line in data set
print dataSet[-1]


# Set up filtering
b, a = signal.butter(8, 0.125, 'low')
#y = signal.filtfilt(b, a, dataSet, padlen=150)
#b, a = scipy.signal.butter(N, Wn, 'low')
output_signal = signal.filtfilt(b, a, dataSet)

# Plot the dataset
# plt.plot(dataSet)
plt.plot(y)
plt.show()