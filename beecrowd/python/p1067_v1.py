# Números Ímpares

number = int(input())
odds = []
while True:
    if number > 0:
        if number % 2 != 0:
            odds.append(number)
            number -= 1
        else:
            number -= 1
    else:
        odds.reverse()
        for odd in odds:
            print(odd)
        break
