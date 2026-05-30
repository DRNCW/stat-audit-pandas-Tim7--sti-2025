import numpy as np
from scipy.special import gammaln

def mle_bernoulli(data):
    return float(np.sum(data) / len(data))

def mle_poisson(data):
    return float(np.sum(data) / len(data))

def beta_posterior(k, m):
    return int(k + 1), int(m + 1)

def log_likelihood_bernoulli(theta, k, n):
    theta = np.clip(theta, 1e-12, 1.0 - 1e-12)
    return float(k * np.log(theta) + (n - k) * np.log(1 - theta))

def log_likelihood_poisson(lam, data_array):
    if lam <= 0:
        return -np.inf
    n = len(data_array)
    sum_data = np.sum(data_array)
    return float(-n * lam + np.log(lam) * sum_data - np.sum(gammaln(data_array + 1)))