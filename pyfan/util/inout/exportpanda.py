'''
Created on Mar 28, 2018

@author: fan
'''

import logging

logger = logging.getLogger(__name__)

import pandas as pd
import os as os
import json

import pyfan.amto.json.json as support_json


def export_history_csv(store, store_map, filepath='', filename='', export=True):
    logger.info('filename:\n%s', filename)
    logger.info('filepath:\n%s', filepath)
    logger.info('store.shape:\n%s', store.shape)

    saveFileDirectory = filepath + filename + '.csv'

    return saveCSV(saveFileDirectory, store, list(store_map.keys()), is_panda=False, export=export)


def saveJSON(saveFileDirectory, data, replace):
    open_str = 'w'
    if (replace):
        open_str = 'w'
    else:
        open_str = 'a'

    with open(saveFileDirectory, open_str) as outfile:
        json_out = json.dump(data, outfile, default=support_json.json_serial)

    return json_out


def saveCSV(saveFileDirectory, dataToSave, header='', rowindex=False,
            is_panda=True, replace=True, export=True):
    'if get permissiond denied error, because possible saveFileDirectory did not have .csv end'

    export_index = False
    if (is_panda == True):
        df = dataToSave
    else:
        df = pd.DataFrame(dataToSave)
        df.columns = header
        if (rowindex is not False):
            df.index = rowindex
            export_index = True

    if (export):
        if (replace == False):
            'check if file already exists'
            if (os.path.exists(saveFileDirectory)):
                df_existing = pd.read_csv(saveFileDirectory)
                df_existing = df_existing.append(df)
                df = df_existing
                df = df.drop_duplicates()

        df.to_csv(saveFileDirectory, header=True, index=export_index)

    return df
