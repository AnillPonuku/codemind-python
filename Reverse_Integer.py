
n=int(input())
x=n
if(n<1):
    n=-n
s=0
while(n):
    r=n%10
    s=s*10+r
    n=n//10
if(x<0):
    print(-s)
else:
    print(s)