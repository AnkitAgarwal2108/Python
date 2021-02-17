l = [21, 13, 26, 15, 3, 7, 18]


def merge(l, left_index, right_index, middle):
    left_copy = l[left_index:middle + 1]
    right_copy = l[middle + 1:right_index + 1]
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            l[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            l[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1
    while left_copy_index < len(left_copy):
        l[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        l[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_sort(l, left_index, right_index):
    if left_index >= right_index:
        return
    middle = (left_index + right_index) // 2
    merge_sort(l, left_index, middle)
    merge_sort(l, middle + 1, right_index)
    merge(l, left_index, right_index, middle)


merge_sort(l, 0, len(l) - 1)
print(l)
