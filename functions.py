def greatest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    if b>a:
        if b>c: 
            return b
        else:
            return c

n=greatest(10,20,30)
print(f"the greates of three numbers is {n}")           


