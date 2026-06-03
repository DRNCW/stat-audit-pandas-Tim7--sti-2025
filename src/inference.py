import numpy as np
from scipy.stats import norm, beta, chi2

def confidence_interval(theta_hat, sigma, n, confidence=0.95):
    z = norm.ppf(1 - (1 - confidence) / 2)
    margin = z * sigma / np.sqrt(n)

    lower = theta_hat - margin
    upper = theta_hat + margin

    return float(lower), float(upper)


def ci_bernoulli(k, n, confidence=0.95):
    p_hat = k / n

    z = norm.ppf(1 - (1 - confidence) / 2)
    se = np.sqrt(p_hat * (1 - p_hat) / n)

    lower = p_hat - z * se
    upper = p_hat + z * se

    lower = max(0.0, lower)
    upper = min(1.0, upper)

    return float(lower), float(upper)


def ci_poisson(data, confidence=0.95):
    data = np.asarray(data)
    total = np.sum(data)
    n = len(data)

    alpha = 1 - confidence

    lower = 0.5 * chi2.ppf(alpha / 2, 2 * total) / n

    upper = (
        0.5 * chi2.ppf(1 - alpha / 2, 2 * (total + 1))
    ) / n

    return float(lower), float(upper)


def credible_interval(alpha, beta_param, confidence=0.95):
    tail = (1 - confidence) / 2

    lower = beta.ppf(tail, alpha, beta_param)
    upper = beta.ppf(1 - tail, alpha, beta_param)

    return float(lower), float(upper)