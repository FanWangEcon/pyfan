'''
Created on Aug 9, 2018

@author: fan
'''
import ast
import logging

import pandas as pd
from pandas.io.json import json_normalize

import pyfan.amto.json.json as support_json
import pyfan.panda.categorical.strsvarskeys as strvarskeys
import pyfan.util.inout.exportpanda as exportpanda

logger = logging.getLogger(__name__)
import shutil


def unflatten_denormalize(dictionary=None, dump_print=False):
    """https://stackoverflow.com/questions/6037503/python-unflatten-dict
    json_normalize results in dict that has dots for nests
    revert back
    
    Examples
    --------
    import panda.io.readexport as readexport
    dictionary = {}
    nested_dict = readexport.unflatten_denormalize(dictionary)
    """
    if (dictionary is None):
        dictionary = \
            {"esti_obj.main_allperiods_obj": 2161.704787809504,
             "data_model": "model",
             "P_jp_j.6.105": 0.35338853785616764,
             "P_jp_j.6.3": 0.08513942723795298,
             "data_param.A": -0.03125,
             "data_param.Region": 0,
             "data_param.Region_set": "[0, 1]",
             "data_param.Year": 0,
             "data_param.Year_set": "[0, 1]",
             "data_param.std_A": 0,
             "esti_obj.main_obj": 1321.7653586006118,
             "esti_obj.subsets_main.agg_prob_for": 6.551240600950623,
             "esti_obj.subsets_main.agg_prob_none": 0.01444353749392462,
             "esti_obj.subsets_main.equi_BI": 1246.3358962825505,
             "support_arg.workers": 1,
             "title": "kappa_ne0209=0.51150.2955:(INF BORR+SAVE)+(0MIN,0FC)+(LOG,Angeletos)BNF_BORR_P-0.500;BNF_SAVE_P-0.300;BNI_BORR_P-0.100;BNI_LEND_P-2.000;R_FORMAL_BORR-1.061;R_FORMAL_SAVE-1.011;R_INFORM_BORR-1.279;R_INFORM_SAVE-1.279;kappa-0.296;kappa_ne0209-0.296;kappa_ne9901-0.511 (g:basic, e:zeroFE, e:Angeletos, e:0,1,102,3,104,105,6, i:forgegeom)",
             "y_opti_grid_allJ_agg_var": 5.9793820314678605,
             "interpolant.interp_type": "['forgegeom']"
             }

    nested_dict = dict()
    for key, value in dictionary.items():
        parts = key.split(".")
        d = nested_dict
        for part in parts[:-1]:
            if part not in d:
                d[part] = dict()
            d = d[part]
        if (isinstance(value, str) and value.startswith('[')):
            d[parts[-1]] = ast.literal_eval(value)
        else:
            d[parts[-1]] = value

    if (dump_print):
        support_json.jdump(nested_dict, 'resultDict',
                           logger=logger.debug, print_here=True)

    return nested_dict


def read_stata(file_directory_name):
    df = pd.read_stata(file_directory_name)

    return df


def read_file(file_key='thai_data_z'):
    data_directory = strvarskeys.main_data_directory()

    file_names_dict = strvarskeys.file_names()
    data_z_strs = file_names_dict[file_key]

    z_df = read_file_main(file_name=data_z_strs['filename'],
                          format_suffix=data_z_strs['format_suffix'],
                          directory=data_directory,
                          data_format=data_z_strs['format'])

    return z_df


def read_csv(csv_file_folder):
    """
    directory = 'C:/Users/fan/Documents/Dropbox (UH-ECON)/Project Dissertation/model_test/test_solu/'
    param_combo = '20180701_basicJ7_basic'
    file_name = 'solu_'+param_combo+'.csv'
    csv_file_folder = directory + '/' + file_name
    solu_opti_pd = proj_sys_sup.read_csv(csv_file_folder)
    """
    return pd.read_csv(csv_file_folder)


def read_file_main(file_name, format_suffix, directory, data_format='stata', show_columns=True):
    if (data_format == 'stata'):
        if (directory.endswith('/')):
            file_full = directory + file_name + format_suffix
        else:
            file_full = directory + '//' + file_name + format_suffix
        panda_df = read_stata(file_full)

    if (show_columns):
        support_json.jdump(list(panda_df.columns.values),
                           'list(z_df.columns.values)',
                           logger=logger.info,
                           print_here=True)

    panda_df.file_name = file_name
    panda_df.directory = directory
    panda_df.data_format = data_format
    panda_df.vars_c = strvarskeys.var_names(file_name=file_name, out_type='coln')
    panda_df.vars_d = strvarskeys.var_names(file_name=file_name, out_type='desc')

    return panda_df


def dict_to_panda(list_of_dict, save_file_directory=None):
    panda_df = json_normalize(list_of_dict)
    logger.info('panda_df\n:%s', panda_df)

    if (save_file_directory is not None):
        exportpanda.saveCSV(saveFileDirectory=save_file_directory,
                            dataToSave=panda_df,
                            header='',
                            rowindex=False,
                            is_panda=True,
                            replace=True,
                            export=True)

    return panda_df


if __name__ == "__main__":
    unflatten_denormalize(dictionary=None, dump_print=True)
