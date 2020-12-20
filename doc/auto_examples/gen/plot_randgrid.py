# -*- coding: utf-8 -*-
"""
Draw Shock Grid
========================================================================

In this example, we draw shock grids.

"""

# Author: Fan Wang (fanwangecon.github.io)
import numpy as np
import matplotlib.pyplot as plt
import pyfan.gen.rand.randgrid as pyfan_gen_rand

# %%
# Shared parameters
# ------------------------
fl_mu = 0
fl_sd = 1
it_draws = 25
it_seed = 123
fl_lower_sd = -2
fl_higher_sd = 2

# %%
# Type 0 Shock draw
# ------------------------
it_draw_type = 0
ar_shock_t0 = \
    pyfan_gen_rand.ar_draw_random_normal(fl_mu, fl_sd, it_draws,
                                         it_seed, it_draw_type,
                                         fl_lower_sd, fl_higher_sd)
print('it_draw_type=0')
print(ar_shock_t0)

# %%
# Type 1 Shock draw
# ------------------------
it_draw_type = 1
ar_shock_t1 = \
    pyfan_gen_rand.ar_draw_random_normal(fl_mu, fl_sd, it_draws,
                                         it_seed, it_draw_type,
                                         fl_lower_sd, fl_higher_sd)
print('it_draw_type=1')
print(ar_shock_t1)

# %%
# Type 2 Shock draw
# ------------------------
it_draw_type = 2
ar_shock_t2 = \
    pyfan_gen_rand.ar_draw_random_normal(fl_mu, fl_sd, it_draws,
                                         it_seed, it_draw_type,
                                         fl_lower_sd, fl_higher_sd)
print('it_draw_type=2')
print(ar_shock_t2)

# %%
# Draw Shocks Jointly
# ------------------------
fig, ax = plt.subplots()
# Graph
ar_it_x_grid = np.arange(1, it_draws + 1)
ax.plot(ar_it_x_grid, ar_shock_t0,
                     color='blue', linestyle='dashed', marker='x',
                     label='Type 0: Bounded Shock Draws')
ax.scatter(ar_it_x_grid, ar_shock_t1,
                     color='red',
                     label='Type 1: Quantile Points')
ax.plot(ar_it_x_grid, ar_shock_t2,
                     color='black', marker='d',
                     label='Type 3: Sorted Bounded Shock Draws')
# Labeling
ax.legend(loc='upper left')
plt.ylabel('Shock Values')
plt.xlabel('Shock Draw Points')
plt.title('Shock, Sorted and Bounded Shocks, Quantile Points')
plt.grid()
plt.show()
