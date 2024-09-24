import time
import random
import matplotlib.pyplot as plt

import quick_select as quick
import heap_select as heap
import median_of_medians_select as median

'''
    initialize array with random values
    in interval [0, max_rand_val]
'''
def init_array(n, max_rand_val):                                        
    random.seed()                                                       
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(0, max_rand_val)
    return arr


'''
    extract k random indexes
    in interval [0, n-1]
'''
def init_indexes(n, k):                                                 
    indexes = [0] * k                                                   
    for i in range(k):
        indexes[i] = random.randint(1, n-1)
    return indexes


'''
    calculate smallest time interval
    recorded by system
'''
def resolution():                                                      
    start = time.monotonic()                                           
    while time.monotonic() == start:
        pass
    stop = time.monotonic()
    return stop - start


'''
    calculate mean resolution
    over n total times
'''
def calculate_mean_resolution(times):                              
    tot_sum = 0    
    for i in range(times):
        tot_sum += resolution()
    return tot_sum / times



'''
    measure the mean time required for the execution
    of a function with multiple k-values on the same array
'''
def measure(arr, function, mean_resolution, k_list):                    
    min_err = 0.001                                                     
    min_time = mean_resolution * ((1/min_err) + 1)                      
    count = 0                                                           
    start_time = time.monotonic()

    while True:        
        for k in k_list:
            a_copy = arr.copy()
            function(a_copy, 0, len(a_copy), k)

        count = count + 1
        end_time = time.monotonic()
        if end_time - start_time >= min_time:
             break

    return (end_time - start_time) / count



def main():
    resolution = calculate_mean_resolution(1000)
    max_rand_val = 1000000
    n_begin = 10
    n_end = 100000
    times = 100
    k_tests = 10
    A = n_begin
    B = (n_end / n_begin) ** (1/99)
    points = [(None, None, None)] * times

    main_duration_start = time.monotonic()

    for i in range(times):
        n = int(A * (B ** i))
        print(f"Progress: {i}%\t Array size: {n}", end='\r')

        arr = init_array(n, max_rand_val)
        k_values = init_indexes(n, k_tests)

        points[i] = (n, 
            measure(arr, quick.quick_select, resolution, k_values),
            measure(arr, heap.heap_select, resolution, k_values),
            measure(arr, median.median_of_medians_select, resolution, k_values),
        )

    main_duration_end = time.monotonic()

    xs, ys1, ys2, ys3 = zip(*points)
    plt.xscale('log')
    plt.yscale('log')
    plt.scatter(xs, ys1, c='lightblue', label='Quick Select')  
    plt.scatter(xs, ys2, c='lightgreen', label='Heap Select')
    plt.scatter(xs, ys3, c='orange', label='Median of Medians Select')   
    plt.legend(title="Algorithms comparison")

    plt.annotate(f'Number of k-tests for array: {k_tests}\n\
            Max random value for array element: {max_rand_val}\n\
            Total execution time (seconds): {main_duration_end - main_duration_start}', \
                xy=(0.0, -0.12), \
                xycoords='axes fraction', \
                ha='left', \
                fontsize=7)
    
    plt.annotate(f'Minimum array length: {n_begin}\n\
                Maximum array length: {n_end}', \
                xy=(1.0, -0.12), \
                xycoords='axes fraction', \
                ha='right', \
                fontsize=7 )
    

    # Disegna le rette di riferimento

    # Riferimento lineare per QuickSelect
    k_qs = ys1[0] / xs[0]  # Calcola il coefficiente di proporzionalità
    tempoLineare_qs = [(k_qs * x) for x in xs]  # Rette lineare
    plt.plot(xs, tempoLineare_qs, '--', color='blue', label='Andamento Lineare QS')

    # Riferimento lineare per HeapSelect
    k_hs = ys2[0] / xs[0]  # Calcola il coefficiente di proporzionalità
    tempoLineare_hs = [(k_hs * x) for x in xs]  # Rette lineare
    plt.plot(xs, tempoLineare_hs, '--', color='green', label='Andamento Lineare HS')

    
    # Riferimento lineare per MedianOfMedians
    k_mom = ys3[0] / xs[0]  # Calcola il coefficiente di proporzionalità
    tempoLineare_mom = [(k_mom * x) for x in xs]  # Rette lineare
    plt.plot(xs, tempoLineare_mom, '--', color='red', label='Andamento Lineare MoM')

    plt.show()

main()