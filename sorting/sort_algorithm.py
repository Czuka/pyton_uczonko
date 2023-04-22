import random
import time

random_list = []
random_list_copy = []
iterated_list = []
iterated_list_copy = []

for i in range(100):
    random_list.append(random.randint(1, 200))

for i in range(100):
    iterated_list.append(100-i)
print(random_list)
print(iterated_list)



def insertion_sort_for(list):
    for i in range(1, len(list)):
        for j in range(i - 1, 0, -1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            else: break

def insertion_sort_while(list):
    for i in range(1, len(list)):
        j=i-1
        while list[j] > list[j+1] and j>= 0:
            list[j], list[j + 1] = list[j + 1], list[j]
            j-=1

def insertion_shifting(list):
    for i in range(1,len(list)):
        curent_number = list[i]
        for j in range(0,0,-1):
            if list[j] < curent_number:
                list[j-1]=list[j]
            else:
                list[j-1] = curent_number
                break


random_list_copy = random_list.copy()
start_time = time.time()
insertion_sort_for(random_list_copy)
end_time = time.time()
print("random for: " ,random_list_copy)
print("time: ", end_time-start_time )

iterated_list_copy = iterated_list.copy()
start_time = time.time()
insertion_sort_for(iterated_list_copy)
end_time = time.time()
print("iterated for:",iterated_list_copy)
print("time: ", end_time-start_time )

random_list_copy = random_list.copy()
start_time = time.time()
insertion_sort_while(random_list_copy)
end_time = time.time()
print("random while: ",random_list_copy)
print("time: ", end_time-start_time )

iterated_list_copy = iterated_list.copy()
start_time = time.time()
insertion_sort_while(iterated_list_copy)
end_time = time.time()
print("iterated while: ",iterated_list_copy)
print("time: ", end_time-start_time )



random_list_copy = random_list.copy()
start_time = time.time()
insertion_shifting(random_list_copy)
end_time = time.time()
print("insertion_shifting random: ",random_list_copy)
print("time: ", end_time-start_time )

iterated_list_copy = iterated_list.copy()
start_time = time.time()
insertion_shifting(iterated_list_copy)
end_time = time.time()
print("insertion_shifting iterated:", iterated_list_copy)
print("time: ", end_time-start_time )