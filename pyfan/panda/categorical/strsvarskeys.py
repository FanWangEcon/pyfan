'''
Created on Aug 9, 2018

@author: fan

Store key variable names, file names, etc. 

Individual analysis files should refer to this file. 
'''
import logging
import pyfan.panda.categorical.catevars as tool_catevars

logger = logging.getLogger(__name__)


def main_data_directory(dataset_name='thai_data_z'):
    if (dataset_name == 'thai_data_z'):
        # this means I am running my home windows machine
        data_directory = 'C:/Users/fan/Documents/Dropbox (UH-ECON)/Project_Nguyen_Townsend_Wang_ThaiFinChoice/data_month160/'

    return data_directory


def file_names():
    data_z = {'filename': 'thaiMthly_Annulized_DataZ',
              'format': 'stata',
              'format_suffix': '.dta'}
    file_names_dict = {'thai_data_z': data_z}

    return file_names_dict


def var_names(vartype=1,
              file_name='thaiMthly_Annulized_DataZ',
              out_type='coln'):
    if (file_name == "thaiMthly_Annulized_DataZ"):
        vars_d = {'Y': ['hy_agg_IS_07', 'Income'],
                  'K': ['hy_agg_BS_09_1st', 'Capital'],
                  'B': ['B_i_y', 'Net Asset'],
                  'provid': ['id_p', 'province'],
                  'provid_num': ['id_p_num', 'province'],
                  'year': ['ts_yrr', 'calendar year']}

    if (out_type == 'coln'):
        vars_coln = {var_key: vars_val[0] for var_key, vars_val in vars_d.items()}
        return vars_coln

    if (out_type == 'desc'):
        vars_desc = {var_key: vars_val[1] for var_key, vars_val in vars_d.items()}
        return vars_desc


def conditions(df, condi_dict=None, return_subset=False):
    """Commonly used conditionings
    
    Can combine conditioning statements together in list
    
    Parameters
    ----------
    condi_dict: dictionary
        condi_dict = {'region':'central', 'years':2002-2005}
    file_name: string
        different files could have different variable names for the same variables,
        although these should be unified if possible
    """

    vars_d = df.vars_c

    '''
    1. Define Conditioning Functions
    '''

    def condi_region(region):
        #     {
        #         "0": "Chachoengsao (Central)",
        #         "1": "Buriram (NE)",
        #         "2": "Lopburi (Central)",
        #         "3": "Sisaket (NE)"
        #     }
        cates_dict = tool_catevars.show_cates(df, vars_d['provid_num'])
        if (region.lower() == 'central' or region.lower() == 'ne'):
            if_condi = ((df[vars_d['provid_num']] == cates_dict[0]) | (df[vars_d['provid_num']] == cates_dict[2]))
        if (region.lower() == 'northeast' or region.lower() == 'ne'):
            if_condi = ((df[vars_d['provid_num']] == cates_dict[1]) | (df[vars_d['provid_num']] == cates_dict[3]))
        return if_condi

    def condi_year(year_range):
        if '-' in year_range:
            year_min_max = year_range.split('-')
            year_min = int(year_min_max[0])
            year_max = int(year_min_max[1])
        if_condi = ((df[vars_d['year']] >= year_min) & (df[vars_d['year']] <= year_max))
        return if_condi

    for ctr, (condi_key, condi_val) in enumerate(condi_dict.items()):
        if (condi_key == 'region'):
            if_condi = condi_region(condi_val)
        if (condi_key == 'year'):
            if_condi = condi_year(condi_val)

        if (ctr == 0):
            if_condi_all = if_condi
        else:
            if_condi_all = if_condi_all & if_condi

    if (return_subset):
        '''
        return subset of data with conditioning imposed
        '''
        return df[if_condi_all]
    else:
        '''
        return just the conditioning
        '''
        return if_condi_all
