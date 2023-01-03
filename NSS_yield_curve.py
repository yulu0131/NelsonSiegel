import numpy as np
from scipy.optimize import minimize

# Nelson-Siegel-Svensson Model
def nss(nss_params, t):
    beta0, beta1, beta2, beta3, lambda1, lambda2 = nss_params
    factor1 = ((1 - np.exp(-t / lambda1)) / t / lambda1)
    factor2 = ((1 - np.exp(-t / lambda1)) / t / lambda1) - np.exp(-t / lambda1)
    factor3 = ((1 - np.exp(-t / lambda2)) / t / lambda2) - np.exp(-t / lambda2)
    fitted = beta0 + beta1*factor1 + beta2*factor2 + beta3*factor3
    return fitted

# define function to calculate errors

def nss_curve_fit(ttm, bond_rates):
    def error_func(nss_params):
        return ((nss(nss_params, ttm) - bond_rates) ** 2).sum()

    initial_guess = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    res = minimize(
        error_func,
        initial_guess
    )

    return res.x


if __name__ == "__main__":
    import pandas as pd

    # import data from csv
    yield_curve_df = pd.read_csv('yield_data/Short-term_20221214.csv')
    t = yield_curve_df.bond_ttm
    rates = yield_curve_df.risk_free_rate
    params = nss_curve_fit(t, rates)
    tenors = np.linspace(0.25, 10)
    fitted_data = nss(params, t)
    print(fitted_data)