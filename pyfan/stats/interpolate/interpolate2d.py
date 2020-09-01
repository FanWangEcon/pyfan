'''
Created on Mar 7, 2017

@author: fan
'''

import numpy as np
import scipy.interpolate as interpolate
import statsmodels.api as sm


def exp_value_interpolate_bp(prod_inst, util_opti,
                             b_ssv_sd, k_ssv_sd, epsilon_ssv_sd,
                             b_ssv, k_ssv, epsilon_ssv,
                             b_ssv_zr, k_ssv_zr, epsilon_ssv_zr,
                             states_vfi_dim, shocks_vfi_dim):
    """interpolate value function and expected value function. 
        
    Need three matrix here:
    1. state matrix x shock matrix where optimal choices were solved at
        - previously, shock for this = 0, but now shock vector might not be zero
    2. state matrix x shock matrix where shocks are drawn monte carlo way to allow 
        for averaging, integrating over shocks for each x row
    3. state matrix alone, shock = 0, each of the x row in matrix x
    
    """

    'A Get States to Integrate over'
    k_alpha_ae_sd, b_ssv_sd, \
    k_alpha_ae, b_ssv, \
    k_alpha_ae_zr, b_ssv_zr = \
        inter_states_bp(prod_inst, util_opti,
                        b_ssv_sd, k_ssv_sd, epsilon_ssv_sd,
                        b_ssv, k_ssv, epsilon_ssv,
                        b_ssv_zr, k_ssv_zr, epsilon_ssv_zr,
                        states_vfi_dim, shocks_vfi_dim)

    'B. invoke'
    util_emax = \
        exp_value_interpolate_main(u1=util_opti,
                                   x1=k_alpha_ae_sd, y1=b_ssv_sd,
                                   x2=k_alpha_ae, y2=b_ssv,
                                   x2_noshk=k_alpha_ae_zr, y2_noshk=b_ssv_zr,
                                   states_dim=states_vfi_dim, shocks_dim=shocks_vfi_dim,
                                   return_uxy=False)
    'C. collect'
    interpolant_exp_v = {'evu': util_emax, 'kae': k_alpha_ae_zr, 'b': b_ssv_zr}

    return interpolant_exp_v


def inter_states_bp(prod_inst, util_opti,
                    b_ssv_sd, k_ssv_sd, epsilon_ssv_sd,
                    b_ssv, k_ssv, epsilon_ssv,
                    b_ssv_zr, k_ssv_zr, epsilon_ssv_zr,
                    states_vfi_dim, shocks_vfi_dim):
    """interpolate value function and expected value function. 
        
    Need three matrix here:
    1. state matrix x shock matrix where optimal choices were solved at
        - previously, shock for this = 0, but now shock vector might not be zero
    2. state matrix x shock matrix where shocks are drawn monte carlo way to allow 
        for averaging, integrating over shocks for each x row
    3. state matrix alone, shock = 0, each of the x row in matrix x
    
    """

    'A. k_alpha_ae variables'
    k_alpha_sd = prod_inst.k_alpha(k_ssv_sd)
    k_alpha_ae_sd = prod_inst.k_alpha_ae(epsilon=epsilon_ssv_sd, k_alpha=k_alpha_sd)

    k_alpha = prod_inst.k_alpha(k_ssv)
    k_alpha_ae = prod_inst.k_alpha_ae(epsilon=epsilon_ssv, k_alpha=k_alpha)

    k_alpha_zr = prod_inst.k_alpha(k_ssv_zr)
    k_alpha_ae_zr = prod_inst.k_alpha_ae(epsilon=epsilon_ssv_zr, k_alpha=k_alpha_zr)

    #     y1 = b_ssv_sd
    #     y2 = b_ssv
    #     y3_noshk = b_ssv_zr

    return k_alpha_ae_sd, b_ssv_sd, k_alpha_ae, b_ssv, k_alpha_ae_zr, b_ssv_zr


def exp_value_interpolate_main(u1, x1, y1,
                               x2, y2,
                               x2_noshk, y2_noshk,
                               states_dim, shocks_dim,
                               return_uxy=False):
    #     interpolant_v(xnew, ynew)
    #         interpolant_v(1,2)
    #     interpolant_v([1,2],[3,4])
    #     interpolant_v(x2[0:3], y2[0:3])
    #
    #     xnew = np.arange(-5.01, 5.01, 1e-2)
    #     ynew = np.arange(-5.01, 5.01, 1e-2)
    #
    #     interpolate.griddata((x1,y1),u1, (x2,y2)).shape

    'A. Get Interpolant'
    #     u2 = interpolate.griddata((x1,y1), u1, (x2,y2), method='linear')
    u2 = interp_griddata(cur_u=u1, cur_x1=x1, cur_x2=y1,
                         new_x1=x2, new_x2=y2)
    'B2. Reshape u2, average over shocks'
    u2_mean = np.mean(np.reshape(u2, (int(states_dim), int(shocks_dim))), axis=1)

    """
    'A. Get Interpolant'    
    interpolant_v = interpolate.interp2d(x1, y1, u1)
    v_regress = regress(u1, regress_mat(x1, y1))
    
    'B1. Get value for another matrix'
    u2 = interpolant_v(x2, y2)
    
    'B2. Reshape u2, average over shocks'
    u2_mean = np.mean(np.reshape(u2, (states_dim, shocks_dim)), axis=1)
    
    'C. Interpolate again, at average values'
    interpolant_exp_v = interp2d(x2_noshk, y2_noshk, u2_mean)    
    exp_v_regress = regress(u2_mean, regress_mat(x2_noshk, y2_noshk))
    """

    'D. States and U Collection'
    if (return_uxy == True):
        uxy_coll = [[u1, x1, y1],
                    [u2, x2, y2],
                    [u2_mean, x2_noshk, y2_noshk]]
        return uxy_coll
    else:
        return u2_mean


def exp_value_interpolate_bpkp(hhp_inst, util_opti, b, k, b_shk, k_shk):
    """interpolate value function and expected value function. 
    
    cash and k_alpha calculation below does not repeat what happened already inside
    lifetimeutility. Inside lifetimeutility, we have next period cash and k_alpha
    here is this period    
    """

    # First Level Interpoalte
    cash, k_alpha = k_alpha_cash(hhp_inst, b, k)

    interpolant_v = interp2d(k_alpha, cash, util_opti)
    v_regress = regress(util_opti, regress_mat(k_alpha, cash))

    # Evaluate with shocks
    cash_shk, k_alpha_shks = k_alpha_cash(hhp_inst, b_shk, k_shk)
    util_opti_interp_shk = interpolant_v(k_alpha_shks, cash_shk)

    # Average over    
    util_opti_interp_shk_mean = np.mean(np.reshape(util_opti_interp_shk, \
                                                   (hhp_inst.states_dim, hhp_inst.shocks_dim)), axis=1)

    # Second Tier Interpolate
    interpolant_exp_v = interp2d(k_alpha, cash, util_opti_interp_shk_mean)
    exp_v_regress = regress(util_opti_interp_shk_mean, regress_mat(k_alpha, cash))

    return interpolant_exp_v, exp_v_regress


def k_alpha_cash(hhp_inst, b_vec, k_vec):
    cash_vec = hhp_inst.bdgt_inst.cash(b_vec, k_vec)
    k_alpha_vec = hhp_inst.prod_inst.k_alpha(k_vec)
    return cash_vec, k_alpha_vec


def interp_griddata(cur_u, cur_x1, cur_x2, new_x1, new_x2):
    """Centralize the invokation of 2D interpolation tool
    
    Potentially chagne this to something else if I don't like it. 
    """
    cur_x1 = np.ravel(cur_x1)
    cur_x2 = np.ravel(cur_x2)
    cur_u = np.ravel(cur_u)
    #     new_x1 = np.ravel(new_x1)
    #     new_x2 = np.ravel(new_x2)

    new_u = interpolate.griddata((cur_x1, cur_x2), cur_u,
                                 (new_x1, new_x2), method='linear')

    #     print('')
    #     print('cur_u:',np.min(cur_u),np.max(cur_u), cur_u.shape)
    #     print('cur_x1:',np.min(cur_x1),np.max(cur_x1),np.mean(cur_x1),cur_x1.shape)
    #     print('cur_x2:',np.min(cur_x2),np.max(cur_x2),np.mean(cur_x2),cur_x2.shape)
    #     print('new_x1:',np.min(new_x1),np.max(new_x1),np.mean(new_x1),new_x1.shape)
    #     print('new_x2:',np.min(new_x2),np.max(new_x2),np.mean(new_x2),new_x2.shape)
    #     print('new_u:',np.min(new_u),np.max(new_u),np.mean(new_u), new_u.shape)
    #     print('')

    return new_u


def interp2d(prod, cash, z=None, interpolant=None, kind='linear'):
    """Centralize the invokation of 2D interpolation tool
    
    Potentially chagne this to something else if I don't like it. 
    """

    if (interpolant == None):
        interpolant = interpolate.interp2d(
            prod.flatten(), cash.flatten(), z.flatten(), kind=kind)
        return interpolant
    else:
        evaluated = interpolant(prod.flatten(), cash.flatten())
        return evaluated


def interpRbf2D(prod, cash, z=None, interpolant=None, kind='linear'):
    #     https://stackoverflow.com/questions/37872171/how-can-i-perform-two-dimensional-interpolation-using-scipy

    if (interpolant == None):
        # default smooth=0 for interpolation
        interpolant = interpolate.Rbf(
            prod.flatten(), cash.flatten(), z.flatten(), function='cubic', smooth=0)

        return interpolant
    else:

        evaluated = interpolant(prod.flatten(), cash.flatten())
        return evaluated


def interpRbf3D(prod, cash, A, z=None, interpolant=None, kind='cubic'):
    #     https://stackoverflow.com/questions/37872171/how-can-i-perform-two-dimensional-interpolation-using-scipy

    if (interpolant == None):
        # default smooth=0 for interpolation
        interpolant = interpolate.Rbf(
            prod.flatten(), cash.flatten(), A.flatten(),
            z.flatten(), function='cubic', smooth=0)

        return interpolant
    else:

        evaluated = interpolant(prod.flatten(), cash.flatten(), A.flatten())
        return evaluated


def regress_mat(k_alpha, cash):
    if ((k_alpha is None) and (cash is None)):
        reg_mat_col_count = 3
        return reg_mat_col_count
    else:
        const = np.zeros(len(k_alpha)) + 1
        regress_mat = np.column_stack((const, k_alpha, cash))
        return regress_mat


def regress(dependent_var, rhs_var):
    model = sm.OLS(dependent_var, rhs_var)

    results = model.fit()
    beta = results.params
    tstats = results.tvalues

    return {'beta': beta, 'tstats': tstats}

# if __name__ == '__main__':
# 
#     import numpy as np
#     import time as time 
#     import scipy.interpolate as interpolate
#     
#     def func(x, y):
#         return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2
#     
#     grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]
#     
#     points = np.random.rand(1000, 2)
#     values = func(points[:,0], points[:,1])
#     
#     startTime = time.time()
#     for i in np.arange(1000):
#             
#         grid_z1 = interpolate.griddata(points, values, (grid_x, grid_y), method='linear')
#     t = time.time() - startTime
#     print(t)
#
