import numpy as np
from scipy.special import factorial

def mle_bernoulli(data):
    """
    Calculates the Maximum Likelihood Estimator for a Bernoulli distribution.
    Formula: theta_hat = k / n (Tsun, 2020, p. 254)
    """
    n = len(data)
    if n == 0:
        return 0.0
    k = np.sum(data)
    return float(k / n)

def mle_poisson(data):
    """
    Calculates the Maximum Likelihood Estimator for a Poisson distribution.
    Formula: lambda_hat = sum(data) / len(data) (Tsun, 2020, p. 254)
    """
    n = len(data)
    if n == 0:
        return 0.0
    return float(np.sum(data) / n)

def beta_posterior(k, m):
    """
    Calculates the Beta posterior parameters and its mode and mean.
    Formula: alpha = k + 1, beta = m + 1 (Tsun, 2020, p. 269)
    Mode: (alpha - 1) / (alpha + beta - 2) (Tsun, 2020, p. 269)
    Mean: alpha / (alpha + beta) (Tsun, 2020, p. 269)
    """
    alpha = int(k + 1)
    beta = int(m + 1)
    
    mode = float((alpha - 1) / (alpha + beta - 2))
    mean = float(alpha / (alpha + beta))
    
    return {
        "alpha": alpha,
        "beta": beta,
        "mode": mode,
        "mean": mean
    }

def log_likelihood_bernoulli(theta, k, n):
    """
    Computes the log-likelihood for a Bernoulli distribution.
    Formula: ln L(theta) = k * ln(theta) + (n - k) * ln(1 - theta)
    """
    theta = np.clip(theta, 1e-12, 1.0 - 1e-12)
    return float(k * np.log(theta) + (n - k) * np.log(1 - theta))

def log_likelihood_poisson(lam, data):
    """
    Computes the log-likelihood for a Poisson distribution.
    Formula: ln L(lambda) = -n*lambda + ln(lambda)*sum(data) - sum(ln(x!))
    """
    if lam <= 0:
        return -np.inf
    n = len(data)
    sum_data = np.sum(data)
    # Gunakan pendekatan log-gamma untuk menghindari overflow pada pencarian nilai faktorial besar
    from scipy.special import gammaln
    return float(-n * lam + np.log(lam) * sum_data - np.sum(gammaln(data + 1)))