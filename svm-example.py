import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv('Maths.csv', ";")

nFeatures = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason',
             'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
             'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences',
             'G1', 'G2', 'G3']

num_encoded = df.loc[:, nFeatures].values
num_encoded = StandardScaler().fit_transform(num_encoded)
num_encoded = pd.DataFrame(data=num_encoded, columns=nFeatures)

labelFeatures = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason',
             'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
             'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences',
             'G1', 'G2', 'G3']

label_encoded = []
for feature in labelFeatures:
  label_encoded.append(LabelEncoder().fit_transform(df[feature]))
label_encoded = list(zip(*label_encoded))
label_encoded = pd.DataFrame(data=label_encoded, columns=labelFeatures)

x = pd.merge(num_encoded, label_encoded, right_index=True, left_index=True)
y = df.loc[:, ['G1', 'G2', 'G3']].values

targetDataframe = pd.DataFrame(np.mean(df.loc[:, ['G1', 'G2', 'G3']], axis=1), columns=['average'])

