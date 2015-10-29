#!/usr/bin/env python

# This program is part of the Kaggle Competition: How much did it rain
# Main entry of the program

import sys
import numpy as np

#Load training data
train = np.genfromtxt('data/train.csv.gz',dtype=float,delimiter=',',skip_header=1)


