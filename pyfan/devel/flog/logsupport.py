"""
The :mod:`pyfan.devel.flog.logsupport` initiates logging and set logging options, output log path
points.

This is imported into other programs as *import pyfan.devel.flog.logsupport as pyfan_logsup*

Includes method :func:`log_vig_start`, :func:`log_format`
"""

import logging
import pyfan.util.path.getfiles as pyfan_getfiles
import pyfan.util.timer.timer as pyfan_timer
import numpy as np


def log_vig_start(spt_root, main_folder_name, file_name='fs_gen_combo_type',
                  sub_folder_name=None, subsub_folder_name=None,
                  it_time_format=8, log_level=logging.WARNING,
                  **kwargs):
    """Start logging to log file

    Generate path to log file and initiate log file. Return this full path to log file. Configure the log file
    with formating

    Parameters
    ----------
    spt_root : str
        folder root to log file.
    main_folder_name : str
        main folder, appended to `spt_root`.
    file_name : str
        file name for the log file, without suffix.
    sub_folder_name : str, optional
        possible subfolder name. This is double pound vig level.
    subsub_folder_name : str, optional
        possible subsub folder name. try not to have lower than this level. This is triple pound vig level.
    it_time_format : int
        different types of time formatting, if `it_time_format` is zero, no time suffix
    log_level : int
        logging level integers to report, including CRITICAL 50 ERROR 40 WARNING 30 INFO 20 DEBUG 10 NOTSET 0.
    **kwargs
        Arguments for functions that is called, including :func:`log_format`

    Returns
    -------
    str
        return the path to the log file

    Examples
    --------
    >>> log_vig_start(spt_root = 'C:/Users/fan/',
    ...               main_folder_name='logvig', sub_folder_name='parameters',
    ...               subsub_folder_name='combo_type',
    ...               file_name='fs_gen_combo_type',
    ...               it_time_format=8, log_level=logging.INFO)
    C:\\Users\\fan\\logvig\\parameters\\combo_type\\fs_gen_combo_type_20201030.log.py
    """

    # A. Generate path
    spt_log = pyfan_getfiles.gen_path(spt_root, main_folder_name, sub_folder_name, subsub_folder_name)

    # B. File name with suffix
    if it_time_format == 0:
        snm_log = file_name
    else:
        snm_log = file_name + '_' + str(pyfan_timer.getDateTime(it_time_format))

    # C. Generate full path to log file
    spn_log = pyfan_getfiles.gen_path_file(spt_log, snm_log, st_file_type='log')

    # D. Start logging using the log file
    logging.basicConfig(filename=spn_log, filemode='w', level=log_level, format=log_format(**kwargs))

    return spn_log


def log_format(bl_set_print_opt=True, it_print_opt=1):
    """Logging formats

    This is called by :func:`log_vig_start`, with parameters fed in with *kwargs*

    Parameters
    ----------
    bl_set_print_opt : bool, optional
        If to set numpy table printing options, how many columns and decimal controls
    it_print_opt : int, optional
        Different possible options to set

    Returns
    -------
    str
        formatting string options for logging config

    Examples
    --------
    >>> log_format(bl_set_print_opt = True, it_print_opt = 1)
    '%(filename)s - %(funcName)s - %(lineno)d -  %(asctime)s - %(levelname)s %(message)s'
    """
    if bl_set_print_opt:
        if it_print_opt == 1:
            np.set_printoptions(precision=2, linewidth=100, suppress=True, threshold=3000)

    return '%(filename)s - %(funcName)s - %(lineno)d -  %(asctime)s - %(levelname)s %(message)s'
