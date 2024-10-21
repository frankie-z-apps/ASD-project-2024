import time
import random
import matplotlib.pyplot as plt
import platform

import quick_select as quick
import heap_select as heap
import median_of_medians_select as median


'''
    Call a different function to get current time
    depending on user's OS, resolving OS-related issues between methods
'''
def get_time():
    os_name = platform.system()

    if os_name == 'Windows':
        return time.perf_counter()
    else:
        return time.monotonic()
    

'''
    Initialize array with random values
    in interval [0, max_rand_val]
'''
def init_array(n, max_rand_val):                                                       
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(0, max_rand_val)
    return arr


'''
    Extract k random indexes
    in interval [0, n-1]
'''
def init_indexes(n, k):                                                 
    indexes = [0] * k                                                   
    for i in range(k):
        indexes[i] = random.randint(1, n-1)
    return indexes


'''
    Calculate smallest time interval
    recorded by system
'''
def resolution():                                                      
    start = get_time()
    while get_time() == start:
        pass
    stop = get_time()
    return stop - start


'''
    Calculate mean resolution
    over n total iterations
'''
def calculate_mean_resolution(iterations):                              
    tot_q_sum = 0    
    for i in range(iterations):
        tot_q_sum += resolution()
    return tot_q_sum / iterations


'''
    Measure the mean time required for the execution
    of a function with multiple k-values on the same array
'''
def measure(arr, function, mean_resolution, k_values):
    min_err = 0.001                                                     
    min_time = mean_resolution * ((1/min_err) + 1)                      
    count = 0                                                           
    start_time = get_time()

    while True:        
        for k in k_values:
            a_copy = arr.copy()
            function(a_copy, 0, len(a_copy), k)

        count = count + 1
        end_time = get_time()
        if end_time - start_time >= min_time:
             break

    return (end_time - start_time) / count


'''
    Run a single function over all samples
    Record times for each iteration and total duration
'''
def test_function(function, samples):
    mean_resolution = calculate_mean_resolution(1000)
    timings = [0] * len(samples)
    
    test_start_time = get_time()

    for i in range(len(samples)):
        sample = samples[i]
        arr = sample[0]
        k_values = sample[1]
        n = len(arr)
        print(f"Array size: {n:6}\tProgress: {((i+1)/len(samples)*100):3.2f}%", end='\r')
        timings[i] = (n, measure(arr, function, mean_resolution, k_values))

    test_duration = get_time() - test_start_time
    
    return timings, test_duration


'''
    Generate sample arrays over which each algorithm will be tested
'''
def generate_samples(n_start, n_end, iterations, max_rand_val, k_tests):
    random.seed()
    samples = []
    A = n_start
    B = (n_end / n_start) ** (1/(iterations-1))

    for i in range(iterations):
        n = int(A * (B ** i))
        a = init_array(n, max_rand_val)
        k_values = init_indexes(n, k_tests)
        samples.append([a, k_values])
    
    return samples


'''
    Put the record times of a function test on a plot
    Draw a line indicating the mean value above all points
'''
def plot_results(timings, color, function_name):
    xs, ys = zip(*timings)
    sum = 0

    for i in range(len(timings)):
        sum += ys[i] / xs[i]
    
    q = sum / len(timings)
    mean_slope = [(q * x) for x in xs]

    plt.scatter(xs, ys, c=color, label=function_name)
    plt.plot(xs, mean_slope, '--', c=color)


'''
    Return seconds in a human readable format
'''
def make_readable(seconds):
    seconds = int(seconds * 1000) / 1000
    hh = int(seconds / 3600)
    seconds = seconds % 3600
    mm = int(seconds / 60)
    ss = int(seconds % 60)
    milli = int((seconds - ss)*1000) % 1000

    return f"{hh:02}h {mm:02}min {ss:02}sec {milli:03}msec"


'''
    Test every algorithm on the same array with same k values
    Measure time required for completion with array of increasing lenght
    Plot the results and return graph
'''
def run_benchmark():
    n_start = 100
    n_end = 100000
    iterations = 100
    max_rand_val = 1000000
    k_tests = 25
    samples = generate_samples(n_start, n_end, iterations, max_rand_val, k_tests)
    
    print("\nTesting Quick Select algorithm:")
    quick_timings, quick_duration = test_function(quick.quick_select, samples)
    plot_results(quick_timings, 'lightblue', 'Quick Select')
    print("\nDone\n")

    print("Testing Median of Medians Select algorithm")
    median_timings, median_duration = test_function(median.median_of_medians_select, samples)
    plot_results(median_timings, 'orange', 'Median of Medians Select')
    print("\nDone\n")

    print("Testing Heap Select algorithm")
    heap_timings, heap_duration = test_function(heap.heap_select, samples)
    plot_results(heap_timings, 'lightgreen', 'Heap Select')
    print("\nDone\n")

    plt.legend(fontsize=16)
    plt.xscale('log')
    plt.yscale('log')

    algorithm_total_time = quick_duration + median_duration + heap_duration

    quick_percentage = quick_duration / algorithm_total_time
    median_percentage = median_duration / algorithm_total_time
    heap_percentage = heap_duration / algorithm_total_time

    print(f'{"Quick Select:":30} {make_readable(quick_duration)} -> {(quick_percentage * 100):.2f}%\n{"Median of Medians Select:":30} {make_readable(median_duration)} -> {(median_percentage * 100):.2f}%\n{"Heap Select:":30} {make_readable(heap_duration)} -> {(heap_percentage * 100):.2f}%\n{"Total time:":30} {make_readable(algorithm_total_time)}')
    print(f'\n{f"Iterations: {iterations}":8}\n{f"Initial array length: {n_start}":8}\n{f"Final array length: {n_end}":8}\n{f"K tests: {k_tests}":8}')
    
    plt.show()


if __name__ == '__main__':
    run_benchmark()