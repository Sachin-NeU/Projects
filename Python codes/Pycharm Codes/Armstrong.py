def numofdigits(x):
    n=0
    while (x!=0):
        n=n+1
        x=int(x/10)
    return n

x=int(input("Enter a number: "))
print(type(x))
n=numofdigits(int(x))
print("Number of digits in ",x," is: ",n)
x1=int(x)
tmp=int(x)%10
sum=0
print(tmp,x)
for i in range(n):
    sum=sum+pow(tmp,n)
    x=x/10
    tmp=int(x)%10
    print(x,tmp,sum)

print(sum,x1)
if sum==x1:
    print("Armstrong number.")
else:
    print("Not an armstrong number.")
