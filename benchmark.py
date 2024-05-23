import time
import random
import math 
import matplotlib.pyplot as plt
import algorithms


'''
Ogni test su una lunghezza n data deve generare in modo pseudo-casuale 
un array di n interi, in un intervallo a scelta (es. interi compresi fra 0 e 1000000) 
e un parametro k∈{1,...,n}. Si noti che la complessità di alcuni algoritmi può dipendere 
in modo significativo dalla scelta del range di interi e dal parametro k
ed è quindi possibile immaginare test diversificati in funzione di queste variabili 
allo scopo di evidenziare tali dipendenze.
'''

def init_array(n, max_val):
    random.seed()
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(0, max_val)
    return arr


def init_indexes(n, tot_indexes):
    indexes = [0] * tot_indexes
    for i in range(tot_indexes):
        indexes[i] = random.randint(1, n-1)
    return indexes


'''
Il primo passo consiste nello stimare la risoluzione del clock di sistema,
utilizzando un ciclo while per calcolare l'intervallo minimo di tempo misurabile. 
'''

def resolution():
    start = time.perf_counter()
    while time.perf_counter() == start:
        pass
    stop = time.perf_counter()
    return stop - start


# result of resoluion() function can vary in time,
# so we calculate a mean value
def calculate_mean_resolution():
    attempts = 1000
    tot_sum = 0    
    for i in range(attempts):
        tot_sum += resolution()
    return tot_sum / attempts


#r = calculate_mean_resolution()

'''
In funzione della risoluzione stimata r e 
dell'errore relativo massimo ammissibile (err = 0.001), 
si calcola il tempo minimo misurabile

Tmin = r*(1/err + 1)
'''

#err_min = 0.001

#min_time = r * ((1/err_min) + 1)


'''
Per stimare il tempo medio di esecuzione di un algoritmo 
su istanze dell'input di dimensione n si utilizza un ciclo while, 
iterando l'esecuzione dell'algoritmo su un input di dimensione n, 
generato in modo pseudo-casuale, e misurando complessivamente 
un intervallo di tempo superiore a Tmin. 
La misurazione deve essere effettuata senza interrompere il clock, 
ovvero calcolando l'intero intervallo di tempo trascorso dall'inizio 
dell'iterazione fino al momento il cui il tempo misurato risulti superiore a Tmin.
Il tempo medio di esecuzione per una singola istanza di input sarà quindi ottenuto calcolando 
il rapporto fra il tempo totale misurato e il numero di iterazioni dell'algoritmo eseguite 
(questa divisione non influisce sull'errore relativo commesso).
'''

def measure(n, max_val, function, mean_resolution, tot_indexes):
    min_err = 0.001
    min_time = mean_resolution * ((1/min_err) + 1)
    # n is the desired size of the array
    # min_time is the minumum measurable time to guarantee bounded relative error
    count = 0
    # start_time = time.perf_counter()      <-----------  TODO (initially timer started here)
    arr = init_array(n, max_val)
    k_values = init_indexes(n, tot_indexes)

    while True:
        # what if I started the timer here?  <----------  TODO
        start_time = time.perf_counter()
        
        for k in k_values:
            a_copy = arr.copy()
            # this way all function must have same signature (required args)
            function(a_copy, 0, len(a_copy), k)

        count = count + 1
        end_time = time.perf_counter()
        if end_time - start_time >= min_time:
             break

    return (end_time - start_time) / count


def main():
    resolution = calculate_mean_resolution()
    n_min = 100
    n_max = 100000
    times = 100
    tot_k_indices = 10
    # if we want n = 100 for i = 0 then A = 100
    A = n_min
    # if A = 100, then 100*(B**i) = 100000 for i = 99,
    # solving for B, we extract the 99th root of 1000 
    # for finding B's value
    B = (n_max / n_min) ** (1/99)
    points = [(None, None, None, None, None)] * times

    for i in range(times):
        print(f"\r{i} -> ", end='')
        n = int(A * (B ** i))
        print(f"valore di n: {n}")
        
        points[i] = (n, 
            measure(n, 100, algorithms.quick_select, resolution, tot_k_indices),
            measure(n, 100, algorithms.heap_select, resolution, tot_k_indices),
            measure(n, 100, algorithms.median_of_medians, resolution, tot_k_indices),
        )

    xs, ys1, ys2, ys3, ys4 = zip(*points)
    plt.xscale('log')
    plt.yscale('log')
    plt.scatter(xs, ys1, c='green') # quick_select
    plt.scatter(xs, ys2, c='blue') # heap_select
    plt.scatter(xs, ys3, c='red') # median_of_medians
    plt.scatter(xs, ys4, c='orange')
    plt.show()

main()