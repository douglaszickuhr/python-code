def count_vowels(word):
    vowels = 'aeiou'
    return len([x for x in word if x.lower() in vowels])

animals = ['cat', 'dog', 'cheetah', 'rhino', 'bear']

sorted(animals, key=lambda animal:count_vowels(animal), reverse=True)

