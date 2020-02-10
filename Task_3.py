string = str(input())
string_to_array = string.split()
for i in range(len(string_to_array)):
    if string_to_array.count(string_to_array[i]) == 1:
        print(string_to_array[i])
