from math import sqrt
def kClosest(points, K):
    dist_from_center = []
    for point in points:
        dist = sqrt((point[0])**2 + point[1]**2)
        dist_from_center.append([dist,[point[0],point[1]]])

    return sorted(dist_from_center)[:K+1]