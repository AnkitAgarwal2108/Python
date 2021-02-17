l = [21, 13, 26, 15, 3, 7, 18]


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


print(bubble_sort(l))
