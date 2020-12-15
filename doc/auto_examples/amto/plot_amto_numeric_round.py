# -*- coding: utf-8 -*-
"""
Numeric Rounding Function
========================================================================
Given an array of numbers round it with conditioning formattings.
"""

# Author: Fan Wang (fanwangecon.github.io)
import pyfan.amto.numeric.round as pyfan_amto_round
import numpy as np
import matplotlib.pyplot as plt

# %%
# Common rounding
# --------------------------------------------------------------

# construct data inputs
ar_fl_exa = np.array([0.4334, 0.5183, 0.0454, 0.0027, 0.0002])
ls_st_numformated_common = pyfan_amto_round.ff_decimal_rounder(ls_fl_num2format=ar_fl_exa, it_or_dc_round_decimal=2)
print(f'{ls_st_numformated_common=}')

# %%
# Uncommon rounding by number size with fractions
# --------------------------------------------------------------
dc_round_decimal = {0.001:4, 0.01:3, 0.1:2, float("inf"):2}
ls_st_numformated_uncommon = pyfan_amto_round.ff_decimal_rounder_uncommon(ls_fl_num2format=ar_fl_exa,
                                                                          dc_round_decimal=dc_round_decimal)
print(f'{ls_st_numformated_uncommon=}')


# %%
# Uncommon rounding by number size test 2 with large numbers
# --------------------------------------------------------------
ls_fl_num2format = [0.0012345, 0.12345, 12.345, 123.45, 1234.5, 123456.789]
dc_round_decimal = {0.1:4, 1:3, 100:2, float("inf"):0}
ls_st_numformated_large_uncommon = pyfan_amto_round.ff_decimal_rounder_uncommon(ls_fl_num2format=ls_fl_num2format,
                                                                                dc_round_decimal=dc_round_decimal)
print(f'{ls_st_numformated_large_uncommon=}')


# Start Plot
fig, ax = plt.subplots()

# Text Plot
ax.text(0.5, 0.5, f'{ar_fl_exa}\n{ls_st_numformated_common=}\n{dc_round_decimal=}\n{ls_st_numformated_uncommon=}'
                  f'\n\n{ls_fl_num2format=}\n{dc_round_decimal=}\n{ls_st_numformated_large_uncommon=}',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=10, color='black',
        transform=ax.transAxes)

# Labeling
ax.set_axis_off()
plt.show()

