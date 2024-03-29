def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    for i in range(len(numbers)):
        for j in range(len(numbers) - i):
            if numbers[i] + numbers[j] == target_sum:
                return tuple([i, j])

print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
