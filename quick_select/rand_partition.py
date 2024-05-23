import partition
import random


def rand_partition(a, low, high):
    i = random.randint(low, high-1)
    a[high-1], a[i] = a[i], a[high-1]
    return partition.partition(a, low, high)