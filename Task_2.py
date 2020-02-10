def find(number):
    array = [int(s) for s in input().split()]
    if int(number in array) == 1:
        print('число', number, 'входит в массив')
    else:
        print('число', number, 'не входит в массив')