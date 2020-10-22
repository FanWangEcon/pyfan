## ----global_options, include = FALSE-------------------------------------------------------------------------------------------
try(source("../../../.Rprofile"))


## Parameters

## ----------

## n : int

##     The upper limit of the range to generate, from 0 to `n` - 1.

## param1 : int

##     The first parameter.

## param1 : str

##     Description of `param1`.

## msg : str

##     Human readable string describing the exception.

## param1 : int

##     The first parameter.

## param2 : str

##     The second parameter.

## param3 : str, optional

##     The second parameter.


## Parameters

## ----------

## param2 : :obj:`str`, optional

##     The second parameter.

## code : :obj:`int`, optional

##     Numeric error code.

## param3 : :obj:`int`, optional

##     Description of `param3`.

## param4 : :obj:`list` of :obj:`str`

##     Description of `param2`. Multiple

##     lines are supported.


## Parameters

## ----------

## *args

##     Variable length argument list.

## **kwargs

##     Arbitrary keyword arguments.


## Returns

## -------

## numpy.array of shape (1, it_draws)

##     A vector of sorted or unsorted random grid points, or equi-quantile

##     points.


## Examples

## --------

## >>> fl_mu = 0

## >>> fl_sd = 1

## >>> it_draws = 5

## >>> it_seed = 123

## >>> fl_lower_sd = -1

## >>> fl_higher_sd = 0.8

## >>> it_draw_type = 0

## >>> ar_draw_random_normal(fl_mu, fl_sd, it_draws,

## ...                       it_seed, it_draw_type,

## ...                       fl_lower_sd, fl_higher_sd)

## [-1.          0.8         0.2829785 - 1. - 0.57860025]

## >>> it_draw_type = 1

## >>> ar_draw_random_normal(fl_mu, fl_sd, it_draws,

## ...                       it_seed, it_draw_type,

## ...                       fl_lower_sd, fl_higher_sd)

## [-1. - 0.47883617 - 0.06672597  0.3338994   0.8]

## >>> it_draw_type = 2

## >>> ar_draw_random_normal(fl_mu, fl_sd, it_draws,

## ...                       it_seed, it_draw_type,

## ...                       fl_lower_sd, fl_higher_sd)

## [-1. - 1. - 0.57860025  0.2829785   0.8]

