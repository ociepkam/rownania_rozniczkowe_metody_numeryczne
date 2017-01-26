def euler(f, ta, tb, xa, n):
    h = (tb - ta) / float(n)
    t = ta
    x = xa
    for i in range(n):
        x += h * f(t, x)
        t += h
    return x


def euler2(f, ta, tb, xa, x1a, n):
    h = (tb - ta) / float(n)
    t = ta
    x = xa
    x1 = x1a
    for i in range(n):
        x1 += h * f(t, x, x1)
        x += h * x1
        t += h
    return x


def euler_fast(f, ta, tb, xa, n):
    h = (tb - ta) / float(n)
    t = ta
    x = xa
    for i in range(n):
        k1 = h * f(t, x)
        k2 = h * f(t + h, x + k1)
        x += 0.5 * (k1 + k2)
        t += h
    return x


def euler_fast2(f, ta, tb, xa, n):
    h = (tb - ta) / float(n)
    t = ta
    x = xa
    for i in range(n):
        k1 = h * f(t, x)
        k2 = h * f(t + h/2., x + k1/2.)
        x += k2
        t += h
    return x
