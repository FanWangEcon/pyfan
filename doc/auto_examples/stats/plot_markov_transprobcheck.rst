.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_auto_examples_stats_plot_markov_transprobcheck.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_auto_examples_stats_plot_markov_transprobcheck.py:


Markov Transition Probability Check and Transform
========================================================================

In this example, use several markov transition matrixes where each row does not
sum up to 1 due to simulation errors. Check if the gap between 1 and the row
values are too big, and then normalize.


.. code-block:: default


    # Author: Fan Wang (fanwangecon.github.io)
    import pyfan.stats.markov.transprobcheck as pyfan_stats_transprobcheck
    import numpy as np
    import matplotlib.pyplot as plt








Check Row Sum of a Five by Five Transition matrix
--------------------------------------------------------------


.. code-block:: default


    # construct data inputs
    mt_ar1_trans = np.array([[0.4334, 0.5183, 0.0454, 0.0027, 0.0002],
                             [0.2624, 0.5967, 0.1245, 0.0145, 0.0016],
                             [0.1673, 0.5918, 0.2005, 0.0343, 0.0052],
                             [0., 0.0312, 0.6497, 0.2774, 0.0371],
                             [0., 0.0681, 0.6569, 0.2379, 0.0327],
                             [0., 0.2201, 0.581, 0.168, 0.0264]])
    ar_row_sums_ar1 = np.sum(mt_ar1_trans, axis=1)
    print(f'{ar_row_sums_ar1=}')

    # Check with default conditions, does not pass
    bl_ar1_sum_pass, bl_per_row_pass, bl_avg_row_pass = \
        pyfan_stats_transprobcheck.markov_trans_prob_check(mt_ar1_trans)
    print(f'{bl_ar1_sum_pass=}')
    print(f'{bl_per_row_pass=}')
    print(f'{bl_avg_row_pass=}')

    # Check with relaxed conditions, pass per row does not pass average
    fl_atol_per_row = 1e-02
    fl_atol_avg_row = 1e-03
    bl_ar1_sum_pass, bl_per_row_pass, bl_avg_row_pass = \
        pyfan_stats_transprobcheck.markov_trans_prob_check(mt_ar1_trans, fl_atol_per_row, fl_atol_avg_row)
    print(f'{bl_ar1_sum_pass=}')
    print(f'{bl_per_row_pass=}')
    print(f'{bl_avg_row_pass=}')

    # Relax condition further, passes
    fl_atol_per_row = 1e-02
    fl_atol_avg_row = 5e-03
    bl_ar1_sum_pass, bl_per_row_pass, bl_avg_row_pass = \
        pyfan_stats_transprobcheck.markov_trans_prob_check(mt_ar1_trans, fl_atol_per_row, fl_atol_avg_row)
    print(f'{bl_ar1_sum_pass=}')
    print(f'{bl_per_row_pass=}')
    print(f'{bl_avg_row_pass=}')

    # Start Plot
    fig, ax = plt.subplots()

    # Text Plot
    ax.text(0.5, 0.5, f'{mt_ar1_trans} '
                      f'\n\n {fl_atol_per_row=} and {fl_atol_avg_row=} '
                      f'\n\n {bl_ar1_sum_pass=} \n {bl_per_row_pass=} \n {bl_avg_row_pass=}',
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=10, color='black',
            transform=ax.transAxes)

    # Labeling
    ax.set_axis_off()
    plt.show()




.. image:: /auto_examples/stats/images/sphx_glr_plot_markov_transprobcheck_001.svg
    :alt: plot markov transprobcheck
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    ar_row_sums_ar1=array([1.    , 0.9997, 0.9991, 0.9954, 0.9956, 0.9955])
    bl_ar1_sum_pass=False
    bl_per_row_pass=False
    bl_avg_row_pass=False
    bl_ar1_sum_pass=False
    bl_per_row_pass=True
    bl_avg_row_pass=False
    bl_ar1_sum_pass=True
    bl_per_row_pass=True
    bl_avg_row_pass=True




Rescale a Three by Three Transition so Each Row Sums to One
--------------------------------------------------------------


.. code-block:: default


    mt_ar1_trans = np.array([[0.4334, 0.5183, 0.0454], [0.2624, 0.5967, 0.1245], [0.1673, 0.5918, 0.2005]])
    bl_ar1_sum_pass, bl_per_row_pass, bl_avg_row_pass = pyfan_stats_transprobcheck.markov_trans_prob_check(mt_ar1_trans)
    mt_ar1_trans_rescaled = pyfan_stats_transprobcheck.markov_condi_prob2one(mt_ar1_trans)
    bl_ar1_sum_pass_rescaled, bl_per_row_pass_rescaled, bl_avg_row_pass_rescaled = \
        pyfan_stats_transprobcheck.markov_trans_prob_check(mt_ar1_trans_rescaled)

    # Start Plot
    fig, ax = plt.subplots()

    # Text Plot
    ax.text(0.5, 0.5, f'{mt_ar1_trans} '
                      f'\n\n {bl_ar1_sum_pass=}'
                      f'\n\n {mt_ar1_trans_rescaled}' 
                      f'\n\n {bl_ar1_sum_pass_rescaled=}',
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=10, color='black',
            transform=ax.transAxes)

    # Labeling
    ax.set_axis_off()
    plt.show()



.. image:: /auto_examples/stats/images/sphx_glr_plot_markov_transprobcheck_002.svg
    :alt: plot markov transprobcheck
    :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.091 seconds)


.. _sphx_glr_download_auto_examples_stats_plot_markov_transprobcheck.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: plot_markov_transprobcheck.py <plot_markov_transprobcheck.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: plot_markov_transprobcheck.ipynb <plot_markov_transprobcheck.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
