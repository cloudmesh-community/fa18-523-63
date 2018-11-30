# This code is authored by the project author


def bubble_sort(listing):
    for j in range(len(listing)-1,0,-1):
        for i in range(j):
            if listing[i] > listing[i + 1]:
                temp = listing[i]
                listing[i] = listing[i + 1]
                listing[i + 1] = temp
    return listing
