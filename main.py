import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

fig = make_subplots(rows=3, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.02)
fig.add_trace(go.Scatter(y=Data['/Nck/MachineAxis/actToolBasePos'], mode='lines', name='/Nck/MachineAxis/actToolBasePos'), row=1, col=1)
fig.add_trace(go.Scatter(y=Data['/Channel/State/progStatus'], mode='lines', name='/Channel/State/progStatus'), row=2, col=1)
fig.add_trace(go.Scatter(y=prozess_zustand.iloc[:, 0].tolist(), mode='lines', name='Zustand(1: aktiv, 0: non-aktiv)'), row=3, col=1)
fig.write_html(
        "gesamt.html")
del fig

for i, prozess in enumerate(e):
    data_prozess = Data.iloc[e[i][0]:e[i][-1], :]
    fig = make_subplots(rows=3, cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.02)
    fig.add_trace(
        go.Scatter(y=data_prozess['/Nck/MachineAxis/actToolBasePos'], mode='lines', name='/Nck/MachineAxis/actToolBasePos'),
        row=1, col=1)
    fig.add_trace(go.Scatter(y=data_prozess['/Channel/State/progStatus'], mode='lines', name='/Channel/State/progStatus'),
                  row=2, col=1)
    fig.add_trace(
        go.Scatter(y=data_prozess['/Channel/MachineAxis/aaLoad'], mode='lines', name='/Channel/MachineAxis/aaLoad'),
        row=3, col=1)

    fig.write_html(
        "./figure/werkstück_" + str(i) + "_" + str(prozess.__len__()) + ".html")
    del fig




