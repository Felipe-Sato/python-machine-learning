from sklearn.datasets._samples_generator import make_blobs
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC

X, y = make_blobs(n_samples=200, centers=2, cluster_std=0.60, random_state=0)

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=20, random_state=0)

plt.scatter(train_X[:, 0], train_X[:, 1], c=train_y, cmap='winter')
