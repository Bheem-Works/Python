
# find the smallest number 

def find_smallest(arr):
    smallest = arr[0]
    for i in range(0,len(arr)):
        if arr[i] < smallest :
            smallest = arr[i]

    return smallest
result = [1,0,-2]
print(find_smallest(result))


# find the largest number 

def find_largest(arr):
    largest = arr[0]
    for i in range(0,len(arr)):
        if arr[i] > largest :
            largest = arr[i]

    return largest
showResult = [3,9,2]
print(find_largest(showResult))