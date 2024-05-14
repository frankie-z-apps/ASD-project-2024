import time
import random

'''
Ogni test su una lunghezza n data deve generare in modo pseudo-casuale 
un array di n interi, in un intervallo a scelta (es. interi compresi fra 0 e 1000000) 
e un parametro k∈{1,...,n}. Si noti che la complessità di alcuni algoritmi può dipendere 
in modo significativo dalla scelta del range di interi e dal parametro k
ed è quindi possibile immaginare test diversificati in funzione di queste variabili 
allo scopo di evidenziare tali dipendenze.
'''

def init_array(n):
    random.seed()
    array = []
    for i in range(n):
        array.append(random.randint(-1000, 1000))
    return array


def init_index(n):
    random.seed()
    return random.randint(1, n-1)


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


r = calculate_mean_resolution()

'''
In funzione della risoluzione stimata r e 
dell'errore relativo massimo ammissibile (err = 0.001), 
si calcola il tempo minimo misurabile

Tmin = r*(1/err + 1)
'''

err_min = 0.001

min_time = r * (1/err_min + 1)


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

def measure(n, min_time, algorithm):
    # n is the desired size of the array
    # min_time is the minumum measurable time to guarantee bounded relative error
    count = 0
    start_time = time.perf_counter()
    
    while True:
        arr = init_array(n)
        k = init_index(n)
        algorithm(arr, k)
        count = count + 1
        end_time = time.perf_counter()

        if end_time - start_time >= min_time:
             break
        
    return (end_time - start_time) / count


arr = init_array(100)
print(arr)
print(init_index(100))