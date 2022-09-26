def count_down(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list

print(count_down(5))


def arr_print(arr):
    print(arr[0])
    return(arr[1])
print(arr_print([1, 2]))

def first_plus_length(arr):
    return arr[0] + len(arr)

print(first_plus_length([1, 2, 3, 4, 5]))

def greater_than_second(arr):
    list = []
    for i in range(len(arr)):
        if i > arr[1]:
            list.append(i)
    return list
            
print(greater_than_second([5,2,3,2,1,4]))




def length_and_value(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list

print(length_and_value(4,7))










