# Par ou Ímpar

user_input = int(input(''))
for _ in range(user_input):
    x = int(input())
    if x == 0:
        print('NULL')
    elif x % 2 == 0:
        if x < 0:
            print('EVEN NEGATIVE')
        else:
            print('EVEN POSITIVE')
    elif x % 2 != 0:
        if x < 0:
            print('ODD NEGATIVE')
        else:
            print('ODD POSITIVE')
