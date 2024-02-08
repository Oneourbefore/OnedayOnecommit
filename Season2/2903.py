a=int(input())
def function(n):
    if n==1:
        return 3
    if n==2:
        return 5
    else:
        return 2*function(n-1)-1
    
print(function(a)**2)
    