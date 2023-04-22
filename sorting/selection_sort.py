
import random
import time

random_list = []
random_list_copy = []
iterated_list = []
iterated_list_copy = []

for i in range(1000):
    random_list.append(random.randint(1, 4000))

for i in range(1000):
    iterated_list.append(1000-i)
print(random_list)
print(iterated_list)



def selecion_sort(list):
    for i in range(0, len(list)-1):
        minIndex =i
        for j in range (i+1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
            list[i],list[minIndex] = list[minIndex],list[i]
    return list


def selectionSort(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i + 1, len(list)):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if list[j] < list[min_idx]:
                min_idx = j

        # put min at the correct position
        (list[i], list[min_idx]) = (list[min_idx], list[i])



random_list_copy = random_list.copy()
start_time = time.time()
selectionSort(random_list_copy)
end_time = time.time()
print("random for: " ,random_list_copy)
print("time: ", end_time-start_time )

iterated_list_copy = iterated_list.copy()
start_time = time.time()
selectionSort(iterated_list_copy)
end_time = time.time()
print("random for: " ,iterated_list_copy)
print("time: ", end_time-start_time )


random_list_copy = random_list.copy()
start_time = time.time()
selecion_sort(random_list_copy)
end_time = time.time()
print("random for: " ,random_list_copy)
print("time: ", end_time-start_time )

iterated_list_copy = iterated_list.copy()
start_time = time.time()
selecion_sort(iterated_list_copy)
end_time = time.time()
print("random for: " ,iterated_list_copy)
print("time: ", end_time-start_time )