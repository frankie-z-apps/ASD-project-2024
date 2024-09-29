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
    random.seed()                                                       
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


'''
    Test every algorithm on the same array with same k values
    Measure time required for completion with array of increasing lenght
    Plot the results and return graph
'''
def main():
    resolution = calculate_mean_resolution(1000)
    max_rand_val = 1000000
    n_begin = 100
    n_end = 10000
    iterations = 100
    k_tests = 15
    A = n_begin
    B = (n_end / n_begin) ** (1/99)
    points = [(None, None, None)] * iterations
    times = [(None, None, None)] * iterations

    main_duration_start = time.monotonic()

    for i in range(iterations):
        n = int(A * (B ** i))
        print(f"Progress: {i}%\t Array size: {n}", end='\r')

        arr = init_array(n, max_rand_val)
        k_values = init_indexes(n, k_tests)

        q = measure(arr, quick.quick_select, resolution, k_values)
        h = measure(arr, heap.heap_select, resolution, k_values)
        m = measure(arr, median.median_of_medians_select, resolution, k_values)

        points[i] = (n, 
            q,
            h,
            m            
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
    

    '''
        Draw mean execution time reference line for each algorithm
    '''

    q_sum = 0
    h_sum = 0
    m_sum = 0

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
    plt.plot(xs, mean_median_select, '--', color='red', label='Tempo medio Median of Median select')

    plt.show()

main()