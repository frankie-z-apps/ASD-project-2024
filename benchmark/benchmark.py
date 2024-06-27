import time
import random
import matplotlib.pyplot as plt

import quick_select.quick_select_rec_rand as quick
import heap_select.heap_select_min_max as heap
import median_of_medians_select.med_of_meds_03 as medians


def init_array(n, max_rand_val):                                        # initialize the array with random values
    random.seed()                                                       # in the interval [0, max_rand_val]
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(0, max_rand_val)
    return arr


def init_indexes(n, k):                                                 # extract k random indexes in the interval [0, n-1] 
    indexes = [0] * k                                                   # from an array of length n
    for i in range(k):
        indexes[i] = random.randint(1, n-1)
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


def measure(arr, function, mean_resolution, k_list):                    # measure the mean time required for the execution 
    min_err = 0.001                                                     # of an algorithm over an array, over a list of many
    min_time = mean_resolution * ((1/min_err) + 1)                      # values of k. min_time is the minimum measurable time
    count = 0                                                           # to guarantee bounded relative error
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
    n_begin = 100
    n_end = 10000
    times = 100
    k_tests = 100
    A = n_begin
    B = (n_end / n_begin) ** (1/99)
    points = [(None, None, None)] * times

    main_duration_start = time.monotonic()

    for i in range(times):
        print(f"\r{i} -> ", end='')
        n = int(A * (B ** i))
        print(f"Value of n: {n}")

        arr = init_array(n, max_rand_val)
        k_values = init_indexes(n, k_tests)

        points[i] = (n, 
            measure(arr, quick.quick_select_rec_rand, resolution, k_values),
            measure(arr, heap.heap_select, resolution, k_values),
            measure(arr, medians.median_of_medians_select, resolution, k_values),
        )

    main_duration_end = time.monotonic()

    xs, ys1, ys2, ys3 = zip(*points)
    plt.xscale('log')
    plt.yscale('log')
    plt.scatter(xs, ys1, c='blue', label='Quick Select')  
    plt.scatter(xs, ys2, c='green', label='Heap Select')
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

    plt.show()

main()