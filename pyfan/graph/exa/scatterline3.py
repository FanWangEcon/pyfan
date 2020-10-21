"""
The :mod:`pyfan.graph.example.scatterline3` generates a graprh with three lines.
This is the functionalized vesrion of `plot_randgrid Example <https://pyfan.readthedocs.io/en/latest/auto_examples/plot_randgrid.html#sphx-glr-auto-examples-plot-randgrid-py>`_.

Includes method :func:`gph_scatter_line_rand`.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyfan.gen.rand.randgrid as pyfan_gen_rand
import pyfan.aws.general.path as pyfan_path
import pyfan.util.timer.timer as pyfan_timer
import argparse
import sys
import os


# Parse Inputs to be used commandline
parser = argparse.ArgumentParser()
parser.add_argument('-A', dest="st_s3_bucket", help="s3 bucket to store output images", default='fans3testbucket')
parser.add_argument('-B', dest="it_seed", help="random seed", type=int, default=666)

args = parser.parse_args()


def gph_scatter_line_rand(fl_mu=0, fl_sd=1,
                          it_draws=25, it_seed=123,
                          fl_lower_sd=-2, fl_higher_sd=2,
                          bl_show_fig=True, bl_save_fig=False,
                          st_s3_bucket='fans3testbucket'):
    """A randomly generated graph with scatter plot and lines.

    Parameters
    ----------
    fl_mu, fl_sd : `float`, optional
        The mean and standard deviation of the normal process for lines
    it_draws: `integer`, optional
        Number of Draws lines
    it_seed: `integer`, optional
        External random seed externally. Default is 123. for lines
    fl_lower_sd, fl_higher_sd : `float`, optional
        Impose lower and upper bounds (in sd units) on shock draws. The normal
        distribution does not have lower or upper bounds.
    bl_show_fig: `bool`, optional
        Show graph in documentation if needed. When storing graph to disc and uploading
        to s3, do not need to show.

    Returns
    -------
    pandas.DataFrame of shape (`it_draws`, 4)
        A pandas dataframe with `it_draws` number of rows and four columns. First
        for x values, the next three for three types of randomly generated variables
        that are been plotted out.

    Examples
    --------
    >>> fl_mu = 0
    >>> fl_sd = 1
    >>> it_draws = 20
    >>> it_seed = 456
    >>> fl_lower_sd = -1
    >>> fl_higher_sd = 0.8
    >>> scatter_line_rand_graph(fl_mu, fl_sd,
	...						    it_draws, it_seed,
	...			                fl_lower_sd, fl_higher_sd)
		   x    shk_t0    shk_t1    shk_t2
	1    1.0 -0.668129 -2.000000 -2.000000
	2    2.0 -0.498210 -1.533950 -1.130231
	3    3.0  0.618576 -1.268601 -1.111846
	4    4.0  0.568692 -1.071098 -0.971485
	5    5.0  1.350509 -0.908400 -0.668129
	6    6.0  1.629589 -0.766786 -0.498210
	7    7.0  0.301966 -0.639112 -0.384060
	8    8.0  0.449483 -0.521108 -0.345811
	9    9.0 -0.345811 -0.409963 -0.325130
	10  10.0 -0.315231 -0.303676 -0.315231
	11  11.0 -2.000000 -0.200721 -0.106208
	12  12.0 -1.130231 -0.099856 -0.088752
	13  13.0 -1.111846  0.000000  0.237851
	14  14.0  0.237851  0.099856  0.301966
	15  15.0 -0.325130  0.200721  0.449483
	16  16.0  1.944702  0.303676  0.568692
	17  17.0  1.915676  0.409963  0.618576
	18  18.0  0.920348  0.521108  0.920348
	19  19.0  0.936398  0.639112  0.936398
	20  20.0  1.157552  0.766786  1.139873
	21  21.0 -0.106208  0.908400  1.157552
	22  22.0 -0.088752  1.071098  1.350509
	23  23.0 -0.971485  1.268601  1.629589
	24  24.0 -0.384060  1.533950  1.915676
	25  25.0  1.139873  2.000000  1.944702
    """

    # Type 0 Shock draw
    it_draw_type = 0
    ar_shock_t0 = \
        pyfan_gen_rand.ar_draw_random_normal(fl_mu, fl_sd, it_draws,
                                             it_seed, it_draw_type,
                                             fl_lower_sd, fl_higher_sd)

    # Type 1 Shock draw
    it_draw_type = 1
    ar_shock_t1 = \
        pyfan_gen_rand.ar_draw_random_normal(fl_mu, fl_sd, it_draws,
                                             it_seed, it_draw_type,
                                             fl_lower_sd, fl_higher_sd)

    # Type 2 Shock draw
    it_draw_type = 2
    ar_shock_t2 = \
        pyfan_gen_rand.ar_draw_random_normal(fl_mu, fl_sd, it_draws,
                                             it_seed, it_draw_type,
                                             fl_lower_sd, fl_higher_sd)

    # Draw Shocks Jointly
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
    if bl_show_fig:
        plt.show()
    if bl_save_fig:
        sna_image_name = 'f_' + pyfan_timer.getDateTime(8) +'_s' + str(it_seed)

        srt_s3_bucket_folder = 'pyfan_gph_scatter_line_rand'
        pyfan_path.save_img(plt, sna_image_name,
                            dpi=300, papertype='a4',
                            orientation='horizontal',
                            bl_upload_s3=True, st_s3_bucket=st_s3_bucket,
                            srt_s3_bucket_folder=srt_s3_bucket_folder)
    # %%
    # Upload a local image
    # ------------------------

    mt_shocks = np.column_stack([ar_it_x_grid, ar_shock_t0, ar_shock_t1, ar_shock_t2])
    df_shocks = pd.DataFrame(data=mt_shocks,
                             index=range(1, mt_shocks.shape[0] + 1),
                             columns=['x', 'shk_t0', 'shk_t1', 'shk_t2'])
    return df_shocks


if __name__ == "__main__":

    # Run on command line, might need to install latest file locally first
    # conda activate base
    # cd "C:/Users/fan/pyfan/"
    # python setup.py install --user
    # python C:/Users/fan/pyfan/pyfan/graph/exa/scatterline3.py -A fans3testbucket -B 1
    # python /pyfan/pyfan/graph/exa/scatterline3.py -A fans3testbucket -B 1

    # This is an AWS Batch run with Job Array Index for Parallel processing
    # With this, only one job needs to be specified
    if "AWS_BATCH_JOB_ARRAY_INDEX" in os.environ:
        print('AWS_BATCH_JOB_ARRAY_INDEX')
        it_seed_arg = os.environ['AWS_BATCH_JOB_ARRAY_INDEX']
        it_seed_arg = int(it_seed_arg)
    else:
        it_seed_arg = args.it_seed

    print(it_seed_arg)

    gph_scatter_line_rand(fl_mu=0, fl_sd=1,
                          it_draws=25, it_seed=it_seed_arg,
                          fl_lower_sd=-2, fl_higher_sd=2,
                          bl_show_fig=False, bl_save_fig=True,
                          st_s3_bucket=args.st_s3_bucket)
