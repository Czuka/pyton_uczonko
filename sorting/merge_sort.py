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



def merge(list):
    for i in range (len(list)-1):
        for j in range( len(list)-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1], list[j]
    return list

start_time = time.time()
bubbleSort(random_list)
end_time = time.time()
print("iterated for:",random_list)
print("time: ", end_time-start_time )

start_time = time.time()
bubbleSort(iterated_list)
end_time = time.time()
print("iterated for:",iterated_list)
print("time: ", end_time-start_time )
