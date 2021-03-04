def squaresum(n):
    s = 0
    for i in range(1, n+1) : 
        s = s + (i * i) 
    return s

n= int (input ("Enter the number: "))
print ("sum of squares of first n natural numbers: ", squaresum(n))