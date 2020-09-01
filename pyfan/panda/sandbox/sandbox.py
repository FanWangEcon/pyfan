'''
Created on Aug 13, 2018

@author: fan
'''
import logging
import pandas as pd
import numpy as np
import pyfan.amto.json.json as support_json

logger = logging.getLogger(__name__)

cols = 5
rows = 20
np.random.seed(123)
data = (np.random.rand(rows, cols) - 0.5) * 100

df = pd.DataFrame(data, columns=['col' + str(ctr) for ctr in range(cols)])
winsor_coln_list = ['col0', 'col1', 'col3', 'col4']
coln_perc_cutoffs = {'col0': {'q_ge': 0, 'q_le': 0.9, 'v_ll': 10},
                     'col1': {'q_ge': 0.30, 'v_le': 50},
                     'col3': {'q_ge': 0.01, 'q_le': 0.60, 'v_ll': 40},
                     'col4': {'q_ge': 0.01, 'q_le': 1, 'v_ll': 33, 'v_gg': -5}}

return_type = 'winsorize'
# return_type = 'cutsubset'


'''
Deep copy original dataframe
'''
condi_ctr = 0
for winsor_coln in winsor_coln_list:
    col_perc_cutoff_dict = coln_perc_cutoffs[winsor_coln]

    '''
    Initialize cut min max
    '''
    winsorize_upper = np.Inf
    winsorize_lower = np.NINF

    '''
    Loop over all min and max conditions, including value and percentile conditions
    '''
    for key, val in col_perc_cutoff_dict.items():
        '''
        Current data series
        '''
        df_col = df[winsor_coln]

        '''
        Obtain Thresholds
        '''
        if ('q_' in key):
            '''
            Quantiles
            '''
            threshold = df_col.quantile(val)
        elif ('v_' in key):
            '''
            levels
            '''
            threshold = val
        else:
            raise ('did not find _q quantile or _v value in key')

        '''
        Generate conditions
        '''
        if ('_l' in key):
            winsorize_upper = np.minimum(winsorize_upper, threshold)
            if ('_le' in key):
                if_condi = (df_col <= threshold)
            elif ('_ll' in key):
                if_condi = (df_col < threshold)
            else:
                raise ('key:' + key + ', is invalid')

        elif ('_g' in key):
            winsorize_lower = np.maximum(winsorize_lower, threshold)
            if ('_ge' in key):
                if_condi = (df_col >= threshold)
            elif ('_gg' in key):
                if_condi = (df_col > threshold)
            else:
                raise ('key:' + key + ', is invalid')

        else:
            raise ('key:' + key + ', is invalid')

        '''
        Combine Conditions
        '''
        if (condi_ctr == 0):
            if_condi_all = if_condi
        else:
            if_condi_all = if_condi_all & if_condi
        condi_ctr = condi_ctr + 1

    '''
    Winsorize
    '''
    if (return_type == 'winsorize'):
        df[winsor_coln] = df_col.clip(lower=winsorize_lower, upper=winsorize_upper)

'''
Cut to data subset
'''
if (return_type == 'cutsubset'):
    df_return = df[if_condi_all]
    print(df_return)
    support_json.jdump(df_return.to_dict(), 'conditions:' + str(if_condi_all),
                       logger=logger.debug, print_here=True)

if (return_type == 'winsorize'):
    print(df)
    support_json.jdump(df.to_dict(), 'winsorized',
                       logger=logger.debug, print_here=True)
