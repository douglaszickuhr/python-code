"""
Write a function that returns the elements on odd positions (0 based) in a list
"""

def solution_1(input):
    output = list()
    for position in range(len(input)):
        if position % 2 != 0:
            output.append(input[position])
    return output


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


"""
Write a function that takes a number and returns a list of its digits
"""
def solution_3(input):
    number = str(input)
    output = list()
    for i in range(len(number)):
        output.append(int(number[i]))
    return output


def solution_3_2(input):
    return list(str(input))

