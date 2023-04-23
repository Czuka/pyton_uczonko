import random
import time


def cocktail_shaker_sort(list):
    for i in range(len(list) - 1, 0, -1):
        is_swapped = False

        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                is_swapped = True

        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                is_swapped = True

        if not is_swapped:
            return list

list1 = [5, 1, 4, 2, 8, 0, 2]
list2 = []
cocktail_shaker_sort(list1)
print("Sorted array is:")
for i in range(len(list1)):
    print("%d" % list1[i])

print(list1)

random_list = []
random_list_copy = []
iterated_list = []
iterated_list_copy = []

for i in range(100):
    random_list.append(random.randint(1, 400))

for i in range(100):
    iterated_list.append(100-i)
print(random_list)
print(iterated_list)


print(random_list)
cocktail_shaker_sort(random_list)
print("random list: ", random_list)

print(iterated_list)
cocktail_shaker_sort(iterated_list)
print("iterated sort: ",iterated_list)

