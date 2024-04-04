import pandas as pd
import os
os.chdir('../')

df = pd.read_csv('Data/qm9.csv')
df = df.sample(n=20000, random_state=25)
df.to_csv('Data/task1.csv', index = False)
