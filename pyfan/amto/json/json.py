'''
Created on Jun 4, 2018

@author: fan
'''

import logging

logger = logging.getLogger(__name__)

import json
from datetime import date, datetime
import numpy as np


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, (np.int_, np.intc, np.intp,
                        np.int8, np.int16, np.int32,
                        np.int64, np.uint8)):
        return int(obj)
    if isinstance(obj, (np.float_, np.float32)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()

    raise TypeError("Type %s not serializable" % type(obj))


def jdump(aws_return_dict, desc='', logger=None, print_here=False):
    strout = json.dumps(aws_return_dict,
                        indent=4,
                        default=json_serial)

    if (print_here):
        print(desc + ':')
        print(strout)

    if (logger is None):
        '''
        default is info logger if there are no loggers specified
        do not specify anything, otherwise plots things I do not want to plot out
        '''
    else:
        logger(desc + '\n:%s',
               json.dumps(aws_return_dict,
                          indent=4,
                          default=json_serial))

    return strout
