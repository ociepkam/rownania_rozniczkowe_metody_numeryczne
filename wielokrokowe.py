import numpy
from Rungego_Kutty import rk4

ab_s1 = [1]
ab_s2 = [-0.5, 1.5]
ab_s3 = [5. / 12, -4. / 3, 23. / 12]
ab_s4 = [-9. / 24, 37. / 24, -59. / 24, 55. / 24]
ab_s5 = [251. / 720, -1274. / 720, 2616. / 720, -2774. / 720, 1901. / 720]


am_s1 = [1]
am_s2 = [0.5, 0.5]
am_s3 = [-1. / 12, 2. / 3, 5. / 12]
am_s4 = [1. / 24, -5. / 24, 19. / 24, 9. / 24]
am_s5 = [-19. / 720, 106. / 720, -264. / 720, 646. / 720, 251. / 720]


def adams_bashforth(f, ta, tb, xa, n, sn=ab_s5):
    h = (tb - ta) / float(n)
    t = ta
    x = xa
    SN = len(sn)
    # first n steps made by Euler method
    last_n = []
    for i in range(SN):
        y = h * f(t, x)
        last_n.append(y)
        x += y
        t += h
    # Adams-Bashforth method
    j = 0
    for i in range(n):
        ss = 0
        for s in sn:
            ss += last_n[j] * s
            j += 1
            if j >= SN: j = 0
        x += h * ss
        last_n[j] = f(t, x)
        t += h
        j += 1
        if j >= SN: j = 0
    return x


def pc(f, t, x0, ab=ab_s5, am=am_s5):
    n = len(t)
    x = numpy.zeros(n)
    x[0] = x0
    len_ab = len(ab)
    len_am = len(am)
    n_of_steps = max(len_ab, len_am) - 1

    # Start up with 4th order Runge-Kutta (single-step method)
    if n_of_steps > 0:
        x[:n_of_steps + 1] = rk4(f, t[0], t[n_of_steps], x0, n_of_steps)[1]
    last_f = [f(t[i], x[i]) for i in range(n_of_steps + 1)]

    # Adams-Bashforth-Moulton steps
    for i in range(n_of_steps, n - 1):
        last_f.append(f(t[i], x[i]))
        h = t[i + 1] - t[i]
        # Adams-Bashfort
        w = x[i] + h * sum([ab[-j] * last_f[-j] for j in range(1, len_ab + 1)])
        fw = f(t[i+1], w)
        # Adams-Moulton
        x[i + 1] = x[i] + h * (fw * am[-1] + sum([am[-j - 1] * last_f[-j] for j in range(1, len_am)]))
    return x
