chain = str(input())
stack = []
dictionary = ['(',')','{','}','[',']']
if len(chain)%2 != 0:
    print('нсп')
    stack = ['1']
else:
    for i in range(len(chain)):
        if chain[i] == dictionary[0] or chain[i] == dictionary[2] or chain[i] == dictionary[4]:
            stack.append(chain[i])
        else:
            if chain[i] == dictionary[1] or chain[i] == dictionary[3] or chain[i] == dictionary[5]:
                if len(stack) == 0:
                    stack = ['1']
                    print('нсп')
                    break
                elif stack[-1] and chain[i] in dictionary:
                    stack.pop()
                else:
                    print('нсп')
if len(stack) == 0:
    print('псп')