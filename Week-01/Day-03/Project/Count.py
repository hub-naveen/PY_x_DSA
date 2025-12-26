def count_even_odd(arr):
    even = 0
    odd = 0

    for x in arr:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


nums = [1, 2, 3, 4, 5, 6]
print(count_even_odd(nums))
