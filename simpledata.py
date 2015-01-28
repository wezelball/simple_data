#!/usr/bin/env python
# Read CSV data into an array
import sys, os
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy import signal
from pylab import *
import sys, getopt

def usage():
    print "Bad usage"

def main(argv):

    # Some vaviables
    filename = ''
    clipping = False
    clipval = 0.0
    
    try:                                
        opts, args = getopt.getopt(argv, "hc:f:", ["help","clip", "file="])
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)
        
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        if opt in ('-c', '--clip'):
            clipping = True
            clipval = float(arg)
        if opt in ('-f', '--file'):
            filename=arg
            print filename

    if filename == "":
        usage()
        sys.exit(2)
    
    # Load the data into dataSet array
    # this will retuen a 2-D array
    dataSet = genfromtxt(filename, dtype=float, usecols = (0, 1), delimiter=' ')
  
    # print some statistics
    #print dataSet.shape
    #print dataSet.size 
    #print dataSet.ndim # number of dimensions
    #print dataSet.dtype.name

    # print 1st line in data set
    #print dataSet[0]
    # print last line in data set
    #print dataSet[-1]
    #print dataSet[0][1]

    # Clip values above a threshold
    if clipping == True:
        np.clip(dataSet, 0, clipval, out=dataSet)
    
    # Split 2D array into 2 1D arrays
    # I still don't understand this slicing shit, but it works
    x = dataSet[:,0]   # the x-axis
    #y = dataSet[:,1:]  # the y-axis
    y = dataSet[:,1:]  # the y-axis
    
    # Test above
    print x[0], y[0]
    print x.shape
    print y.shape

    # Iterate through array, isolating x and y
    #for a,b in dataSet:
        #print a, b

    # Set up filtering
    #b, a = signal.butter(8, 0.125, 'low')
    #y = signal.filtfilt(b, a, dataSet, padlen=150)
    #b, a = scipy.signal.butter(N, Wn, 'low')
    #output_signal = signal.filtfilt(b, a, dataSet)
  

    # Plot the dataset
    plt.plot(x,y)
    plt.show()

if __name__ == "__main__":
   main(sys.argv[1:])