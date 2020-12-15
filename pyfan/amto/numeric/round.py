'''
The :mod:`pyfan.amto.numeric.round` provides decimal rounding for float arrays.

Given an array of numbers, provide conditional decimal formatting rounding via
fstring. This is used by table function to generate table specific rounding rules.

For example, a table with birthweight in grams, and ratios, might have 2 decimals for numbers
less than 1, but no decimals for numbers larger than 1000 (which are the grams).

import pyfan.amto.numeric.round as pyfan_amto_round

Created on Dec 14, 2020

Includes method :func:`ff_decimal_rounder_uncommon` and :func:`ff_decimal_rounder`.
'''


def ff_decimal_rounder(ls_fl_num2format, it_or_dc_round_decimal, verbose=False):
    """Decimal rounding function with common decimal formatting

    Parameters
    ----------
    ls_fl_num2format : list of float
        see :func:`ff_decimal_rounder`
    it_or_dc_round_decimal : int or dict
        the number of decimal points to keep. If dict, same as dc_round_decimal for :func:`ff_decimal_rounder`.
        If decimal, generate dict that provides common formating

    Returns
    -------
    list of str
        Decimal formatted string outputs
    """

    if isinstance(it_or_dc_round_decimal, int):
        dc_round_decimal = {float("inf"): it_or_dc_round_decimal}
    elif isinstance(it_or_dc_round_decimal, dict):
        dc_round_decimal = it_or_dc_round_decimal
    else:
        raise ValueError(f'{it_or_dc_round_decimal=} needs to be int or dict')

    return ff_decimal_rounder_uncommon(ls_fl_num2format=ls_fl_num2format, dc_round_decimal=dc_round_decimal, verbose=verbose)


def ff_decimal_rounder_uncommon(ls_fl_num2format=[0.0012345, 0.12345, 12.345, 123.45, 1234.5, 123456.789],
                                dc_round_decimal={0.1: 4, 1: 3, 100: 2, float("inf"): 0},
                                verbose=False):
    """Decimal rounding function with conditional formatting by number size

    Given an array of numbers, format and return as a list of string, with different decimal formatting given
    different number sizes.

    Parameters
    ----------
    ls_fl_num2format : list of float
        list of numbers of approximate to decimals
    dc_round_decimal : dict
        dict incremental formatter. For example, for the default, if below 0.1 keep 4 decimals, If below 1 keep 3,
        if below 100 keep 2, if otherwise above, then keep 0 decimals Loop over formatter.

    Returns
    -------
    list of str
        Decimal formatted string outputs
    """

    ls_st_numformated = []

    for fl_num2format in ls_fl_num2format:
        for fl_threshold, it_decimals in dc_round_decimal.items():
            if fl_num2format < fl_threshold:
                st_float_rounded = f'{fl_num2format:.{it_decimals}f}'
                ls_st_numformated.append(st_float_rounded)
                if verbose:
                    print(f'{fl_num2format=}, {st_float_rounded=}, {fl_threshold=}, {it_decimals=}')
                break
        else:
            continue

    return ls_st_numformated
