def divisors(n):
    div = 2
    for div in range(2,n//2+1):
        if n%div==0:
            print(f'{div} is a divisor,end=')

cnt = True
while cnt:
    ans =int(input("Enter a number"))
    divisors(ans)
    ct = input("Do you want to continue?")
    if ct=="n":
        break