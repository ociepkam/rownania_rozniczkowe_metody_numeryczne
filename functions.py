import time
import matplotlib.pyplot as plt
from Rungego_Kutty import rk4
from Euler import euler, euler_fast
from wielokrokowe import *


def test_speed(func, param, repeat=100):
    t0 = time.time()
    for i in range(repeat):
        func(*param)
    t1 = time.time()
    return t1 - t0


def test_met(met, x_true, tb, x0, param):
    if met.__name__ == "rk4":
        value = met(*param)[1][-1]
    elif met.__name__ == "pc":
        value = met(*param)[-1]
    else:
        value = met(*param)
    error = abs(x_true(x0, tb) - value)
    time = test_speed(met, param)
    return {"value": value, "error": error, "time": time}


def list_minus(l1, l2):
    return [a-b for a, b in zip(l1, l2)]


def metods_x(f, f_true, ta, tb, xa, n):
    e = []
    e_f = []
    f_t = []
    ab = []
    h = (tb - ta) / float(n)
    t = ta
    x_e = x_f = x_ab = xa
    while t < tb:
        x_e = euler(f, t-h, t, x_e, 1)
        x_f = euler_fast(f, t-h, t, x_f, 1)
        x_t = f_true(xa, t)
        x_ab = adams_bashforth(f, t-h, t, x_f, 1)
        e.append(x_e)
        e_f.append(x_f)
        f_t.append(x_t)
        ab.append(x_ab)
        t += h
    time = [ta + a * h for a in range(len(f_t))]
    p = pc(f, time, xa)
    r = rk4(f, ta, tb, xa, n)[1]
    return {"euler": e, "euler upgrade": e_f, "rk4": r, "adams bashforth": ab, "pc": p, "time": time, "true": f_t}


def plotting_val(f, f_true, ta, tb, xa, n):
    x = metods_x(f, f_true, ta, tb, xa, n)
    plt.plot(x["time"], x["true"], label="true value")
    plt.plot(x["time"], x["euler"], label="euler")
    plt.plot(x["time"], x["rk4"], label="rk4")
    plt.plot(x["time"], x["euler upgrade"], label="euler upgrade")
    plt.plot(x["time"], x["pc"], label="pc")
    plt.plot(x["time"], x["adams bashforth"], label="adams bashforth")
    plt.legend(loc='upper left')
    plt.show()


def plotting_error(f, f_true, ta, tb, xa, n):
    x = metods_x(f, f_true, ta, tb, xa, n)
    plt.plot(x["time"], list_minus(x["true"], x["true"]), label="true value")
    plt.plot(x["time"], list_minus(x["euler"], x["true"]), label="euler")
    plt.plot(x["time"], list_minus(x["rk4"], x["true"]), label="rk4")
    plt.plot(x["time"], list_minus(x["euler upgrade"], x["true"]), label="euler upgrade")
    plt.plot(x["time"], list_minus(x["pc"], x["true"]), label="pc")
    plt.plot(x["time"], list_minus(x["adams bashforth"], x["true"]), label="adams bashforth")
    plt.legend(loc='upper left')
    plt.show()