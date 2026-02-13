# Sort Simples

n1, n2, n3 = map(int, input().split())

values = [n1, n2, n3]
ascending_order = sorted(values)
for number in ascending_order:
    print(number)
print(f'\n{n1}\n{n2}\n{n3}')
