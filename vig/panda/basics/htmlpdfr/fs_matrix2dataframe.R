## ----global_options, include = FALSE----------------------------------------------------------
try(source("../../../.Rprofile"))


## import numpy as np

## import pandas as pd


## # Concatenate to matrix

## mt_abc = np.column_stack(np.random.randint(10, size=(5, 3)))

## # Matrix to data frame with columns and row names

## df_abc = pd.DataFrame(data=mt_abc,

##             index=[ 'r' + str(it_col) for it_col in np.array(range(1, mt_abc.shape[0]+1))],

##             columns=[ 'c' + str(it_col) for it_col in np.array(range(1, mt_abc.shape[1]+1))])

## # Print

## print(df_abc)

