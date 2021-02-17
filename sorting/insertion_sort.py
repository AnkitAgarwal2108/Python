l = [21, 13, 26, 15, 3, 7, 18]


def insertion_sort(l):
    for i in range(1, len(l)):
        current_index = i
        current_value = l[i]
        while current_index > 0 and l[current_index - 1] > current_value:
            l[current_index] = l[current_index - 1]
            current_index -= 1
        l[current_index] = current_value
    return l


print(insertion_sort(l))
