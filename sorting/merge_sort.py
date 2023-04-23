import random
import time

random_list = []
random_list_copy = []
iterated_list = []
iterated_list_copy = []

for i in range(10000):
    random_list.append(random.randint(1, 1000000))

for i in range(10000):
    iterated_list.append(10000-i)
print(random_list)
print(iterated_list)



def merge_sort(lst):
    merge_sort_inplace(lst,0,len(lst)-1)

def merge_sort_inplace(lst, start, end):
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort_inplace(lst, start, mid)
    merge_sort_inplace(lst, mid + 1, end)
    merge_inplace(lst, start, mid, end)


def merge_inplace(lst, start, mid, end):
    left = lst[start:mid + 1]
    right = lst[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1




random_list_copy = random_list.copy()
start_time = time.time()
merge_sort(random_list_copy)
end_time = time.time()
print("random merge_sort :",random_list_copy)
print("time: ", end_time-start_time )


start_time = time.time()
merge_sort(iterated_list)
end_time = time.time()
print("iterated merge_sort:",iterated_list)
print("time: ", end_time-start_time )
