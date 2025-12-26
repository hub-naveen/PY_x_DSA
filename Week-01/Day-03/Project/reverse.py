def reverse_list(arr):
    rev = []
    for x in arr:
        rev.insert(0, x)
    return rev


nums = [1, 2, 3, 4]
print(reverse_list(nums))


#Method 2
def reverse_inplace(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr
