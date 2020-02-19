def find(number):
    array = [int(s) for s in input().split()]
    first = 0
    last = len(array)
    if number > array[last-1]:
        print('число', number, 'не входит в массив')
    else:
        while first <= last:
            m = (last + first)//2
            if number > array[m]:
                first = m+1
            elif number < array[m]:
                last = m-1
            else:
                print('число', number, 'входит в массив')
                break
        else:
            print('число', number, 'не входит в массив')