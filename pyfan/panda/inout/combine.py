'''
Created on Aug 14, 2018

@author: fan

Combine Files Together
'''

import logging
import glob as glob
import pandas as pd
import os.path

import pyfan.panda.inout.readexport as readexport

logger = logging.getLogger(__name__)


def search_combine(search_directory=None,
                   file_search_str=None,
                   save_file_name=None,
                   save_panda=True,
                   return_current=False):
    """
    Estimation saves csv files in different folders. Each folder has different starting value. 
    Different estimation method. 
    
    Gather results together, create single csv file. To find which parameters lead to smallest objective. 
    
    Parameters
    ----------
    return_current: boolean
        return_current if true, do not save file, return current file
        
    
    Examples
    --------
    import panda.io.combine as pd_combine
    all_esti_df = pd_combine.search_combine(search_directory = None,
                                            file_search_str = None, 
                                            save_file_name = None)
    
    """

    '''
    A. Piece together folder and search string
    '''
    if (search_directory is None):
        d_root = 'C:/Users/fan/Documents/Dropbox (UH-ECON)/Project Dissertation EC2/'
        d_submain = 'thaijmp201808j7itgesti/esti/'
        param_folder_name = 'c_20180814_list_all_params'
        search_directory = d_root + d_submain + param_folder_name + '/'
    if (file_search_str is None):
        file_search_str = '*/*.csv'

    '''
    B. Generate folder_name + file_name, check if file exists
    '''
    save_directory = search_directory
    if (save_file_name is None):
        file_name = param_folder_name + '.csv'
    else:
        if (save_file_name.endswith('.csv')):
            file_name = save_file_name
        else:
            file_name = save_file_name + '.csv'

    save_directory_file_name = save_directory + file_name

    file_exists = False
    if (os.path.isfile(save_directory_file_name)):
        file_exists = True

    '''
    B. Return existing file and exit
    '''
    if (return_current and file_exists):
        all_esti_df = readexport.read_csv(save_directory_file_name)
    else:
        '''
        C. Get files satisfying search condition
        '''
        file_list = glob.glob(search_directory + file_search_str)

        method_fast = True

        if (method_fast == True):
            '''
            This is significantly faster than the method below: 
                - the pd.concat function is only invoked once
            '''
            total_count = 0
            pd_list = []
            for ctr, file in enumerate(file_list):
                total_count = total_count + 1
                pd_list.append(pd.read_csv(file))
                if (ctr % 10 == 0):
                    logger.critical('pd_list file current %s of file total %s', total_count, len(file_list))
                    logger.critical('pd_list list length:%s', len(pd_list))

            all_esti_df = pd.concat(pd_list, ignore_index=True)

            if (all_esti_df is not None):
                logger.critical('search_combine total file count:%s', total_count)
                logger.critical('search_combine total row count:%s', all_esti_df.shape[0])

                if (save_panda):
                    all_esti_df.to_csv(save_directory + file_name, header=True, index=False)

        else:
            '''
            D. Import as panda from each file and then join panda file together
            '''
            total_count = 0
            all_esti_df = None
            for ctr, file in enumerate(file_list):
                total_count = total_count + 1
                df_cur = pd.read_csv(file)
                if (ctr == 0):
                    all_esti_df = df_cur
                else:
                    all_esti_df = pd.concat([all_esti_df, df_cur], ignore_index=True)

                if (ctr % 10 == 0):
                    logger.critical('search_combine file current %s of file total %s', total_count, len(file_list))
                    logger.critical('search_combine row count:%s', all_esti_df.shape[0])

            if (all_esti_df is not None):
                logger.critical('search_combine total file count:%s', total_count)
                logger.critical('search_combine total row count:%s', all_esti_df.shape[0])

                '''
                E. Save Results in single file under main folder
                '''
                if (save_panda):
                    all_esti_df.to_csv(save_directory + file_name, header=True, index=False)

    return all_esti_df


if __name__ == "__main__":
    search_combine()
