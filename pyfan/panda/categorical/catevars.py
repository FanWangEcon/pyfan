'''
Created on Aug 10, 2018

@author: fan
'''

import logging
import pyfan.amto.json.json as support_json

logger = logging.getLogger(__name__)


def show_cates(df, varname):
    dtype_name = df[varname].dtype.name
    if (dtype_name == 'category'):
        cates_dict = dict(enumerate(df[varname].cat.categories))
    else:
        cates_dict = 'not categorical,' + varname + ' is ' + dtype_name

    support_json.jdump(cates_dict, df.file_name + ':' + varname,
                       logger=logger.debug, print_here=True)

    return cates_dict
