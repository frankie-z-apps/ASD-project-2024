import time
import random
import matplotlib.pyplot as plt
import quick_select.quick_select_rec_rand as quick
import heap_select.heap_select_min_max as heap
import median_of_medians_select.med_of_meds_03 as median


# generate a 2D array with k copies of the same array of length n
def init_array_copies(n, max_rand_val, tot_k_values):
    random.seed()
    
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(0, max_rand_val)

    #arr = [[None for _ in range(tot_k_values)] for i in range(n)]
    arr_copies = [arr.copy() for i in range(tot_k_values)]
    return arr_copies


def init_indexes(n, tot_k_values):
    indexes = [0] * tot_k_values
    for i in range(tot_k_values):
        indexes[i] = random.randint(1, n-1)
    return indexes


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


def measure(n, max_rand_val, function, mean_resolution, tot_k_values):
    min_err = 0.001
    min_time = mean_resolution * ((1/min_err) + 1)
    # n is the desired size of the array
    # min_time is the minumum measurable time to guarantee bounded relative error
    count = 0
    #start_time = time.perf_counter()      #  <-----------  TODO (initially timer started here -see below-)
    arr_copies = init_array_copies(n, max_rand_val, tot_k_values) # initialize all k copies of the same array
    #print(f"Array copies: {arr_copies}")
    k_values = init_indexes(n, tot_k_values)
    #print(f"K-values: {k_values}")
    start_time = time.perf_counter()
    
    while True:
        # what if I started the timer here?  <----------  TODO ()
        # start_time = time.perf_counter()
        
        for k in range(tot_k_values):
            #print(f"Array number {k}: {arr_copies[k]}\nK_values: {k_values}\nCurrent k-value: {k_values[k]}\nValue of n: {n}")
            # this way all function must have same signature (required args)
            #print(f"Arr_copies[k]: {arr_copies[k]}\nlen(arr_copies[k]): {len(arr_copies[k])}")
            function(arr_copies[k], 0, len(arr_copies[k]), k_values[k])

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
    tot_k_indices = 3
    max_random_value = 1000000

    A = n_min
    B = (n_max / n_min) ** (1/99)
    points = [(None, None, None)] * times

    main_duration_start = time.perf_counter()

    for i in range(times):
        print(f"\r{i} -> ", end='')
        n = int(A * (B ** i))
        print(f"n value: {n}")
        
        points[i] = (n, 
            measure(n, max_random_value, quick.quick_select_rec_rand, resolution, tot_k_indices),
            measure(n, max_random_value, heap.heap_select, resolution, tot_k_indices),
            measure(n, max_random_value, median.median_of_medians_select, resolution, tot_k_indices),
        )

    main_duration_end = time.perf_counter()

    xs, ys1, ys2, ys3 = zip(*points)
    plt.xscale('log')
    plt.yscale('log')
    plt.scatter(xs, ys1, c='blue', label='Quick Select')  
    plt.scatter(xs, ys2, c='green', label='Heap Select')
    plt.scatter(xs, ys3, c='orange', label='Median of Medians Select')
    plt.legend(title="Algorithms comparison")
    
    plt.annotate(f'Number of k-tries for array: {tot_k_indices}\nMax random value for array element: {max_random_value}\nTotal execution time (seconds): {main_duration_end - main_duration_start}',xy=(0.0, -0.12), xycoords='axes fraction', ha='left', fontsize=7)
    plt.show()

main()