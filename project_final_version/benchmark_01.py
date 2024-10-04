import time
import random
import matplotlib.pyplot as plt

import quick_select as quick
import heap_select as heap
import median_of_medians_select as median


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
    start = time.monotonic()                                           
    while time.monotonic() == start:
        pass
    stop = time.monotonic()
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
    start_time = time.monotonic()

    while True:        
        for k in k_values:
            a_copy = arr.copy()
            function(a_copy, 0, len(a_copy), k)

        count = count + 1
        end_time = time.monotonic()
        if end_time - start_time >= min_time:
             break

    return (end_time - start_time) / count


def test_function(function, samples):
    mean_resolution = calculate_mean_resolution(1000)
    timings = [0] * len(samples)
    i = 0

    test_start_time = time.monotonic()

    for sample in samples:
        arr = sample[0]
        k_values = sample[1]
        n = len(arr)
        print(f"Array size: {n} \tProgress: {i}%", end='\r')
        timings[i] = (n, measure(arr, function, mean_resolution, k_values))
        i = i + 1

    test_end_time = time.monotonic()
    test_duration = test_end_time - test_start_time
    

    return timings, test_duration


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


def plot_results(timings, color, function_name):
    xs, ys = zip(*timings)

    plt.scatter(xs, ys, c=color, label=function_name)


'''
    Test every algorithm on the same array with same k values
    Measure time required for completion with array of increasing lenght
    Plot the results and return graph
'''
def main():          
    main_duration_start = time.monotonic()
    samples = generate_samples(100, 10000, 100, 1000000, 5)

    print("Testing Quick Select algorithm:")
    quick_timings, quick_duration = test_function(quick.quick_select, samples)
    plot_results(quick_timings, 'lightblue', 'Quick Select')
    print("Done\n\n")

    print("Testing Heap Select algorithm")
    heap_timings, heap_duration = test_function(heap.heap_select, samples)
    plot_results(heap_timings, 'orange', 'Heap Select')
    print("Done\n\n")

    print("Testing Median of Medians Select algorithm")
    median_timings, median_duration = test_function(median.median_of_medians_select, samples)
    plot_results(median_timings, 'lightgreen', 'Median of Medians Select')
    print("Done\n\n")
     
    main_duration_end = time.monotonic()

    plt.xscale('log')
    plt.yscale('log')
    plt.legend(title="Algorithms comparison")

    print(f"QuickSort total duration: {quick_duration}\nHeapSort total duration: {heap_duration}\nMedian of Medians total duration: {median_duration}\nTotal duration: {main_duration_end-main_duration_start}")

    

    '''
        Draw mean execution time reference line for each algorithm
    '''

    q_sum = 0
    h_sum = 0
    m_sum = 0

    '''
    for i in range(iterations):
        q_sum += ys1[i] / xs[i]
        h_sum += ys2[i] / xs[i]
        m_sum += ys3[i] / xs[i]

    q_quick_select = q_sum / iterations
    q_heap_select = h_sum / iterations
    q_median_select = m_sum / iterations


    mean_quick_select = [(q_quick_select * x) for x in xs]
    mean_heap_select = [(q_heap_select * x) for x in xs]
    mean_median_select = [(q_median_select * x) for x in xs]

    plt.plot(xs, mean_quick_select, '--', color='blue', label='Tempo medio Quick Sort')
    plt.plot(xs, mean_heap_select, '--', color='green', label='Tempo medio Heap Sort')
    plt.plot(xs, mean_median_select, '--', color='red', label='Tempo medio Median of Median select')'''

    plt.show()

main()