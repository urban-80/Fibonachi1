f1=1
f2=1

n = int(input("введите значение: "))

for i in range(2, n):
    f1,f2 = f2, f1 + f2

print(f2)