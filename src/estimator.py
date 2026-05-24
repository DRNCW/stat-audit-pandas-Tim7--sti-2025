
import math 

def mle_bernoulli(k, n):
    """
    Menghitung Maximum Likelihood Estimation (MLE) untuk distribusi Bernoulli.
    k = jumlah kejadian sukses (misal: PR yang di-merge)
    n = jumlah total percobaan (misal: total PR)
    """
    if n == 0:
        return 0
    return k / n

def mle_poisson(data_list):
    """
    Menghitung Maximum Likelihood Estimation (MLE) untuk distribusi Poisson.
    data_list = list/array dari data diskrit.
    """
    if len(data_list) == 0:
        return 0
    return sum(data_list) / len(data_list)

def beta_posterior(k, m):
    """
    Menghitung parameter Alpha dan Beta untuk distribusi Posterior Beta.
    Wajib menggunakan prior Uniform Beta(1,1), sehingga rumusnya menjadi +1.
    k = kejadian sukses
    m = kejadian gagal
    """
    alpha_post = k + 1
    beta_post = m + 1
    return alpha_post, beta_post

def beta_mode(alpha, beta):
    """
    Menghitung mode dari distribusi Beta.
    
    Rumus:
    mode = (alpha - 1) / (alpha + beta - 2)

    Syarat:
    alpha > 1 dan beta > 1
    """
    if alpha <= 1 or beta <= 1:
        return "Mode tidak terdefinisi untuk alpha <= 1 atau beta <= 1"
    
    return (alpha - 1) / (alpha + beta - 2)


def beta_mean(alpha, beta):
    """
    Menghitung mean/rata-rata dari distribusi Beta.
    
    Rumus:
    mean = alpha / (alpha + beta)
    """
    if (alpha + beta) == 0:
        return 0
    
    return alpha / (alpha + beta)

def log_likelihood_bernoulli(theta, k, n):
    """
    Menghitung log-likelihood distribusi Bernoulli.

    theta = probabilitas sukses
    k     = jumlah sukses
    n     = total percobaan

    Rumus:
    log L(theta) = k*log(theta) + (n-k)*log(1-theta)
    """

    if theta <= 0 or theta >= 1:
        return float('-inf')

    return (k * math.log(theta)) + ((n - k) * math.log(1 - theta))


def log_likelihood_poisson(theta, data):
    """
    Menghitung log-likelihood distribusi Poisson.

    theta = parameter lambda Poisson
    data  = list/array data diskrit

    Rumus:
    log L(theta) = Σ [x_i * log(theta) - theta - log(x_i!)]
    """

    if theta <= 0:
        return float('-inf')

    log_likelihood = 0

    for x in data:
        log_likelihood += (
            x * math.log(theta)
            - theta
            - math.log(math.factorial(x))
        )

    return log_likelihood
