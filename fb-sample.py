"""
Write a function that returns the elements on odd positions (0 based) in a list
"""

def solution_1(input):
    output = list()
    for position in range(len(input)):
        if position % 2 != 0:
            output.append(input[position])
    return output


assert solution_1([0,1,2,3,4,5]) == [1,3,5]
assert solution_1([1,-1,2,-2]) == [-1,-2]


"""
Write a function that returns the cumulative sum of elements in a
list
"""
def solution_2(input):
    output = list()

    for i in range(len(input)):
        if i == 0:
            output.append(input[i])
        else:
            output.append(input[i] + output[i-1])
    return output

assert solution_2([1,1,1]) == [1,2,3]
assert solution_2([1,-1,3]) == [1,0,3]


"""
Write a function that takes a number and returns a list of its digits
"""
def solution_3(input):
    number = str(input)
    output = list()
    for i in range(len(number)):
        output.append(int(number[i]))
    return output

assert solution_3(123) == [1,2,3]
assert solution_3(400) == [4,0,0]


"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3"""

def centered_average(nums):
    total = sum(nums[1:len(nums)-1])
    # for i in range(len(nums)-1):
    #     print("Number: {}".format(nums[i]))
    #     if i > 0:
    #         print("Added to output: {}".format(nums[i]))
    #         total = total + nums[i]

    return int(total // (len(nums)-2))

"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""
def string_match(a, b):
    short = min(len(a), len(b))
    count = 0

    for i in range(short - 1):
        print(i)
        print(i + 2)
        print("Numbers A: {}".format(a[i:i + 2]))
        print("Numbers B: {}".format(b[i:i + 2]))
        if a[i:i + 2] == b[i:i + 2]:
            count += 1

    return count


def last2(str):
    count = 0
    for i in range(len(str)-2):
        local = str[i] + str[i+1]

    return count

def make_tags(tag, word):
  return "<{0}>{1}</{0}>".format(tag,word)

def in1to10(n, outside_mode):
    print(n in list(range(1,11)))
    print(outside_mode)
    print(n <= 1 or n >= 10)
    print(outside_mode and (n <= 1 or n >= 10))
    x = n in range(1,10) or (outside_mode and (n <= 1 or n >= 10))
    print(x)
    return x

def sum13(nums):
  total = 0
  for i in range(len(nums)):
    if nums[i] != 13:
      if nums[i-1] != 13:
        total += nums[i]
  return total

