'''
Created on Nov 27, 2017

@author: fan
'''

import numpy as np
import scipy.stats

import pyfan.amto.array.mesh as mesh


def three_vec_grids(vara_min, vara_max, vara_grid, vara_grid_add=None,
                    varb_min=None, varb_max=None, varb_grid=None, varb_grid_add=None,
                    varc_min=None, varc_max=None, varc_grid=None, varc_grid_add=None,
                    gridtype='grid', tomesh=False,
                    return_joint=False, return_single_col=False,
                    seed=999):
    """Grid for VFI
    Temporary code, so that I can deal with minimal school hour. should be 
    deleted in the future. and combined with the method above 
    """

    if (gridtype == 'grid'):
        a = np.linspace(vara_min, vara_max, vara_grid)
        if (varb_grid is not None):
            b = np.linspace(varb_min, varb_max, varb_grid)
        if (varc_grid is not None):
            c = np.linspace(varc_min, varc_max, varc_grid)
            if (varc_grid_add is not None):
                c = np.append(c, varc_grid_add)

    if (gridtype == 'rand'):
        np.random.seed(seed)
        a = random_vector_min_max(vara_min, vara_max, vara_grid)
        if (varb_grid is not None):
            b = random_vector_min_max(varb_min, varb_max, varb_grid)
        if (varc_grid is not None):
            c = random_vector_min_max(varc_min, varc_max, varc_grid)

    if (vara_grid_add is not None):
        a = np.append(a, vara_grid_add)
    if (varb_grid_add is not None):
        b = np.append(b, varb_grid_add)
    if (varc_grid_add is not None):
        c = np.append(c, varc_grid_add)

    a = np.sort(a)
    a = np.reshape(a, (-1, 1))

    if (varb_grid is not None):
        b = np.sort(b)
        if (varb_grid is not None):
            b = np.reshape(b, (-1, 1))

    if (varc_grid is not None):
        c = np.sort(c)
        if (varc_grid is not None):
            c = np.reshape(c, (-1, 1))

    if (varb_grid is not None):
        if (varc_grid is not None):
            if (tomesh == True):
                if (return_joint is True):
                    abc = mesh.three_mat_mesh(a, b, c,
                                              return_joint=return_joint,
                                              return_single_col=return_single_col)
                    return abc
                else:
                    a, b, c = mesh.three_mat_mesh(a, b, c,
                                                  return_joint=return_joint,
                                                  return_single_col=return_single_col)
                    return a, b, c
            else:
                return a, b, c
        else:
            if (tomesh == True):
                if (return_joint is True):
                    ab = mesh.two_mat_mesh(a, b, return_joint,
                                           return_single_col=return_single_col)
                    return ab
                else:
                    a, b = mesh.two_mat_mesh(a, b, return_joint,
                                             return_single_col=return_single_col)
                    return a, b
            else:
                return a, b
    else:
        return a


def random_vector_mean_sd(mean, sd, grid_count, gridtype='grid', seed=382):
    if (gridtype == 'grid'):
        unif_grid = np.linspace(0.001, 0.999, grid_count)
        standard_normal_grid = scipy.stats.norm.ppf(unif_grid)
        standard_normal_grid = np.reshape(standard_normal_grid, (-1, 1))

    if (gridtype == 'rand'):
        np.random.seed(seed)
        standard_normal_grid = np.random.randn(grid_count, 1)

    normal_grid = mean + sd * standard_normal_grid

    return normal_grid


def random_vector_min_max(minval, maxval, grid_count):
    if (grid_count == 1):
        'grid_count == 1 means we have no choice along that dimension'
        random_points = np.random.uniform(grid_count)
        random_vector = minval + random_points * (maxval - minval)
    else:
        random_points = np.random.uniform(size=(grid_count - 2))
        random_vector = minval + random_points * (maxval - minval)

        random_vector = np.insert(random_vector, 0, minval)
        random_vector = np.insert(random_vector, len(random_vector), maxval)

    return random_vector


if __name__ == '__main__':
    vara_min = 1
    vara_max = 10
    vara_grid = 4

    varb_min = 30
    varb_max = 31
    varb_grid = 2

    varc_min = -10
    varc_max = -5
    varc_grid = 3

    print('3 grids, 3 outputs')
    [veca, vecb, vecc] = three_vec_grids(vara_min, vara_max, vara_grid,
                                         vara_grid_add=None,
                                         varb_min=varb_min, varb_max=varb_max, varb_grid=varb_grid,
                                         varb_grid_add=None,
                                         varc_min=varc_min, varc_max=varc_max, varc_grid=varc_grid,
                                         varc_grid_add=None,
                                         gridtype='grid', tomesh=False, return_joint=False, seed=999)
    print('vec a:', np.transpose(veca))
    print('vec b:', np.transpose(vecb))
    print('vec c:', np.transpose(vecc))

    print('3 grids, mesh, 3 outputs')
    [veca, vecb, vecc] = three_vec_grids(vara_min, vara_max, vara_grid,
                                         vara_grid_add=None,
                                         varb_min=varb_min, varb_max=varb_max, varb_grid=varb_grid,
                                         varb_grid_add=None,
                                         varc_min=varc_min, varc_max=varc_max, varc_grid=varc_grid,
                                         varc_grid_add=None,
                                         gridtype='grid', tomesh=True, return_joint=False, seed=999)
    print('vec a:', np.transpose(veca))
    print('vec b:', np.transpose(vecb))
    print('vec c:', np.transpose(vecc))

    print('3 grids, mesh, joint')
    outputs = three_vec_grids(vara_min, vara_max, vara_grid,
                              vara_grid_add=None,
                              varb_min=varb_min, varb_max=varb_max, varb_grid=varb_grid,
                              varb_grid_add=None,
                              varc_min=varc_min, varc_max=varc_max, varc_grid=varc_grid,
                              varc_grid_add=None,
                              gridtype='grid', tomesh=True, return_joint=True, seed=999)
    print('outputs:', outputs)

    print('3 grids, mesh, joint, rand')
    outputs = three_vec_grids(vara_min, vara_max, vara_grid,
                              vara_grid_add=None,
                              varb_min=varb_min, varb_max=varb_max, varb_grid=varb_grid,
                              varb_grid_add=None,
                              varc_min=varc_min, varc_max=varc_max, varc_grid=varc_grid,
                              varc_grid_add=None,
                              gridtype='rand', tomesh=True, return_joint=True, seed=999)
    print('outputs:', outputs)

    print('3 grids, mesh, joint, rand, add_more')
    outputs = three_vec_grids(vara_min, vara_max, vara_grid,
                              vara_grid_add=np.array([-1]),
                              varb_min=varb_min, varb_max=varb_max, varb_grid=varb_grid,
                              varb_grid_add=None,
                              varc_min=varc_min, varc_max=varc_max, varc_grid=varc_grid,
                              varc_grid_add=np.array([-999, -99, 111]),
                              gridtype='rand', tomesh=True, return_joint=True, seed=999)
    print('outputs:', outputs)

    print('2 grids, mesh, joint, rand, add_more')
    outputs = three_vec_grids(vara_min, vara_max, vara_grid,
                              vara_grid_add=np.array([-1, 839, 33]),
                              varb_min=varb_min, varb_max=varb_max, varb_grid=varb_grid,
                              varb_grid_add=None,
                              gridtype='grid', tomesh=True, return_joint=True, seed=999)
    print('outputs:', outputs)
