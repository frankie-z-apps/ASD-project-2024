import quick_select.partition as partition
import random


def rand_partition(a, low, high):
    i = random.randint(low, high-1)
    #print(f"random index i: {i}\nValue of a[i]: {a[i]}")
    a[high-1], a[i] = a[i], a[high-1]
    return partition.partition(a, low, high)