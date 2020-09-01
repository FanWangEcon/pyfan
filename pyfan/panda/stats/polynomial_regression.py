'''
Created on Sep 23, 2018

@author: fan
'''


import logging
import pyfan.amto.json.json as support_json

import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

logger = logging.getLogger(__name__)


def ols_formula(df, dependent_var, *excluded_cols):
    '''
    Generates the R style formula for statsmodels (patsy) given
    the dataframe, dependent variable and optional excluded columns
    as strings
    '''
    df_columns = list(df.columns.values)
    df_columns.remove(dependent_var)
    for col in excluded_cols:
        df_columns.remove(col)
        
    return dependent_var + ' ~ ' + ' + '.join(df_columns)


def tester():
#     df = sm.datasets.get_rdataset("Guerry", "HistData").data
#     print(df.columns)
#     df = df[['Lottery', 'Literacy', 'Wealth', 'Region']].dropna()

    folder = 'C:/Users/fan/Documents/Dropbox (UH-ECON)/Project Dissertation EC2/thaijmp201809j8vara/esti/c_20180918_ITG_list_tall_mlt_ce1a2/'
#     file_base = 'c_20180918_ITG_list_tall_mlt_ce1a2'
    file_base = 'c_20180918_ITG_list_tall_mlt_ce1a2_modelsimu_regress'
    file = file_base + '.csv'
    
    file_path = folder + file
    df_use = proj_sys_sup.read_csv(csv_file_folder=file_path)
    df_use_columns = df_use.columns.tolist()
    support_json.jdump((df_use.columns).tolist(), 'df_use.columns', logger=logger.warning)
    
    
    poly = PolynomialFeatures(2)
#     df_inter = poly.fit_transform(df_use[['esti_param.BNF_SAVE_P_ce9901', 'esti_param.BNF_BORR_P_ce0209']])
    
    columns_rhs = []
    for columns in df_use.columns:
        if ('esti_obj' in columns):
            pass
        elif ('_ce0209' in columns):
            pass
        else:
            columns_rhs.append(columns)
    
    support_json.jdump((columns_rhs), 'columns_rhs', logger=logger.warning)
    support_json.jdump((len(columns_rhs)), 'len(columns_rhs)', logger=logger.warning)        
    
    '''
    if 13 + 1 (constant) rhs, this should be 105 terms for poly(2)
    half matrix = (14*14 - 14)/2 + 14
    '''
    
    X = poly.fit_transform(df_use[columns_rhs])
    y = df_use['esti_obj.main_allperiods_obj']
    est = sm.OLS(y, X).fit()
    
    
    print(est.summary())
    
    
    
    
#     mod = smf.ols(formula='Lottery ~ .', data=df)
#     res = mod.fit()
#     print(res.summary())
    
#     support_json.jdump(df.head().values().tolist(), 'df.head()', logger=logger.warning)
    
    
if __name__ == '__main__':
    
    FORMAT = '%(filename)s - %(funcName)s -\n %(asctime)s - %(levelname)s  - %(message)s'
    FORMAT = '%(funcName)s - %(asctime)s - %(levelname)s  - %(message)s'
    FORMAT = '%(filename)s - %(funcName)s - %(lineno)d -  %(asctime)s - %(levelname)s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    tester()
    
    
    
    
    