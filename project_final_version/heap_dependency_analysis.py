import time
import random
import matplotlib.pyplot as plt
import platform

import heap_select as heap


# DEPENDENCY ANALYSIS: 
# how k parameter affects performance of heap-select algorithm


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
    random.seed()                                                       
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(0, max_rand_val)
    return arr


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
    tot_sum = 0    
    for i in range(iterations):
        tot_sum += resolution()
    return tot_sum / iterations


'''
   Measure the time required for a single execution
   of function on array with given k
'''
def measure(arr, function, mean_resolution, k, executions):                         
    min_err = 0.001                                                     
    min_time = mean_resolution * ((1/min_err) + 1)                      
    count = 0                                                           
    start_time = get_time()

    while True:
        for i in range(executions):
            a_copy = arr.copy()
            function(a_copy, 0, len(arr), k)

        count = count + 1
        end_time = get_time()
        if end_time - start_time >= min_time:
             break

    return (end_time - start_time) / count


'''
    Run a single function over the same array
    While k parameter iterates over every legal index of array
    Record times for each iteration and total duration
'''
def test_function(function, arr, executions):
    mean_resolution = calculate_mean_resolution(1000)
    timings = [0] * len(arr)

    test_start_time = get_time()

    for k in range(len(arr)):
        print(f"Test number: {k+1:8}\tProgress: {int(((k+1) / len(arr))*100):3.2f}%", end='\r')
        timings[k] = (k, measure(arr, function, mean_resolution, k, executions))
    
    test_duration = get_time() - test_start_time

    return timings, test_duration


'''
    Put the record times of a function test on a plot
'''
def plot_results(timings, color, function_name):
    xs, ys = zip(*timings)    
    plt.scatter(xs, ys, c=color, label=function_name)


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
    Test heap select algorithm on given array size
    k parameter iterates over the entire array
    so that each and every index is passed exactly once
    in the function call
    Measure time required for completion
    Plot results and show graph
'''
def run_dependency_test():
    array_length = 1000
    max_rand_val = 1000000
    executions = 10
    arr = init_array(array_length, max_rand_val)

    print("\nTesting Min-Max Heap Select algorithm:")
    min_max_timings, min_max_duration = test_function(heap.heap_select, arr, executions)
    plot_results(min_max_timings, 'lightgreen', 'Min-Max Heap')
    print("\nDone\n")

    print("Testing Min-Heap Select algorithm:")
    min_timings, min_duration = test_function(heap.select_min_heap, arr, executions)
    plot_results(min_timings, 'orange', 'Min-Heap')
    print("\nDone\n")

    total_execution_sum = min_max_duration + min_duration

    min_max_percentage = min_max_duration / total_execution_sum
    min_percentage = min_duration / total_execution_sum

    plt.xscale('linear')
    plt.yscale('linear')
    plt.legend(fontsize=16)

    print(f'{"MinMax Heap duration:":30} {make_readable(min_max_duration)} -> {(min_max_percentage * 100):.2f}%\n{"Min Heap duration:":30} {make_readable(min_duration)} -> {(min_percentage * 100):.2f}%\n{"Total time:":30} {make_readable(total_execution_sum)}')
    print(f'\n{f"Array length: {array_length}":8}\n{f"Executions for each k-value: {executions}":8}')

    plt.show()


if __name__ == '__main__':
    run_dependency_test()