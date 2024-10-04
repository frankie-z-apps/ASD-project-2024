import time
import random
import matplotlib.pyplot as plt

import heap_select as heap

# DEPENDENCY ANALYSIS: 
# how k parameter affects performance of heap-select algorithm

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
    Create n copies of arr
'''
def create_copies(arr, n):
    copies = [arr] * n
    return copies


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
    tot_sum = 0    
    for i in range(iterations):
        tot_sum += resolution()
    return tot_sum / iterations


'''
   Measure the time required for a single execution
   of function on array with given k
'''
def measure(arr, function, mean_resolution, k):                         
    min_err = 0.001                                                     
    min_time = mean_resolution * ((1/min_err) + 1)                      
    count = 0                                                           
    start_time = time.monotonic()

    while True:        
        #a_copy = arr.copy()
        function(arr, 0, len(arr), k)

        count = count + 1
        end_time = time.monotonic()
        if end_time - start_time >= min_time:
             break

    return (end_time - start_time) / count


'''
    Test heap select algorithm on given array size
    k parameter iterates over the entire array
    so that each and every index is passed only once
    in the function call
    Measure time required for completion
    Plot results and show graph
'''
def main():
    array_length = int(input("Input test array size: "))
    resolution = calculate_mean_resolution(1000)        
    max_rand_val = 1000000
    points = [(None)] * array_length
    arr = init_array(array_length, max_rand_val)
    #print("Creating array copies...")
    copies = create_copies(arr, array_length)
    #print("Done")

    main_duration_start = time.monotonic()

    for i in range(array_length):
        print(f"Test number: {i+1}  Progress: {int((i / array_length)*100)}%", end='\r')

        points[i] = (i, 
            measure(copies[i], heap.heap_select, resolution, i),
            #measure(copies[i], heap.select_min_heap, resolution, i)
        )

    main_duration_end = time.monotonic()

    xs, ys1 = zip(*points)
    plt.xscale('linear')
    plt.yscale('linear')
    plt.scatter(xs, ys1, c='lightgreen', label='Min-Max heap')  
    #plt.scatter(xs, ys2, c='orange', label='Min heap')
    plt.legend(title="K-dependency analysis")


    plt.annotate(f"Array size: {array_length}\nMax random value for array element: {max_rand_val}\nTotal execution time (seconds): {main_duration_end - main_duration_start}", \
                xy=(0.0, -0.128), \
                xycoords='axes fraction', \
                ha='left', \
                fontsize=7)

    plt.show()

main()