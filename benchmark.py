import time
import random
import matplotlib.pyplot as plt
import quick_select.quick_select_rec_rand as quick
import heap_select.heap_select_min_max as heap
import median_of_medians_select.med_of_meds_03 as median


def init_array(n, max_rand_val):
    random.seed()
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(0, max_rand_val)
    return arr


def init_indexes(n, tot_indexes):
    indexes = [0] * tot_indexes
    for i in range(tot_indexes):
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


def measure(n, max_rand_val, function, mean_resolution, tot_indexes):
    min_err = 0.001
    min_time = mean_resolution * ((1/min_err) + 1)
    # n is the desired size of the array
    # min_time is the minumum measurable time to guarantee bounded relative error
    count = 0
    start_time = time.perf_counter()      #  <-----------  TODO (initially timer started here -see below-)
    arr = init_array(n, max_rand_val)
    k_values = init_indexes(n, tot_indexes)

    while True:
        # what if I started the timer here?  <----------  TODO ()
        # start_time = time.perf_counter()
        
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
    tot_k_indices = 5
    A = n_min
    B = (n_max / n_min) ** (1/99)
    points = [(None, None, None)] * times

    for i in range(times):
        print(f"\r{i} -> ", end='')
        n = int(A * (B ** i))
        print(f"valore di n: {n}")
        
        points[i] = (n, 
            measure(n, 1000000, quick.quick_select_rec_rand, resolution, tot_k_indices),
            measure(n, 1000000, heap.heap_select, resolution, tot_k_indices),
            measure(n, 1000000, median.median_of_medians_select, resolution, tot_k_indices),
            #measure(n, 1000000, rec_rand.quick_select_rec_rand, resolution, tot_k_indices)
        )

    xs, ys1, ys2, ys3 = zip(*points)
    plt.xscale('log')
    plt.yscale('log')
    plt.scatter(xs, ys1, c='blue', label='Quick Select')  
    plt.scatter(xs, ys2, c='green', label='Heap Select')
    plt.scatter(xs, ys3, c='orange', label='Median of Medians Select')   
    #plt.scatter(xs, ys4, c='orange', label="Recursive Random Pivot")    # recursion random
    plt.legend(title="Median of Medians Select")
    plt.show()

main()