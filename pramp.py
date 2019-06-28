def find_pairs_with_given_difference_1(arr, k):
    out = []
    for values in [(i, j) for i in range(len(arr)) for j in range(len(arr)) if i != j]:
        if arr[values[1]] - arr[values[0]] == k:
            out.append([arr[values[1]], arr[values[0]]])

    return out

def find_pairs_with_given_difference_2(arr, k):
    out = []

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if (arr[j]-arr[i]) == k:
                    out.append([arr[j], arr[i]])

    return out


# Optimised solution
# Space: O(N)
# Time: O(N log(N)) worst scenario
def find_pairs_with_given_difference(arr, k):
    print("k value is {}".format(k))
    if k == 0:
        return []

    map = {}
    answer = []

    for x in arr:
        print("x value is: {}".format(x))
        print("x - k value is: {}".format(x - k))
        map[x - k] = x

    print(map)

    for y in arr:
        print("y value is: {}".format(y))
        if y in map:
            print("map[y] value is: {}".format(map[y]))
            print("y value is: {}".format(y))
            answer.append([map[y], y])

    return answer

