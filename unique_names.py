def unique_names(names1, names2):
    unique = list()
    for names in [names1, names2]:
        for name in names:
            if name not in unique:
                unique.append(name)
    return unique


names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]

# should print Ava, Emma, Olivia, Sophia
print(unique_names(names1, names2))
