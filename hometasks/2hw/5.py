def get_pyth_triple(n):
    return [(i**2 - j**2, 2*i*j, i**2 + j**2) for i in range(2, n) for j in range(1, i - 1) if i**2 + j**2 <= n]
