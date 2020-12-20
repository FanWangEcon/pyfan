'''
The :mod:`pyfan.amto.lsdc.lsdcconvert` module provides list and dict converters.

Created on Dec 18, 2020

import pyfan.amto.lsdc.lsdcconvert as pyfan_amto_lsdcconvert

Includes method :func:`ff_decimal_rounder_uncommon` and :func:`ff_decimal_rounder`.
'''

import traceback
import pprint


def ff_ls2dc(ls_list, st_counter_str='i', st_all_str='o', st_ls_name=None, verbose=False):
    """Convert list to dict with list name and index and dict keys

    Parameters
    ----------
    ls_list : list
        A list of values.
    st_counter_str : str
        String prefix for list counter in dictionary name.
    st_all_str : str
        String prefix in front of total ele length in dict key name.

    Returns
    -------
    dict
        A dictionary of equal length to `ls_list` input, list converted to dict.
    """

    if st_ls_name is None:

        stack = traceback.extract_stack()
        filename, lineno, function_name, code = stack[-2]

        if verbose:
            pprint.pprint(code, width=1)

        if "ls_list=" in code:
            # function called with three parameters all named, looks like:
            #   "dc_ls_combo_type = pyfan_amto_lsdcconvert.ff_ls2dc(ls_list=ls_combo_type,"
            st_ls_name = code.split("ls_list=")[1]
        else:
            # function was not called with named parameter, looks like:
            #   "dc_ls_combo_type = pyfan_amto_lsdcconvert.ff_ls2dc(ls_combo_type, 'i', 'o')"
            #    "dc_ls_combo_type = pyfan_amto_lsdcconvert.ff_ls2dc(ls_combo_type)"
            st_ls_name = code.split("ff_ls2dc(")[1]

        # Get first input element
        if ',' in st_ls_name:
            st_ls_name = st_ls_name.split(",")[0]
        else:
            st_ls_name = st_ls_name.split(")")[0]

        if "=" in st_ls_name:
            raise ValueError(f'ff_ls2dc function called incorrectly, ls_list parameter must be first:{code=}')

    # List name as string variable
    # st_ls_name = f'{ls_list=}'.split('=')[0]

    # Convert to dict
    dc_from_list = {st_ls_name + '_' +
                    st_counter_str + str(it_idx) + st_all_str + str(len(ls_list)): ob_val
                    for it_idx, ob_val in enumerate(ls_list)}
    # Print
    if verbose:
        pprint.pprint(dc_from_list, width=1)

    # Return
    return dc_from_list
