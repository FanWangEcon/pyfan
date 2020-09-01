'''
Created on May 24, 2018

@author: fan

To have a better grid denser at the beginning
'''

import time as time
import numpy as np

from numba import jit

import logging

logger = logging.getLogger(__name__)


# @vectorize([float64(float64, float64, float64, float64, float64, float64, float64, float64)])
def grid_to_geom_short(choice_grid, choice_grid_max, choice_grid_min,
                       start, stop, num, geom_ratio, a):
    scaler = (choice_grid_max - choice_grid_min) / (stop - start)
    __, displacement, multiplier, a, b = gen_geom_grid(start, stop, num, geom_ratio, a)

    return grid_to_geom_short_core(choice_grid, a, scaler, displacement, multiplier, geom_ratio)


@jit(nopython=True, parallel=True)
def grid_to_geom_short_core(choice_grid, a, scaler, displacement, multiplier, geom_ratio):
    #     choice_grid_geom = ((choice_grid/scaler) + displacement)/multiplier
    #     but a is 1
    #     choice_grid_geom_base = (np.log(choice_grid_geom/a))/np.log(geom_ratio)

    return np.log((((choice_grid / scaler) + displacement) / multiplier) / a) / np.log(geom_ratio)


# @njit
def grid_to_geom(choice_grid, choice_grid_max, choice_grid_min,
                 start, stop, num, geom_ratio, a):
    """
    the code now is under the assumption that initial start and end were 0 and 1 
    
    Given geom_grid results, how do we go back to actual data grid. 
    So for interpolation. 
    interpolate not on actual K and B scales, but on any even grid, as long
    as the grid count is right. 
    
    interp_K_grid = np.linspace(0,1,n)
    
    but then there is a vector of actual choices kn_vec, how to map kn_vec to interp_K_grid?
    
    Parameters
    ----------
    choice_grid:
        this is the choice grid, on the actual choice scale
    start: float
        from gen_geom_grid
    stop: float
        from gen_geom_grid
    num: int
        from gen_geom_grid
    geom_ratio: float
        from gen_geom_grid        
    """
    #     logger.debug('enter grid_to_geom')

    '''
    0. Choice Grid Rescaling
    '''
    scaler = (choice_grid_max - choice_grid_min) / (stop - start)

    '''
    A. Reverse engineer from vector to geom scale
    '''
    #     startTime = time.time()
    __, displacement, multiplier, a, b = gen_geom_grid(start, stop, num, geom_ratio, a)
    #     logger.debug('displacement:%s', displacement)
    #     logger.debug('multiplier:%s', multiplier)
    #     logger.debug('a:%s', a)
    #     logger.debug('b:%s', b)
    #     t = time.time() - startTime
    #     print('Step aa:', t)

    '''choice_grid_geom is now between a and b'''
    #     startTime = time.time()
    choice_grid_geom = ((choice_grid / scaler) + displacement) / multiplier
    #     logger.debug('choice_grid:\n%s', choice_grid)
    #     logger.debug('choice_grid_geom:\n%s', choice_grid_geom)
    t = time.time() - startTime
    print('Step aaa:', t)

    '''
    B.
        a <= choice_grid_geom = a*(geom_ratio)^{x} <= b
        
        solve for x
        
        log(choice_grid_geom) = log(a) + x*log(geom_ratio)
        x = (log(choice_grid_geom) - log(a))/log(geom_ratio)
         
    '''
    startTime = time.time()
    choice_grid_geom_base = (np.log(choice_grid_geom / a)) / np.log(geom_ratio)
    #     choice_grid_geom_base = (np.log(choice_grid_geom))/np.log(geom_ratio)
    #     logger.debug('choice_grid_geom_base:\n%s', choice_grid_geom_base)
    t = time.time() - startTime
    print('Step bb:', t)

    return choice_grid_geom_base


# @njit
def gen_geom_grid(start, stop, num, geom_ratio, a):
    """    
    Specify geom_ratio, the z below:
        a*z^0=a
        a*z^1
        a*z^2
        ...
        ...
        a*z^49=b
    Then generate the grid points that is consistent with the geom_ratio
    
    Parameters
    ----------
    start: float
        same as in linspace
    stop: float
        same as in linspace
    num: int
        same as in linspace
    geom_ratio: float
        z value below kind of except for rescaling
    """

    '''
    A. Start with a and b
    '''
    #     a = 1
    b = a * geom_ratio ** (num - 1)

    geom_base = a * (geom_ratio) ** np.arange(num)
    #     geom_base2 = np.geomspace(a, b, num)
    #     logger.debug('geom_base:\n%s', geom_base)

    '''
    B. Rescaling
    '''
    multiplier = ((stop - start) / (b - a))
    geom_base_scaled = geom_base * multiplier
    #     logger.debug('geom_base_scaled:\n%s', geom_base_scaled)

    displacement = (np.min(geom_base_scaled) - start)
    geom_base_scaled = geom_base_scaled - displacement
    #     logger.debug('geom_base_scaled:\n%s', geom_base_scaled)

    #     logger.debug('geom_base_scaled diff:\n%s', np.diff(geom_base_scaled))

    return geom_base_scaled, displacement, multiplier, a, b


def tester(a=1, b=51, max_power=49):
    """
    1. 1 to 51, geomspace 
    """
    list_geom_1t51 = np.geomspace(a, b, max_power + 1)
    print('list_geom_1t51:', list_geom_1t51)

    """
    2. what is the list above, what does it mean?
    the point is to start from a=start, end at b=end, find:
    
    a*z^0=a
    a*z^1
    a*z^2
    ...
    ...
    a*z^49=b
    
    50 numbers like above. 
    a is determined by start of geomspace
    b is determined by: 
    
    """
    z = (b / a) ** (1 / max_power)
    print('z:', z)
    list_geom_fan = a * z ** np.linspace(0, max_power, max_power + 1)
    print('list_geom_fan:', list_geom_fan)

    return list_geom_fan


def tester_plus1(a=0, b=50, max_power=49, adjust=1):
    """
    to accomndate zero,  
    """
    list_geom_1t51 = np.geomspace(a + adjust, b + adjust, max_power + 1)
    list_geom_1t51 = list_geom_1t51 - 1
    print('list_geom_1t51:', list_geom_1t51)

    """
    2. what is the list above, what does it mean?
    the point is to start from a=start, end at b=end, find:
    
    a*z^0=a
    a*z^1
    a*z^2
    ...
    ...
    a*z^49=b
    
    50 numbers like above. 
    a is determined by start of geomspace
    b is determined by: 
    
    """
    z = ((b + adjust) / (a + adjust)) ** (1 / max_power)
    print('z:', z)
    list_geom_fan = (a + adjust) * z ** np.linspace(0, max_power, max_power + 1) - 1
    print('list_geom_fan:', list_geom_fan)

    """
    3. So suppose I have list_geom now, how to I take it back to geomspace?
    """
    lencount = len(list_geom_1t51)
    equi_space = np.linspace(1, lencount, lencount)
    print('equi_space:', equi_space)


if __name__ == "__main__":
    FORMAT = '%(filename)s - %(funcName)s - %(lineno)d -  %(asctime)s - %(levelname)s %(message)s'
    np.set_printoptions(precision=4, linewidth=100, suppress=True, threshold=np.nan)
    np.set_printoptions(precision=3, linewidth=100, suppress=True, threshold=3000)
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)

    tester(a=1, b=2, max_power=49)
    tester(a=1, b=3, max_power=49)
    tester(a=1, b=4, max_power=49)
    print((tester(a=1, b=5, max_power=49) - 1) / 4)
    print('')
    print('')
    print('')
    tester(a=1, b=51, max_power=49)
    tester(a=0.1, b=51, max_power=10)
    tester(a=100, b=200, max_power=3)

    tester_plus1()

    print('')
    print('')
    print('')

    start = 0
    stop = 1
    num = 11
    geom_ratio = 1.2
    gen_geom_grid(start, stop, num, geom_ratio, 1)

    start = 10
    stop = 20
    num = 11
    geom_ratio = 1.00000001
    gen_geom_grid(start, stop, num, geom_ratio, 1)

    start = -10
    stop = 20
    num = 11
    geom_ratio = 1.1
    gen_geom_grid(start, stop, num, geom_ratio, 1)

    start = -3.5
    stop = -3.1
    num = 3
    geom_ratio = 1.1
    gen_geom_grid(start, stop, num, geom_ratio, 1)

    start = 0
    stop = 1
    num = 50
    geom_ratio = 1.03
    geom_base_scaled, __, __, __, __, = gen_geom_grid(start, stop, num, geom_ratio, 1)
    choice_grid_max = stop
    choice_grid_min = start
    grid_to_geom(geom_base_scaled, choice_grid_max, choice_grid_min,
                 start, stop, num, geom_ratio, 1)

    geom_base_scaled = np.linspace(0, 30, 22)
    choice_grid_max = 30
    choice_grid_min = 0
    grid_to_geom(geom_base_scaled, choice_grid_max, choice_grid_min,
                 start, stop, num, geom_ratio, 1)
