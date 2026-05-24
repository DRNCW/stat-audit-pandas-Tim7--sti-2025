import math

def mle_bernoulli(k, n):
    """
    Maximum Likelihood Estimation (MLE)
    untuk distribusi Bernoulli.
    """

    if n == 0:
        return 0

    return k / n


def beta_posterior(k, m):
    """
    Menghitung parameter posterior Beta
    dengan prior Uniform Beta(1,1).
    """

    alpha_post = k + 1
    beta_post = m + 1

    return alpha_post, beta_post


def beta_mean(alpha, beta):
    """
    Mean distribusi Beta.
    """

    if (alpha + beta) == 0:
        return 0

    return alpha / (alpha + beta)


def beta_mode(alpha, beta):
    """
    Mode distribusi Beta.
    """

    if alpha <= 1 or beta <= 1:
        return None

    return (alpha - 1) / (alpha + beta - 2)


def log_likelihood_bernoulli(theta, k, n):
    """
    Log-likelihood distribusi Bernoulli.
    """

    if theta <= 0 or theta >= 1:
        return float("-inf")

    return (
        k * math.log(theta)
        + (n - k) * math.log(1 - theta)
    )


def mle_poisson(data_list):
    """
    Maximum Likelihood Estimation (MLE)
    untuk distribusi Poisson.
    """

    if len(data_list) == 0:
        return 0

    return sum(data_list) / len(data_list)


def log_likelihood_poisson(theta, data):
    """
    Log-likelihood distribusi Poisson.
    """

    if theta <= 0:
        return float("-inf")

    log_likelihood = 0

    for x in data:
        log_likelihood += (
            x * math.log(theta)
            - theta
            - math.log(math.factorial(x))
        )

    return log_likelihood