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

def beta_posterior_params(k, m):
    """
    Menghitung parameter Alpha dan Beta untuk distribusi Posterior Beta.
    Wajib menggunakan prior Uniform Beta(1,1), sehingga rumusnya menjadi +1.
    k = kejadian sukses
    m = kejadian gagal
    """
    alpha_post = k + 1
    beta_post = m + 1
    return alpha_post, beta_post