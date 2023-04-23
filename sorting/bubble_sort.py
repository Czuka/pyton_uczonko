import random
import time

random_list = []
random_list_copy = []
iterated_list = []
iterated_list_copy = []

for i in range(10000):
    random_list.append(random.randint(1, 40000))

for i in range(10000):
    iterated_list.append(10000-i)
print(random_list)
print(iterated_list)
def bubbleSort(lst):
    for i in range (len(lst)-1):
        for j in range( len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    return lst
def shake_sort(lst):
    swapped = True
    start = 0
    end = len(lst)

    while swapped:
        swapped = False
        for i in range(start, end-1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end -1
        for j in range(end-1, start, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                swapped = True
        start += 1
    return lst

random_list_copy = random_list.copy()
start_time = time.time()
bubbleSort(random_list_copy)
end_time = time.time()
print("random bubble:",random_list_copy)
print("time: ", end_time-start_time )

iterated_list_copy = iterated_list.copy()
start_time = time.time()
bubbleSort(iterated_list_copy)
end_time = time.time()
print("iterated bubble: ",iterated_list_copy)
print("time: ", end_time-start_time )


random_list_copy2 = random_list.copy()
start_time = time.time()
shake_sort(random_list_copy2)
end_time = time.time()
print("random shake:", random_list_copy2)
print("time: ", end_time-start_time )

iterated_list_copy3 = iterated_list.copy()
start_time = time.time()
shake_sort(iterated_list_copy3)
end_time = time.time()
print("iterated shake:",iterated_list_copy3)
print("time: ", end_time-start_time )


