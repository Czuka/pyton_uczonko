
sorted_list = [1,2,3,4,5,6,7,8,9,10]
target1 = 2
target2 = 10





def binary_serch(list,element):
    middle =0
    start =0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Step ",steps, " : ", str(list[start:end+1]))

        steps=steps+1
        middle = (start+end) //2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle-1
        else:
            start = middle +1


    return -1





binary_serch(sorted_list,target1)
binary_serch(sorted_list,target2)





























