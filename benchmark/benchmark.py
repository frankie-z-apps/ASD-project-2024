import time
import random
import matplotlib.pyplot as plt


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
    start = time.monotonic()
    while time.monotonic() == start:
        pass
    stop = time.monotonic()
    return stop - start


# result of resoluion() function can vary in time,
# so we calculate a mean value
def calculate_mean_resolution():
    attempts = 1000
    tot_sum = 0    
    for i in range(attempts):
        tot_sum += resolution()
    return tot_sum / attempts


def measure(arr, function, mean_resolution, k_list):
    min_err = 0.001
    min_time = mean_resolution * ((1/min_err) + 1)
    # n is the desired size of the array
    # min_time is the minumum measurable time to guarantee bounded relative error
    count = 0
    start_time = time.monotonic()      #  <-----------  TODO (initially timer started here -see below-)

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
    resolution = calculate_mean_resolution()
    max_rand_val = 1000000
    n_begin = 100
    n_end = 10000
    times = 100
    k_tests = 5
    A = n_begin
    B = (n_end / n_begin) ** (1/99)
    points = [(None, None, None)] * times

    # we want each algorithm to be tested on the same array with the same k-values

    for i in range(times):
        print(f"\r{i} -> ", end='')
        n = int(A * (B ** i))
        print(f"valore di n: {n}")

        arr = init_array(n, max_rand_val)
        k_values = init_indexes(n, k_tests)

        
        points[i] = (n, 
            measure(arr, function, resolution, k_values),
            measure(arr, function, resolution, k_values),
            measure(arr, function, resolution, k_values),
            #measure(n, 1000000, rec_rand.quick_select_rec_rand, resolution, k_tests)
        )

    xs, ys1, ys2, ys3 = zip(*points)
    plt.xscale('log')
    plt.yscale('log')
    plt.scatter(xs, ys1, c='blue', label='First Version')  
    plt.scatter(xs, ys2, c='green', label='Second Version')
    plt.scatter(xs, ys3, c='orange', label='Third Version')   
    #plt.scatter(xs, ys4, c='orange', label="Recursive Random Pivot")    # recursion random
    plt.legend(title="Median of Medians Select")
    plt.show()

main()