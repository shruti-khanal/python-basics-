n=int (input("enter a number "))
flag=0;
if (n==0) or (n==1):
    flag=1
elif (n==2):
    flag=0
else:
    for i in range (2,n):
        if (n%i==0):
            flag=1
            break
if flag ==0:
    print("prime")
else:
    print("not prime ")    







