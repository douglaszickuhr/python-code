# Pairs with Specific Difference
# Given an array arr of distinct integers and a nonnegative integer k, write a function
# findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k.
# If no such pairs exist, return an empty array.
#
# Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

# Naive solution
# Space: O(1)
# Time: O(n^2)
def find_pairs_with_given_difference(arr, k):
    out = []

    for x in range(len(arr)):
        for y in range(len(arr)):
            if x != y:
              if (arr[y]-arr[x]) == k:
                out.append([arr[y], arr[x]])
    return out


# Optimised solution
# Space: O(N)
# Time: O(N log(N)) worst scenario
def find_pairs_with_given_difference(arr, k):
    if k == 0:
        return []

    map = {}
    answer = []

    for x in arr:
        map[x - k] = x

    for y in arr:
        if y in map:
            answer.append([map[y],y])

    return answer