# O maior

numbers = input().split()
first_number = int(numbers[0])
second_number = int(numbers[1])
third_number = int(numbers[2])

largest = first_number

if second_number > largest:
    largest = second_number
if third_number > largest:
    largest = third_number
print(f'{largest} eh o maior')
