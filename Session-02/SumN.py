def sumn(n):
    res = 0
    for i in range(1, n+1):
        res+=i
    return res
print("sum of the 20 first integers: ", sumn(20))
print("Sum of the 100 frist integers: ", sumn(100))