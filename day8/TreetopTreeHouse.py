import numpy as np
import pandas as pd
input = open("day8/inputtest.txt", "r")
# input = open("day8/input.txt", "r")

raw =[]
with open('day8/inputtest.txt',"r") as f:
    for l in f:
        raw.append(l.split())
data = pd.DataFrame(raw, columns = ['row', 'column', 'value'])
data_ind = data.set_index(['row','column']).unstack('column')
np.array(data_ind.values, dtype=int)

