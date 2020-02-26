# -*- coding: utf-8 -*-
"""
Spyder Editor

Divorce Model
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import pickle

# https://dergipark.org.tr/en/download/article-file/748448, p. 266
# Using features, 2, 6, 11, 18, 26, 40 are the most effective

divorce_data_optimized = pd.read_csv('divorce_optimized.csv')

X = divorce_data_optimized.iloc[:, :-1]
y = divorce_data_optimized.iloc[:, -1]

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

from sklearn.ensemble import RandomForestClassifier

RFC = RandomForestClassifier()
RFC.fit(X_train, Y_train)

print('rfc', RFC.score(X_test, Y_test))

pickle.dump(RFC, open('model.pkl', 'wb'))


