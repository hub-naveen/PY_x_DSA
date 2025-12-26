def find_max(arr):
    m = arr[0]
    for x in arr:
        if x > m:
            m = x
    return m


def find_min(arr):
    m = arr[0]
    for x in arr:
        if x < m:
            m = x
    return m


nums = [5, 9, 2, 7]
print(find_max(nums))
print(find_min(nums))
