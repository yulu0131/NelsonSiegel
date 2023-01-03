import numpy as np
from scipy.optimize import minimize

# Nelson-Siegel Model
def ns(ns_params, ttm):
    beta0, beta1, beta2, lam = ns_params
    factor1 = ((1 - np.exp(-ttm / lam)) / ttm / lam)
    factor2 = ((1 - np.exp(-ttm / lam)) / ttm / lam) - np.exp(-ttm / lam)
    fitted = beta0 + beta1*factor1+beta2*factor2
    return fitted

# define function to calculate errors
def ns_curve_fit(ttm, bond_rates):
    def error_func(ns_params):
        return ((ns(ns_params, ttm) - bond_rates) ** 2).sum()

    initial_guess = np.array([1.0, 1.0, 1.0, 1.0])
    res = minimize(
        error_func,
        initial_guess
    )

    return res.x

# model calibration
from numpy.linalg import lstsq

#initial guess of lambda for curve optimization required
def betas_ns_ols(lam, ttm, bond_rates):
    factor1 = ((1 - np.exp(-ttm / lam)) / ttm / lam)
    factor2 = ((1 - np.exp(-ttm / lam)) / ttm / lam) - np.exp(-ttm / lam)
    constant = np.ones(factor1.size)
    factor_matrix = np.stack([constant, factor1, factor2]).transpose()
    # calculate best-fitting beta given parameter lambda
    lstsq_res = lstsq(factor_matrix, bond_rates, rcond=None)
    betas = lstsq_res[0]
    fitted = betas[0] + betas[1]*factor1 + betas[2]*factor2
    return fitted, betas

def ns_ols_fit(ttm, bond_rates):
    def error_ns_ols(lamda_value):
        fitted, betas_value = betas_ns_ols(lamda_value, ttm, bond_rates)
        return ((fitted - bond_rates) ** 2).sum()

    initial_guess = 1.0
    res = minimize(
        error_ns_ols,
        initial_guess
    )

    lam = res.x
    fitted_curve, betas = betas_ns_ols(lam, ttm, bond_rates)

    return betas[0], betas[1], betas[2], lam

if __name__ == "__main__":
    # load data
    import pandas as pd
    yield_curve_df = pd.read_csv('yield_data/Short-term_20221214.csv')
    t = yield_curve_df.bond_ttm
    # test NS model
    rates = yield_curve_df.risk_free_rate
    params = ns_curve_fit(t, rates)
    fitted_data = ns(params, t)
    print("original fitted NS", fitted_data)

    # test calibrated data
    ols_params = ns_ols_fit(t, rates)
    ols_data = ns(ols_params, t)
    print("calibrated NS", ols_data)