words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


for i in range(10):
    print(i)
print("\n")

for i in range(100,110):
    print(i)
print("\n")

for i in range(100,1000,200):
    print(i)
print("\n")


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')

while True:
    pass