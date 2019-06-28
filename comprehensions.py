def comp(x, y, z, n):
    L = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:
                    L.append([i, j, k])
    return L


def comp_2(x, y, z, n):
    return [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

