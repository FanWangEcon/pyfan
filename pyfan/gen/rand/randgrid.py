"""
The :mod:`pyfan.gen.rand.randgrid` generate a grid with randomly spaced grid
points.

.. math:: x \\sim N\\left(\\mu, \\sigma\\right)

Includes method :func:`ar_draw_random_normal`.
"""

import numpy as np
from scipy.stats import norm


def ar_draw_random_normal(fl_mu, fl_sd, it_draws,
                          it_seed=None, it_draw_type=0,
                          fl_lower_sd=-3, fl_higher_sd=None):
    """Draw a Vector of Possibly Sorted and Bounded Normal Shocks

    Parameters
    ----------
    fl_mu, fl_sd : `float`
        The mean and standard deviation of the normal process
    it_draws: `int`
        Number of Draws
    it_seed: `int`, optional
        External random seed externally. Default is 123.
    it_draw_type: `int`, optional
        Indicates which type of normal draws to make. 0 sorted normal draws
        cut off at bounds. 1 equi-quantile unequal distance points;
        2 normal draws unsorted.
    fl_lower_sd, fl_higher_sd : `float`
        Impose lower and upper bounds (in sd units) on shock draws. The normal
        distribution does not have lower or upper bounds.

    Returns
    -------
    numpy.array of shape (1, it_draws)
        A vector of sorted or unsorted random grid points, or equi-quantile
        points.

    Notes
    -----
        This method requires a dataset of equal-sized time series

    Examples
    --------
    >>> fl_mu = 0
    >>> fl_sd = 1
    >>> it_draws = 5
    >>> it_seed = 123
    >>> fl_lower_sd = -1
    >>> fl_higher_sd = 0.8
    >>> it_draw_type = 0
    >>> ar_draw_random_normal(fl_mu, fl_sd, it_draws,
    ...                       it_seed, it_draw_type,
    ...                       fl_lower_sd, fl_higher_sd)
    [-1.          0.8         0.2829785 - 1. - 0.57860025]

    >>> it_draw_type = 1
    >>> ar_draw_random_normal(fl_mu, fl_sd, it_draws,
    ...                       it_seed, it_draw_type,
    ...                       fl_lower_sd, fl_higher_sd)
    [-1. - 0.47883617 - 0.06672597  0.3338994   0.8]

    >>> it_draw_type = 2
    >>> ar_draw_random_normal(fl_mu, fl_sd, it_draws,
    ...                       it_seed, it_draw_type,
    ...                       fl_lower_sd, fl_higher_sd)
    [-1. - 1. - 0.57860025  0.2829785   0.8]
    """

    # set seed
    if it_seed is None:
        it_seed = 123
    np.random.seed(it_seed)

    if (fl_higher_sd is None) and (fl_lower_sd is not None):
        fl_higher_sd = -fl_lower_sd

    # randomly drawing and then sorting
    if it_draw_type == 0 or it_draw_type == 2:
        ar_shock_draws = np.random.normal(0, 1, it_draws)
        if it_draw_type == 2:
            ar_shock_draws = np.sort(ar_shock_draws)
        if fl_lower_sd is not None:
            ar_shock_draws[ar_shock_draws < fl_lower_sd] = fl_lower_sd
        if fl_higher_sd is not None:
            ar_shock_draws[ar_shock_draws > fl_higher_sd] = fl_higher_sd
        ar_shock_draws = fl_mu + fl_sd * ar_shock_draws

    # Equi-quantile z points (but unequal x-distance)
    if it_draw_type == 1:
        if fl_lower_sd is None:
            fl_lower_sd = 0.0000001
        if fl_higher_sd is None:
            fl_higher_sd = 0.9999999
        lower_q = norm.cdf(fl_lower_sd)
        higher_q = norm.cdf(fl_higher_sd)
        ar_e_quantiles = np.linspace(lower_q, higher_q, it_draws)
        ar_shock_draws = norm.ppf(ar_e_quantiles, loc=fl_mu, scale=fl_sd)

    return ar_shock_draws
