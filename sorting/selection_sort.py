l = [21, 13, 26, 15, 3, 7, 18]


def selection_sort(l):
    for pos in range(len(l)):
        min_pos = pos
        for i in range(pos, len(l)):
            if l[min_pos] > l[i]:
                min_pos = i
        l[pos], l[min_pos] = l[min_pos], l[pos]
    return l


print(selection_sort(l))
