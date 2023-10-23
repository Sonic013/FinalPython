import pandas as pd

from numpy import int8
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
dumm = pd.DataFrame()
for column in data.columns:
  for unique_value in data[column].unique():
    dumm[column + '_' + unique_value] = (data[column] == unique_value).astype(int8)
print(dumm)
