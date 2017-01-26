import math
import numpy

from prettytable import PrettyTable

from Rungego_Kutty import rk4
from Euler import euler, euler_fast
from wielokrokowe import *
from functions import *


# porownanie z innymi metodami
def t_1():
    def dx(t, x):
        return t * x

    def x_true(xa, tb):
        return xa * math.exp(0.5 * tb * tb)

    ta = 0.
    tb = 1.
    x0 = 10.
    n = 10
    t = numpy.linspace(ta, tb, n + 1)

    test_euler = test_met(euler, x_true, tb, x0, (dx, ta, tb, x0, n))
    test_euler_fast = test_met(euler_fast, x_true, tb, x0, (dx, ta, tb, x0, n))
    test_rk4 = test_met(rk4, x_true, tb, x0, (dx, ta, tb, x0, n))
    test_adams_bashforth = test_met(adams_bashforth, x_true, tb, x0, (dx, ta, tb, x0, n))
    test_pc = test_met(pc, x_true, tb, x0, (dx, t, x0))

    x = PrettyTable()
    x.field_names = ["Nazwa metody", "Wynik obliczen", "Blad", "Czas wykonania operacji"]
    x.add_row(["Rozwiazanie dokladne", x_true(x0, tb), "", ""])
    x.add_row(["Metoda Eulera", test_euler["value"], test_euler["error"], test_euler["time"]])
    x.add_row(["Ulepszona metoda Eulera", test_euler_fast["value"], test_euler_fast["error"], test_euler_fast["time"]])
    x.add_row(["Metoda Rungego-Kutty", test_rk4["value"], test_rk4["error"], test_rk4["time"]])
    x.add_row(["Metoda Adamsa-Bashfortha", test_adams_bashforth["value"], test_adams_bashforth["error"],
               test_adams_bashforth["time"]])
    x.add_row(["Metoda predyktor-korektor", test_pc["value"], test_pc["error"], test_pc["time"]])
    x.align = "l"
    print x

    plotting_val(dx, x_true, ta, tb, x0, n)
    plotting_error(dx, x_true, ta, tb, x0, n)


# taki sam blad
def t_2():
    def dx(t, x):
        return t * x

    def x_true(xa, tb):
        return xa * math.exp(0.5 * tb * tb)

    ta = 0
    tb = 2
    x0 = 10
    n_e = 34478
    n_e_f = 140
    n_rk4 = 10
    n_a_b = 118235
    n_pc = 35
    t = numpy.linspace(ta, tb, n_pc + 1)

    test_euler = test_met(euler, x_true, tb, x0, (dx, ta, tb, x0, n_e))
    test_euler_fast = test_met(euler_fast, x_true, tb, x0, (dx, ta, tb, x0, n_e_f))
    test_rk4 = test_met(rk4, x_true, tb, x0, (dx, ta, tb, x0, n_rk4))
    test_adams_bashforth = test_met(adams_bashforth, x_true, tb, x0, (dx, ta, tb, x0, n_a_b))
    test_pc = test_met(pc, x_true, tb, x0, (dx, t, x0, ab_s3, am_s3))

    x = PrettyTable()
    x.field_names = ["Nazwa metody", "Wynik obliczen", "Blad", "Czas wykonania operacji", "n"]
    x.add_row(["Rozwiazanie dokladne", x_true(x0, tb), "", "", ""])
    x.add_row(["Metoda Eulera", test_euler["value"], test_euler["error"], test_euler["time"], n_e])
    x.add_row(
        ["Ulepszona metoda Eulera", test_euler_fast["value"], test_euler_fast["error"], test_euler_fast["time"], n_e_f])
    x.add_row(["Metoda predyktor-korektor 3", test_pc["value"], test_pc["error"], test_pc["time"], n_pc])
    x.add_row(["Metoda Rungego-Kutty", test_rk4["value"], test_rk4["error"], test_rk4["time"], n_rk4])
    x.add_row(["Metoda Adamsa-Bashfortha", test_adams_bashforth["value"], test_adams_bashforth["error"],
               test_adams_bashforth["time"], n_a_b])

    x.align = "l"
    print x


def t_3():
    def dx(t, x):
        return -5 * x

    def x_true(xa, tb):
        return xa * math.exp(-5 * tb)

    ta = 0
    tb = 2
    x0 = 100
    n = 20
    t = numpy.linspace(ta, tb, n + 1)

    am = [am_s1, am_s2, am_s3, am_s4, am_s5]
    ab = [ab_s1, ab_s2, ab_s3, ab_s4, ab_s5]

    test_pc = [test_met(pc, x_true, tb, x0, (dx, t, x0, ab_i, am_i)) for am_i, ab_i in zip(am, ab)]
    x = PrettyTable()
    x.field_names = ["Nazwa metody", "Wynik obliczen", "Blad", "Czas wykonania operacji", "liczba krokow"]
    x.add_row(["Rozwiazanie dokladne", x_true(x0, tb), "", "", ""])
    for idx, p in enumerate(test_pc):
        x.add_row(["Metoda predyktor-korektor", p["value"], p["error"], p["time"], idx + 1])
    x.align = "l"
    print x

    f_t = []
    for elem in t:
        f_t.append(x_true(x0, elem))
    plt.plot(t, f_t, label="true value")
    for ab_i, am_i in zip(ab, am):
        x = pc(dx, t, x0, ab_i, am_i)
        plt.plot(t, x, label="pc " + str(len(ab_i)))
    plt.legend(loc='upper left')
    plt.show()

    f_t = [x_true(x0, tb)] * len(t)
    for ab_i, am_i in zip(ab, am):
        x = pc(dx, t, x0, ab_i, am_i)
        plt.plot(t, list_minus(x, f_t), label="pc " + str(len(ab_i)))
    plt.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    t_1()
    t_2()
    t_3()
