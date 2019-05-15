#m = 51062111012908
#a = 2487143
m = 10
a = 3

for i in range(m):
    n = (a * i) % m
    if i%1000000 == 0:
        print(i)
    if n == 1:
        print("\nThe inverse of",a,"is = ",i)
        break
