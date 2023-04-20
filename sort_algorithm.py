import random
import time

random_list = []
random_list_copy = []
iterated_list = []
iterated_list_copy = []

for i in range(1000):
    random_list.append(random.randint(1, 2000))

for i in range(1000):
    iterated_list.append(1000-i)
print(random_list)
print(iterated_list)

def copy_list(primary_list, copy_list):
    for i in range(0,len(primary_list)):
        copy_list.append(primary_list[i])


def insertion_sort_for(list):
    for i in range(1, len(list)):
        for j in range(i - 1, -1, -1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            else: break

def insertion_sort_while(list):
    for i in range(1, len(list)):
        j=i-1
        while list[j] > list[j+1] and j>= 0:
            list[j], list[j + 1] = list[j + 1], list[j]
            j-=1


copy_list(random_list , random_list_copy)
start_time = time.time()
insertion_sort_for(random_list_copy)
end_time = time.time()
print("random for: " ,random_list_copy)
print("time: ", end_time-start_time )

copy_list(iterated_list,iterated_list_copy)
start_time = time.time()
insertion_sort_for(iterated_list_copy)
end_time = time.time()
print("iterated for:",iterated_list_copy)
print("time: ", end_time-start_time )

copy_list(random_list,random_list_copy)
start_time = time.time()
insertion_sort_while(random_list_copy)
end_time = time.time()
print("random while: ",random_list_copy)
print("time: ", end_time-start_time )

copy_list(iterated_list,iterated_list_copy)
start_time = time.time()
insertion_sort_while(iterated_list_copy)
end_time = time.time()
print("iterated while: ",iterated_list_copy)
print("time: ", end_time-start_time )