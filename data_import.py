# Read and import the reaction rate constant here 
import pandas as pd
import numpy as np

def import_data():
    i_data_read = pd.read_csv(('Reaction-rate-constant.csv'))
    i_data_k1 = i_data_read[["k1 (day-1)"]].to_numpy()
    i_data_k2 = i_data_read[["k2 (day-1)"]].to_numpy()

    d_len = len(i_data_read)

    r_data_k1 = np.zeros(d_len)
    r_data_k2 = np.zeros(d_len)

    for i in range(d_len):
        r_data_k1[i] = i_data_k1[i]
        r_data_k2[i] = i_data_k2[i]
        
    return d_len, r_data_k1, r_data_k2
    



