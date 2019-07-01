#----------------------------------------#
# Question 1
# Level 1
#
# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method
#----------------------------------------#
def div_by_7_not_5(from_num, to_num):
    out = []
    for i in range(from_num, to_num):
        if i % 7 == 0 and i % 4 != 0:
            out.append(str(i))

    return ','.join(out)

div_by_7_not_5(2000,3200)

#----------------------------------------#
# Question 2
# Level 1
#
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#----------------------------------------#


def fat(num):
    if num == 0:
        return 1
    else:
        return num * fat(num-1)

# #----------------------------------------#
# Question 3
# Level 1
#
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# #----------------------------------------#


def dict_square(num):
    my_dict = {}
    for i in range(1,num+1):
        my_dict[i] = i ** 2

    return my_dict

# #----------------------------------------#
# Question 4
# Level 1
#
# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# #----------------------------------------#


def split_numbers(str):
    nums = str.split(',')
    return nums, tuple(nums)


# #----------------------------------------#
# Question 5
# Level 1
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters
# #----------------------------------------#
class myClass(object):
    def __init__(self):
        self.str = ""

    def get_string(self):
        self.str = input()

    def print_string(self):
        print(self.str.upper())


# #----------------------------------------#
# Question 7
# Level 2
#
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th
# row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a
# comma-separated form.
# #----------------------------------------#
def dim_array(x, y):
    my_array = [[0 for i in range(y)] for j in range(x)]

    for i in range(x):
        for j in range(y):
            my_array[i][j] = i * j

    return my_array


# #----------------------------------------#
# Question 8
# Level 2
#
# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# #----------------------------------------#
def sort_words(words):
    my_words = words.split(',')
    my_words.sort()
    return ','.join(my_words)


# #----------------------------------------#
# Question 10
# Level 2
#
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
# duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.
# #----------------------------------------#
def split_remove_dup(words):
    out = []
    for word in words.split(' '):
        if word not in out:
            out.append(word)

    out.sort()
    return ' '.join(out)


# #----------------------------------------#
# Question 11
# Level 2
#
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# #----------------------------------------#
def divisible_by(nums):
    out = []
    for num in nums.split(','):
        if int(num) % 5 == 0:
            out.append(num)

    return ','.join(out)



# #----------------------------------------#
# Question 19
# Level 3
#
# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
# age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.
# #----------------------------------------#
from operator import itemgetter

def order_tuple(data):
    return sorted(data, key=itemgetter(0, 1, 2))


#----------------------------------------#
# Question 22
# Level 3
#
# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
#
# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input
#----------------------------------------#
def words_from_sentence(sentence):
    words = [word.lower() for word in sorted(sentence.split())]
    out = {}
    for word in words:
        if word in out:
            out[word] += 1
        else:
            out[word] = 1

    return out


#----------------------------------------#
# Question 25
# Level 1
#
# Question:
#     Define a class, which have a class parameter and have a same instance parameter.
#
# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later
#----------------------------------------#
class my_class_25:
    def __init__(self, parameter):
        self.parameter = parameter

obj = my_class_25("Douglas")


#----------------------------------------#
# Question:
#
# Please write a program which accepts basic mathematic expression from console and print the evaluation result.
#
# Example:
# If the following string is given as input to the program:
#
# 35+3
#
# Then, the output of the program should be:
#
# 38
#
# Hints:
# Use eval() to evaluate an expression.
#----------------------------------------#
def eval_math(str):
    return eval(str)
