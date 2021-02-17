from heapq import heappop, heappush

l = [21, 13, 26, 15, 3, 7, 18]


def heap_sort(l):
    heap = []
    for i in l:
        heappush(heap, i)
    order_list = []
    while heap:
        order_list.append(heappop(heap))

    return order_list


print(heap_sort(l))
