"""
The :mod:`pyfan.stats.markov.transprobcheck` checks markov transition row sums.

A markov transition matrix where each row does not
sum up to 1 due to simulation errors. Check if the gap between 1 and the row
values are too big, and then normalize.

import pyfan.stats.markov.transprobcheck as pyfan_stats_transprobcheck

Includes method :func:`markov_trans_prob_check` and :func:`markov_condi_prob2one`.
"""

import numpy as np


def markov_trans_prob_check(mt_trans, fl_atol_per_row=1e-05, fl_atol_avg_row=1e-08, fl_sum_to_match=1):
    """Markov conditional transition probability check

    Parameters
    ----------
    mt_trans : numpy.array of shape (N, N)
        The AR1 transition matrix, each row is a state, each value in each row is the conditional
        probability of moving from state i (row) to state j (column)
    fl_atol_per_row : `float`, optional
        Tolerance for the difference between 1 and each row sum
    fl_atol_avg_row : `float`, optional
        Tolerance for the difference between 1 and average of row sums
    fl_sum_to_match : `float`, optional
        This should be 1, unless the function is not used to handle transition matrixes
    Returns
    -------
    tuple
        A tuple of booleans, the first element is if satisfies the overall criteria. Second
        is if satisifes the per_row condition. Third if satisfies the average criteria.

    Examples
    --------
    >>> mt_ar1_trans = np.array([[0.4334, 0.5183, 0.0454],
    >>>                          [0.2624, 0.5967, 0.1245],
    >>>                          [0.1673, 0.5918, 0.2005]])
    >>> bl_ar1_sum_pass, bl_per_row_pass, bl_avg_row_pass = markov_trans_prob_check(mt_ar1_trans)
    >>> print(f'{bl_ar1_sum_pass=}')
    bl_ar1_sum_pass=False
    >>> print(f'{bl_per_row_pass=}')
    bl_per_row_pass=False
    >>> print(f'{bl_avg_row_pass=}')
    bl_avg_row_pass=False
    """

    ar_row_sums_ar1 = np.sum(mt_trans, axis=1)
    # per-row check
    bl_per_row_pass = np.allclose(ar_row_sums_ar1, fl_sum_to_match,
                                  rtol=0,
                                  atol=fl_atol_per_row)
    # all-rows check
    fl_row_gap_mean = np.mean(abs(ar_row_sums_ar1 - fl_sum_to_match))
    bl_avg_row_pass = np.allclose(fl_row_gap_mean + fl_sum_to_match, fl_sum_to_match,
                                  rtol=0,
                                  atol=fl_atol_avg_row)
    # Joint
    bl_ar1_sum_pass = bl_per_row_pass and bl_avg_row_pass

    return bl_ar1_sum_pass, bl_per_row_pass, bl_avg_row_pass


def markov_condi_prob2one(mt_trans):
    """Rescale markov transitions rows to sum to 1

    Suppose each transition matrix row sums up to slighly less than one, rescale so it sums to one.

    Parameters
    ----------
    mt_trans : numpy.array of shape (N, N)
        The AR1 transition matrix, each row is a state, each value in each row is the conditional
        probability of moving from state i (row) to state j (column)

    Returns
    -------
    ndarray
        The rescaled numpy array
    """

    # current row sums
    ar_row_sums_ar1 = np.sum(mt_trans, axis=1)
    ar_row_sums_ar1 = np.reshape(ar_row_sums_ar1, [-1, 1])
    # Update row values
    mt_ar1_trans_norm = mt_trans / np.reshape(ar_row_sums_ar1, [-1, 1])
    # ar_row_sums_ar1_norm = np.sum(mt_ar1_trans_norm, axis=1)
    # ar_row_sums_ar1_norm = np.reshape(ar_row_sums_ar1_norm, [-1, 1])

    return mt_ar1_trans_norm
