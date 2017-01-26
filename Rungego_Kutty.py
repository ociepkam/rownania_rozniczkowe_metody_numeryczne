def rk4(f, ta, tb, xa, n):
    vt = [0] * (n + 1)
    vx = [0] * (n + 1)
    h = (tb - ta) / float(n)
    vt[0] = t = ta
    vx[0] = x = xa
    for i in range(1, n + 1):
        k1 = h * f(t, x)
        k2 = h * f(t + 0.5 * h, x + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, x + 0.5 * k2)
        k4 = h * f(t + h, x + k3)
        vt[i] = t = ta + i * h
        vx[i] = x = x + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vt, vx