import partition

# QUICK SELECT ITERATIVE VERSION (FIXED PIVOT)


def quick_select_iter_fixed(a, low, high, k):
    if not(are_parameters_valid(low, high, k)):
        return f"Index of k({k}) is out of range.\nPlease insert a valid index."
    else:
        return iter_quick_select_tested(a, low, high, k)
    

# verify that the array is not empty and that the value of k is in array range  
def are_parameters_valid(low, high, k):
    return not ((high - low < 1) or (k-1 < low or k-1 > high-1))


# we're assuming that the parameters are valid
def iter_quick_select_tested(a, low, high, k):
    r = partition.partition(a, low, high)
    while r != k-1:
        #print(f"Array: {a}")
        if r > k-1:
            #print(f"Array: {a}\nValue of r(index): {r}\nValue of a[r]: {a[r]}\nValue of k: {k}\nValue of k-1: {k-1}")
            r = partition.partition(a, low, r)
            #print(f"Array: {a}\nValue of r(index): {r}\nValue of a[r]: {a[r]}\nValue of k: {k}\nValue of k-1: {k-1}")
        else:
            #print(f"Array: {a}\nValue of r(index): {r}\nValue of a[r]: {a[r]}\nValue of k: {k}\nValue of k-1: {k-1}")
            r = partition.partition(a, r+1, high)
            #print(f"Array: {a}\nValue of r(index): {r}\nValue of a[r]: {a[r]}\nValue of k: {k}\nValue of k-1: {k-1}")
    return a[r]


def input_array():
    return [int(x) for x in input().split(" ") if x]

'''
a = input_array()
k = int(input())
print(quick_select_iter_fixed(a, 0, len(a), k))
#'''