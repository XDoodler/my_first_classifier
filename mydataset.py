import numpy as np
import csv
from sklearn.datasets.base import Bunch
import matplotlib.pyplot as plt
from sklearn import tree
def load_my_fancy_dataset():
    with open('Jobs.csv') as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0]) #14
        n_features = int(temp[1]) #2
        
        features = np.empty((n_samples,n_features), dtype=np.float32)
        labels = np.empty((n_samples), dtype=np.int)
        male_c=1;
         
        for i, sample in enumerate(data_file):
            features[i] = np.asarray(sample[:-1], dtype=np.float32)
            if(male_c%2==0):
                 plt.plot([sample[0:1]],[sample[1:2]],'bo')
                 male_c=male_c+1
            else:
                 plt.plot([sample[0:1]],[sample[1:2]],'ro')
                 male_c=male_c+1
            labels[i] = np.asarray(sample[-1], dtype=np.int)

        
           
            
    return Bunch(features=features, labels=labels, plot=plt)
    




