a = [5, 8, 2, 1, 10, 25, 32, 45, 3, 8, 13, 7]
print(a)

for i in range(1, len(a)):
    for j in range(0, len(a)- i):
        if a[j] > a[j+1]:
            temporal = a[j]
            a[j] = a[j+1]
            a[j+1] = temporal
    print(a)

print('Después del bubble sort')
print(a)

