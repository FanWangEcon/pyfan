'''
Created on Aug 9, 2018

@author: fan

Generate mean, and variance covariance of key state variables from data
'''
import logging
import numpy as np

logger = logging.getLogger(__name__)


def gen_mean(df, mean_var_list,
             short_mean_var_list=None,
             group_by_var_list=None,
             conditioning=None):
    if (short_mean_var_list == None):
        short_mean_var_list = mean_var_list

    '''
    Generate the means of a number of variables
    '''
    if (conditioning is not None):
        df_subset = df[conditioning]
    else:
        df_subset = df

    if (group_by_var_list is not None):
        means = df_subset.groupby(group_by_var_list)[mean_var_list].mean()
    elif (group_by_var_list is None):
        means = df_subset[mean_var_list].mean()

    means.info = {}
    means.info['obs'] = len(df_subset)
    means.info['means'] = {var_short: means[var] for var, var_short in zip(mean_var_list, short_mean_var_list)}

    return means


def gen_varcov(df, varcov_var_list,
               short_varcov_var_list=None,
               group_by_var_list=None,
               conditioning=None):
    if (short_varcov_var_list is None):
        short_varcov_var_list = varcov_var_list

    if (conditioning is not None):
        df_subset = df[conditioning]
    else:
        df_subset = df

    if (group_by_var_list is not None):
        varcov = df_subset.groupby(group_by_var_list)[varcov_var_list].cov()
    else:
        subset = df_subset[varcov_var_list]
        varcov = subset.cov()

    varcov.info = {}
    varcov.info['obs'] = len(df_subset)
    varcov.info['variance'] = {var_short: varcov[var][var] for var, var_short in
                               zip(varcov_var_list, short_varcov_var_list)}
    varcov.info['sd'] = {var_short: np.sqrt(varcov[var][var]) for var, var_short in
                         zip(varcov_var_list, short_varcov_var_list)}

    return varcov
