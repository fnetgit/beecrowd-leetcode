# Seis Números Ímpares


data = int(input())
for _ in range(6):
    if data % 2 == 0:
        data += 1
    print(data)
    data += 2


# Fiz esse primeiro, mas deu erro

# data = int(input())
# for _ in range(6):
#     data += 1
#     if data % 2 == 0:
#         data += 1
#     print(data)
