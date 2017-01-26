    Projekt programistyczny z przedmiotu Równania Różniczkowe
    Autor: Michał Ociepka
    Temat: Algorytm Predyktor-Korektor, porównanie z innymi metodami
    
    Aby uruchomić program potrzebny jest Python 2.* oraz następujące biblioteki:
        - numpy
        - matplotlib (używane tylko do porównywania metod)
        - prettytable (używane tylko do porównywania metod)


    Zawartość projektu:
    
    1) Euler.py
        - euler(f, ta, tb, xa, n)
            * służy do obliczania numerycznego metodą Eulera równań postaci x' = f(t, x)
            * f - funckcja dwuargumentowa f(t, x)
            * ta - początek predziału
            * tb - koniec przedziału
            * xa - wartość funkcji w ta
            * n - liczba kroków metody (podział przedziłu [ta, tb] na n części
            * zwraca wartość funkcji w chwili tb
        - euler2(f, ta, tb, xa, x1a, n)
            * służy do obliczania numerycznego metodą Eulera równań postaci x'' = f(t, x, x')
            * f - funckcja trzyargumentowa f(t, x, x')
            * ta - początek predziału
            * tb - koniec przedziału
            * xa - wartość funkcji w ta
            * x1a - wartość pochodnej funkcji w ta
            * n - liczba kroków metody (podział przedziłu [ta, tb] na n części
            * zwraca wartość funkcji w chwili tb
        - euler_fast(f, ta, tb, xa, n)
            * służy do obliczania numerycznego zmodyfikowaną metodą Eulera równań postaci x' = f(t, x)
            * f - funckcja dwuargumentowa f(t, x)
            * ta - początek predziału
            * tb - koniec przedziału
            * xa - wartość funkcji w ta
            * n - liczba kroków metody (podział przedziłu [ta, tb] na n części
            * zwraca wartość funkcji w chwili tb
        - euler_fast2(f, ta, tb, xa, n)
            * służy do obliczania numerycznego ulepszoną metodą Eulera równań postaci x' = f(t, x)
            * f - funckcja dwuargumentowa f(t, x)
            * ta - początek predziału
            * tb - koniec przedziału
            * xa - wartość funkcji w ta
            * n - liczba kroków metody (podział przedziłu [ta, tb] na n części
            * zwraca wartość funkcji w chwili tb
            
    2) Rungego_Kutty.py
        - rk4(f, ta, tb, xa, n)
            * służy do obliczania numerycznego metodą Rungego Kutty 4 równań postaci x' = f(t, x)
            * f - funckcja dwuargumentowa f(t, x)
            * ta - początek predziału
            * tb - koniec przedziału
            * xa - wartość funkcji w ta
            * n - liczba kroków metody (podział przedziłu [ta, tb] na n części
            * zwraca (vt, vx)
            * vt - wektor z kolejnymi t (kolejne ktoki metody)
            * vx - wektor z rozwiązaniami równania dla kolejnych kroków
            
    3) wielokrokowe.py
        - am_s1, am_s2, am_s3, am_s4, am_s5 - parametry dla metody Adamsa-Multona
        - ab_s1, ab_s2, ab_s3, ab_s4, ab_s5 - parametry dla metody Adamsa-Bashfortha
        - adams_bashforth(f, ta, tb, xa, n, sn=ab_s5)
            * służy do obliczania numerycznego metodą Adamsa-Bashfortha równań postaci x' = f(t, x)
            * f - funckcja dwuargumentowa f(t, x)
            * ta - początek predziału
            * tb - koniec przedziału
            * xa - wartość funkcji w ta
            * n - liczba kroków metody (podział przedziłu [ta, tb] na n części
            * sn - parametry dla metody w zależności od tego, które parametry zostaną wczytane do 
                   funkcji takiego rzędu będzie metoda (domyślnie ab_s5 - netoda 5 rzędu)
            * zwraca wartość funkcji w chwili tb
        - pc(f, t, x0, ab=ab_s5, am=am_s5)
            * służy do obliczania numerycznego metodą Adamsa-Bashfortha równań postaci x' = f(t, x)
            * f - funckcja dwuargumentowa f(t, x)
            * t - lista zawierająca kolejne kroki metody
            * x0 - wartość funkcji w ta
            * ab - parametry dla metody w zależności od tego, które parametry zostaną wczytane do funkcji
            * am - parametry dla metody w zależności od tego, które parametry zostaną wczytane do funkcji
            * rząd metody = min(len(ab, len(am))
            * zwraca wektor z rozwiązaniami równania dla kolejnych kroków
            
    4) functions.py
        - plik zawierający funkcje używane przy testach poszczególnych metod
        - test_speed(func, param, repeat=100)
            * sprawdza łączny czas powtórzenia wykonania funkcji func z parametrami param
        - test_met(met, x_true, tb, x0, param):
            * zwraca podstawowe informacje o konkretnej metodzie
            * zwraca słownik {"value": value, "error": error, "time": time}
            * value - wartość funkcji w czasie tb
            * error - błąd metody w czasie tb
            * time - czas wykonania 100 uruchomień metody
        - list_minus(l1, l2):
            * odejmuje od siebie odpowiadające sobie elemety z dwóch list
        - metods_x(f, f_true, ta, tb, xa, n):
            * zwraca wartości metod na całym przedziale [ta, tb] dla funkcji f
            * używa metod euler, euler upgrade, rk4, adams bashforth, pc
        - plotting_val(f, f_true, ta, tb, xa, n)
            * rysuje wszystkie wartości metod dla przedziału [ta, tb] dla funkcji f
            * używa metod euler, euler upgrade, rk4, adams bashforth, pc
        - plotting_error(f, f_true, ta, tb, xa, n)
            * rysuje wszystkie błędy metod dla przedziału [ta, tb] dla funkcji f
            * używa metod euler, euler upgrade, rk4, adams bashforth, pc
            
    5) projekt.py
        - plik zawiera funkcje, które porównują za sobą poszczególne metody
        - t_1()
            * porównuje wynik obliczeń, błąd i czas wykonania metod dla tego samego n
            * używa metod euler, euler upgrade, rk4, adams bashforth, pc
            * w tabeli podaje poszczególne wartości a na dwóch wykresach wyświetla kolejno
              przebieg poszczególnych metod i ich błąd
        - t_2()
            * porównuje wynik obliczeń, błąd i czas wykonania metod dla tego samego błędu
            * pokazuje jak zmniejsza się n dla kolejnych rzędów metod
            * używa metod euler, euler upgrade, rk4, adams bashforth, pc 3
            * w tabeli podaje poszczególne wartości a na dwóch wykresach wyświetla kolejno
              przebieg poszczególnych metod i ich błąd
        - t_3()
            * porównuje wynik obliczeń, błąd i czas wykonania metody pc dla kolejnych kroków
            * pc 1, pc 2, pc 3, pc 4, pc 5
            * w tabeli podaje poszczególne wartości a na dwóch wykresach wyświetla kolejno
              przebieg poszczególnych metod i ich błąd

         
    Tabele z wynikami trzech kolejnych testów:
    
    Test 1:
    +---------------------------+----------------+-------------------+-------------------------+
    | Nazwa metody              | Wynik obliczen | Blad              | Czas wykonania operacji |
    +---------------------------+----------------+-------------------+-------------------------+
    | Rozwiazanie dokladne      | 16.487212707   |                   |                         |
    | Metoda Eulera             | 15.4711039801  | 1.0161087269      | 0.000656127929688       |
    | Ulepszona metoda Eulera   | 16.4788134551  | 0.00839925186921  | 0.00121593475342        |
    | Metoda Rungego-Kutty      | 16.4872100705  | 2.63646731469e-06 | 0.00276803970337        |
    | Metoda Adamsa-Bashfortha  | 26.6264104904  | 10.1391977834     | 0.00232815742493        |
    | Metoda predyktor-korektor | 16.4575814187  | 0.0296312882764   | 0.0378818511963         |
    +---------------------------+----------------+-------------------+-------------------------+
    
    Test 2:
    +-----------------------------+----------------+------------------+-------------------------+--------+
    | Nazwa metody                | Wynik obliczen | Blad             | Czas wykonania operacji | n      |
    +-----------------------------+----------------+------------------+-------------------------+--------+
    | Rozwiazanie dokladne        | 73.8905609893  |                  |                         |        |
    | Metoda Eulera               | 73.88056101    | 0.00999997927482 | 2.25990700722           | 34478  |
    | Ulepszona metoda Eulera     | 73.8806263734  | 0.00993461592208 | 0.0199890136719         | 140    |
    | Metoda predyktor-korektor 3 | 73.8807158851  | 0.00984510417256 | 0.0763869285583         | 35     |
    | Metoda Rungego-Kutty        | 73.882248432   | 0.00831255729942 | 0.00369000434875        | 10     |
    | Metoda Adamsa-Bashfortha    | 73.9005609789  | 0.00999998961856 | 27.2815389633           | 118235 |
    +-----------------------------+----------------+------------------+-------------------------+--------+
    
    Test 3:
    +---------------------------+------------------+-------------------+-------------------------+---------------+
    | Nazwa metody              | Wynik obliczen   | Blad              | Czas wykonania operacji | liczba krokow |
    +---------------------------+------------------+-------------------+-------------------------+---------------+
    | Rozwiazanie dokladne      | 0.00453999297625 |                   |                         |               |
    | Metoda predyktor-korektor | 0.317121193893   | 0.312581200917    | 0.0504908561707         | 1             |
    | Metoda predyktor-korektor | 0.00210601788541 | 0.00243397509084  | 0.0520648956299         | 2             |
    | Metoda predyktor-korektor | 0.00555478226041 | 0.00101478928416  | 0.0577931404114         | 3             |
    | Metoda predyktor-korektor | 0.00402457042065 | 0.000515422555596 | 0.062518119812          | 4             |
    | Metoda predyktor-korektor | 0.00505745019866 | 0.000517457222411 | 0.0677058696747         | 5             |
    +---------------------------+------------------+-------------------+-------------------------+---------------+