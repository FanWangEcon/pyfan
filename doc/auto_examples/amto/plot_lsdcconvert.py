# -*- coding: utf-8 -*-
"""
List and Dictionary Convertions
========================================================================
Convert between list and dictionary
"""

# Author: Fan Wang (fanwangecon.github.io)
import pyfan.amto.lsdc.lsdcconvert as pyfan_amto_lsdcconvert
import pprint
import matplotlib.pyplot as plt
import textwrap

# %%
# Convert list to dictionary
# --------------------------------------------------------------

# list
ls_combo_type = ["e", "20201025x_esr_list_tKap_mlt_ce1a2", ["esti_param.kappa_ce9901", "esti_param.kappa_ce0209"],
                 1, "C1E31M3S3=1"]

# convert calling function without parameters:
dc_ls_combo_type_a = pyfan_amto_lsdcconvert.ff_ls2dc(ls_combo_type, 'i', 'o', verbose=True)
print(f'{dc_ls_combo_type_a=}')

# convert calling function with later parameter names:
dc_ls_combo_type_b = pyfan_amto_lsdcconvert.ff_ls2dc(ls_combo_type, st_counter_str='i', st_all_str='o')
print(f'{dc_ls_combo_type_b=}')

# convert calling function with all named parameters:
dc_ls_combo_type_c = pyfan_amto_lsdcconvert.ff_ls2dc(ls_list=ls_combo_type, st_counter_str='i', st_all_str='o')
print(f'{dc_ls_combo_type_c=}')

# provide name for list
dc_ls_combo_type_d= pyfan_amto_lsdcconvert.ff_ls2dc(ls_list=ls_combo_type, st_counter_str='CTR', st_all_str='OF', st_ls_name='ls_other_name')
print(f'{dc_ls_combo_type_d=}')

# check three calling methods all work
print(f'{dc_ls_combo_type_a==dc_ls_combo_type_b=}')
print(f'{dc_ls_combo_type_a==dc_ls_combo_type_c=}')
print(f'{dc_ls_combo_type_a==dc_ls_combo_type_d=}')

# Start Plot
fig, ax = plt.subplots()

# Text Plot
ax.text(0.5, 0.5,
        f'ls_combo_type is:\n{textwrap.fill(str(ls_combo_type), width=80)}'
        f'\n\n'
        f'dc_ls_combo_type_c is:\n{textwrap.fill(str(dc_ls_combo_type_c), width=80)}',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=10, color='black',
        transform=ax.transAxes)

# Labeling
ax.set_axis_off()
plt.show()
