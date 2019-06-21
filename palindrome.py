def is_palindrome(word):
    word = word.casefold()
    return word[::-1] == word

print(is_palindrome('Deleveled'))
