n=int(input("enter the number"))
sumofdigits=0
i=1
while(i<=n):
    sumofdigits=sumofdigits+n%10
    n=n//10
    print(sumofdigits)
