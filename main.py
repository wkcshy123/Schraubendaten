import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly 
sns.set()
Data = pd.read_csv('DataRUB.csv')
prozess_zustand = pd.read_csv('prozess_zustand.csv')


def arrayzerlegen(array):
    b = []
    tast = False
    j = -1
    for i, item in enumerate(array):
        if i == array.__len__()-1:
            break
        if item == 0 and array[i+1] == 1:
            tast = True
            b.append([])
            j += 1
        elif item == 1 and array[i+1] == 0:
            tast = False

        if tast:
            b[j].append(i+1)
    return b


prozesslist = arrayzerlegen(prozess_zustand.iloc[:, 0].tolist())
prozess_length_list = [x.__len__() for x in prozesslist]

prozess_length_list = np.array(prozess_length_list)
sns.distplot(prozess_length_list)
plt.show()


e = []
for item in prozesslist:
    if np.percentile(prozess_length_list, 10) <= item.__len__() <= np.percentile(prozess_length_list, 99):
        e.append(item)


_, axes = plt.subplots()



