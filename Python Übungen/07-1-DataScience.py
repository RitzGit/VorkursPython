# Aufgabe:  Data Science mit diesen Daten
from typing import List, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

reale_teilnehmeranzahl = [( '2020-10-12', 210) , ('2020-10-13', 180) ,
                    ('2020-10-14', 180) , ('2020-10-15', 165) ,
                    ('2020-10-16', 160) , ('2020-10-19', 165) ,
                    ('2020-10-20', 155) , ('2020-10-21', 150 ) ,
                    ('2020-10-22', None ) , ('2020-10-23', None )]


teilnehmeranzahl = [( '2020-10-12', 210) , ('2020-10-13', 180) ,
                    ('2020-10-14', 180) , ('2020-10-15', 165) ,
                    ('2020-10-16', 160) , ('2020-10-19', 165) ,
                    ('2020-10-20', 155) , ('2020-10-21', None ) ,
                    ('2020-10-22', None ) , ('2020-10-23', None )]

def daily_lost(stats: List[Tuple[str, int]]) -> List[float]:
    changes = []

    for i in range(len(stats) - 1):
        now = stats[i]
        tomorrow = stats[i+1]

        if now[1] != None and tomorrow[1] != None:
            changes.append( ( 1 - ( tomorrow[1]/now[1] ) ) )

    return changes

def give_statistics(stats: np.array) -> str:
    response  = ""
    response += f'Minimum: {np.min(stats):.3f}\n'
    response += f'Maximum: {np.max(stats):.3f}\n'
    response += f'Standardabweichung: {np.std(stats):.3f}\n'
    response += f'Durchschnitt: {np.average(stats):.3f}'
    return response

def get_panda(data: List[Tuple[str, int]]) -> pd.DataFrame:

    pd_teilnehmeranzahl = pd.DataFrame(data, columns= ['datum', 'anzahl'])
    return pd_teilnehmeranzahl

def plot_panda(data: pd.DataFrame):
    plt.style.use('seaborn-whitegrid')
    plt.bar(data.datum, data.anzahl, align='center', alpha=0.8)
    plt.show()

def extrapolate(data1: pd.DataFrame, loss: np.array) -> pd.DataFrame:
    data2 = data1.copy()
    for i in range(len(data2['anzahl'])):
        if pd.isna(data2['anzahl'][i]):
            data2['anzahl'][i] = int(data2['anzahl'][i-1] * (1 - np.average(loss)))
    return data2

def plot_extra(real: pd.DataFrame, extra: pd.DataFrame):
    plt.plot(real.datum, real.anzahl)
    plt.plot(extra.datum, extra.anzahl)
    plt.show()

percent_loss = daily_lost(teilnehmeranzahl)
percent_loss = np.array(percent_loss, dtype='float32')

#print(plot_panda(get_panda(teilnehmeranzahl)))

plot_extra(extrapolate(get_panda(teilnehmeranzahl), percent_loss), get_panda(reale_teilnehmeranzahl))