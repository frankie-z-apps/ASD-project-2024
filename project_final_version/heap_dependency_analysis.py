import time
import random
import matplotlib.pyplot as plt

import heap_select as heap

# DEPENDENCY ANALYSIS: how k parameter affects performance of heap-select algorithm


def init_array(n, max_rand_val):                                        # initialize the array with random values
    random.seed()                                                       # in the interval [0, max_rand_val]
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(0, max_rand_val)
    return arr


def init_indexes(n):                                                    # return sorted list of indexes [0, 1, ... n-1]
    indexes = [i for i in range(n)]
    return indexes


def resolution():                                                       # calculate the smallest time interval  
    start = time.monotonic()                                            # recorded from the system
    while time.monotonic() == start:
        pass
    stop = time.monotonic()
    return stop - start


def calculate_mean_resolution(n_attempts):                              # calculate the mean resolution over n total attempts
    tot_sum = 0    
    for i in range(n_attempts):
        tot_sum += resolution()
    return tot_sum / n_attempts


def measure(arr, function, mean_resolution, k):                         # measure the mean time required for the execution 
    min_err = 0.001                                                     # of an algorithm over an array, over a list of many
    min_time = mean_resolution * ((1/min_err) + 1)                      # values of k. min_time is the minimum measurable time
    count = 0                                                           # to guarantee bounded relative error
    start_time = time.monotonic()

    while True:        
        a_copy = arr.copy()
        function(a_copy, 0, len(a_copy), k)

        count = count + 1
        end_time = time.monotonic()
        if end_time - start_time >= min_time:
             break

    return (end_time - start_time) / count



def main():
    array_length = int(input("Input test array size: "))
    resolution = calculate_mean_resolution(1000)
    max_rand_val = 1000000
    #n_begin = 100
    #n_end = 10000
    #k_tests = 100
    #A = n_begin
    #B = (n_end / n_begin) ** (1/99)
    points = [(None, None)] * array_length

    arr = init_array(array_length, 1000000)
    k_values = init_indexes(array_length)

    main_duration_start = time.monotonic()

    for i in range(array_length):
        #print(f"\r{i} -> ", end='')
        #n = int(A * (B ** i))
        print(f"Test number: {i+1} - {int((i / array_length)*100)}%", end='\r')

        points[i] = (i, 
            measure(arr, heap.heap_select, resolution, i),
            measure(arr, heap.min_heap_select, resolution, i)
        )

    main_duration_end = time.monotonic()

    xs, ys1, ys2 = zip(*points)
    plt.xscale('linear')
    plt.yscale('linear')
    plt.scatter(xs, ys1, c='darkblue', label='Min-Max heap')  
    plt.scatter(xs, ys2, c='lightblue', label='Min heap')
    plt.legend(title="K-dependence analysis")

    '''
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
    plt.plot(xs, tempoLineare_qs, '--', color='green', label='Andamento Lineare QS')

    # Riferimento lineare per HeapSelect
    k_hs = ys2[0] / xs[0]  # Calcola il coefficiente di proporzionalità
    tempoLineare_hs = [(k_hs * x) for x in xs]  # Rette lineare
    plt.plot(xs, tempoLineare_hs, '--', color='blue', label='Andamento Lineare HS')

    
    # Riferimento lineare per MedianOfMedians
    k_mom = ys3[0] / xs[0]  # Calcola il coefficiente di proporzionalità
    tempoLineare_mom = [(k_mom * x) for x in xs]  # Rette lineare
    plt.plot(xs, tempoLineare_mom, '--', color='red', label='Andamento Lineare MoM')
    '''


    plt.show()

main()