def buble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                buffer = array[j]
                array[j] = array[j+1]
                array[j+1] = buffer
    return array
a = [int(s) for s in input().split()]
print(buble(a))