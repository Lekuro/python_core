n = 101

for i in range(0, n, 2):
    print(i, end='_')
print()

i = 0
while i < n:
    if i % 2 == 0:
        print(i, end='_')
    i += 1
print()

print(list(range(0, n, 2)))
print([i for i in range(0, n, 2)])
