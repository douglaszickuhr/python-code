my_list = [["A","B"],["A","C"],["B","D"],["B","C"],["R","M"], ["S"],["P"], ["A"]]


def friends(L):
    friends = {}
    for item in L:
        if len(item) > 1:
            if item[0] in friends:
                friends[item[0]].append(item[1])
            else:
                friends[item[0]] = [item[1]]

    return friends