'''
Created on Dec 2, 2017

@author: fan
'''

import numpy as np

def scalar_to_2darray(x, check_first=True):
    input_is_scalar = False
    if (check_first is True):
        if (np.isscalar(x)):
            input_is_scalar = True
        else:
            input_is_scalar = False

    if (input_is_scalar is True):
        x = np.asarray([[x]])
    else:
        pass

    return x

def scalar_to_array(x, check_first=True):
    input_is_scalar = False
    if (check_first is True):
        if (np.isscalar(x)):
            input_is_scalar = True
        else:
            input_is_scalar = False

    if (input_is_scalar is True):
        x = np.asarray(x)
        x = x[None]
    else:
        pass

    return x


def zero_ndims(ndims_var):
    """
    Parameters
    ----------
    ndims_var: array
        the dimension of this array to be duplicated

    """
    zero_array = 0
    if (np.isscalar(ndims_var)):
        zero_array = 0
    else:
        ndims = ndims_var.ndim
        if (ndims==1):
            zero_array = np.zeros(1)
        if (ndims==2):
            zero_array = np.zeros((1,1))
        if (ndims==3):
            zero_array = np.zeros((1,1,1))

    return zero_array


# # https://stackoverflow.com/questions/29318459/python-function-that-handles-scalar-or-arrays
# def func_for_scalars_or_vectors(x):
#     x = np.asarray(x)
#     scalar_input = False
#     if x.ndim == 0:
#         x = x[None]  # Makes x 1D
#         scalar_input = True
#
#     # The magic happens here
#
#     if scalar_input:
#         return np.squeeze(ret)
#     return ret

if __name__ == '__main__':

    print(scalar_to_array(1.0).shape)
    print(scalar_to_2darray(1.0).shape)

    print(scalar_to_2darray(np.array([1,2,3,4])).shape)
