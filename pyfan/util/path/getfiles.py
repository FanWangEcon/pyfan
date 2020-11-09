"""
The :mod:`pyfan.util.path.getfiles` generate and get various file paths.

Includes method :func:`gen_path_file`, :func:`gen_path`
"""

import os as os
from pathlib import Path
import pyfan.util.inout.iosupport as pyfan_iosup


def gen_path_file(spt_folder='', snm_file='', st_file_type=''):
    """Return full path to file given folder path and file name with suffix

    Parameters
    ----------
    spt_folder : str
        full path to folder
    snm_file : str
        file name without suffix (or with)
    st_file_type : str
        type of file, see options below, with pre-determined suffix, by default, there is no suffix. so if specify
        nothing, will save the `snm_file` with what is externally fed in

    Returns
    -------
    str
        Full path to file with path and file name.

    Examples
    --------
    >>> gen_path_file(spt_folder = 'C:/Users/fan/logvig/parameters/combo_type/',
    ...               snm_file = 'fs_gen_combo_type_20201030', st_file_type='log')
    C:\\Users\\fan\\logvig\\parameters\\combo_type\\fs_gen_combo_type_20201030.log.py
    """
    st_suffix = ''
    if st_file_type == 'log':
        st_suffix = '.log.py'

    return os.path.join(spt_folder, snm_file + st_suffix)


def gen_path(spt_root='', main_folder_name='', sub_folder_name=None, subsub_folder_name=None):
    """Generate a file path and return it

    Parameters
    ----------
    spt_root : str
        root name
    main_folder_name : str
        folder name
    sub_folder_name : str, optional
        subfolder name
    subsub_folder_name : str
        subsub folder name

    Returns
    -------
    str
        the full path to the folder

    Examples
    --------
    >>> gen_path(spt_root = 'C:/Users/fan/',
    ...          main_folder_name='logvig', sub_folder_name='parameters',
    ...          subsub_folder_name='combo_type')
    C:\\Users\\fan\\logvig\\parameters\\combo_type\\
    """
    spn_path_full = os.path.join(spt_root, main_folder_name, '')

    if sub_folder_name is not None:
        spn_path_full = pyfan_iosup.csvIO().createDirectory(spn_path_full, sub_folder_name)
        if subsub_folder_name is not None:
            spn_path_full = pyfan_iosup.csvIO().createDirectory(spn_path_full, subsub_folder_name)

    return spn_path_full


def fp_search_rglob(spt_root="../",
                    st_rglob='*.py',
                    ls_srt_subfolders=None,
                    verbose=False,
                    ):
    """Searches for files with search string in a list of folders

    Parameters
    ----------
    spt_root : string
        root folder to search in
    st_rglob : string
        search for files with this rglob string
    ls_srt_subfolders : :obj:`list` of :obj:`str`
        a list of subfolders of the spt_root to search in
    verbose: bool
        print details

    Returns
    -------
    :obj:`list` of :obj:`str`
        A list of file names

    Examples
    --------

    >>> ls_spn = fp_search_rglob(spt_root="../",
    >>>                          ls_srt_subfolders=['rmd', 'pdf'],
    >>>                          st_rglob = '*d*.py')
    [WindowsPath('../rmd/bookdownparse.py'), WindowsPath('../rmd/mattexmd.py'), WindowsPath('../rmd/rmdparse.py'), WindowsPath('../pdf/pdfgen.py')]

    """

    # Directories to search in
    if ls_srt_subfolders is None:
        # ls_srt_subfolders = ['calconevar/', 'derivative/', 'derivative_application/',
        #                      'matrix_basics/',
        #                      'opti_firm_constrained/', 'opti_hh_constrained_brsv/',
        #                      'opti_hh_constrained_brsv_inequality/']
        # ls_srt_subfolders = ['matrix_basics/']
        ls_spt = [spt_root]
    else:
        ls_spt = [spt_root + srt_subf for srt_subf in ls_srt_subfolders]

    if verbose:
        print(ls_spt)

    # get file names
    ls_spn_found_tex = [spn_file for spt_srh in ls_spt
                        for spn_file in Path(spt_srh).rglob(st_rglob)]
    if verbose:
        print(ls_spn_found_tex)

    return ls_spn_found_tex


# if __name__ == '__main__':
#     spt_root_u = "../"
#     ls_srt_subfolders_u = ['rmd', 'pdf']
#     st_rglob_u = '*d*.py'
#     verbose_u = False
#     ls_spn = fp_search_rglob(spt_root=spt_root_u, ls_srt_subfolders=ls_srt_subfolders_u,
#                              st_rglob=st_rglob_u, verbose=verbose_u)
#     print(ls_spn)
