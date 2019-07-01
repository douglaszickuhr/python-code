for i, j in enumerate(['douglas', 'petra', 'filipa'], start=332):
    print(i, j)


my_numbers = [45, 22, 14, 65, 97, 72]

for i, num in enumerate(my_numbers):
    if num % 3 == 0 and num % 5 == 0:
        my_numbers[i] = "fizbuzz"
    elif num % 3 == 0:
        my_numbers[i] = "fizz"
    elif num % 5 == 0:
        my_numbers[i] = "buzz"


print(my_numbers)
