import numpy as np
from scipy.optimize import minimize

# Nelson-Siegel Model
def ns(ns_params, t):
    beta0, beta1, beta2, lam = ns_params
    factor1 = beta0
    factor2 = beta1 * ((1 - np.exp(-t / lam)) / t / lam)
    factor3 = beta2 * ((1 - np.exp(-t / lam)) / t / lam) - np.exp(-t / lam)
    fitted = factor1 + factor2 + factor3
    return fitted

# define function to calculate errors

def ns_curve_fit(t, rates):
    def Error(ns_params, t, rates):
        return ((ns(ns_params, t) - rates) ** 2).sum()

    initial_guess = np.array([1.0, 1.0, 1.0, 1.0])
    res = minimize(
        Error,
        initial_guess,
        args=(t, rates)
    )

    return res.x

# model calibration
def ns_ols():
    pass

if __name__ == "__main__":
    import pandas as pd

    # import data from csv
    yield_curve_df = pd.read_csv('yield_data/Short-term_20221214.csv')
    t = yield_curve_df.bond_ttm
    rates = yield_curve_df.risk_free_rate
    params = ns_curve_fit(t, rates)
    fitted_data = ns(params, t)
    print(fitted_data)