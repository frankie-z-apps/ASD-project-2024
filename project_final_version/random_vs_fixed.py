import time
import random
import matplotlib.pyplot as plt
import platform

import quick_select as quick


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
    i = 0

    test_start_time = get_time()

    for sample in samples:
        arr = sample[0]
        k_values = sample[1]
        n = len(arr)
        print(f"Array size: {n} \tProgress: {i+1}%", end='\r')
        timings[i] = (n, measure(arr, function, mean_resolution, k_values))
        i = i + 1

    test_duration = get_time() - test_start_time
    
    return timings, test_duration


'''
    Generate sample arrays over which each algorithm will be tested
'''
def generate_samples(n_start, n_end, iterations, max_rand_val, k_tests):
    random.seed()
    samples = []
    A = n_start
    B = (n_end / n_start) ** (1/99)

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
    plt.plot(xs, mean_slope, '--', c=color, label=f'Mean execution time of {function_name}')


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
    k_tests = 10
    samples = generate_samples(n_start, n_end, iterations, max_rand_val, k_tests)

    benchmark_start = get_time()

    print("\nTesting Quick Select - fixed pivot:")
    fixed_timings, fixed_duration = test_function(quick.quick_select_fixed, samples)
    plot_results(fixed_timings, 'lightblue', 'Quick Select - fixed pivot')
    print("\nDone\n\n")

    print("Testing Quick Select - randomized pivot:")
    randomized_timings, randomized_duration = test_function(quick.quick_select, samples)
    plot_results(randomized_timings, 'orange', 'Quick Select - random pivot')
    print("\nDone\n\n")
    
    benchmark_duration = get_time() - benchmark_start

    algorithm_sum = fixed_duration + randomized_duration

    fixed_percentage = fixed_duration / algorithm_sum
    randomized_percentage = randomized_duration / algorithm_sum

    plt.xscale('log')
    plt.yscale('log')
    plt.legend(title="Fixed vs Random pivot comparison")

    plt.annotate(f'Fixed pivot duration: {fixed_duration:.6f}s  {(fixed_percentage * 100):.2f}%\nRandom pivot duration: {randomized_duration:.6f}s  {(randomized_percentage * 100):.2f}%\nTotal time: {benchmark_duration:.6f}s', \
                xy=(0.0, -0.128), \
                xycoords='axes fraction', \
                ha='left', \
                fontsize=7)
    
    plt.annotate(f'Iterations: {iterations}\nInitial array length: {n_start}\nFinal array length: {n_end}\nK tests: {k_tests}', \
                xy=(1, -0.128), \
                xycoords='axes fraction', \
                ha='right', \
                fontsize=7 )
    
    plt.show()


if __name__ == '__main__':
    run_benchmark()