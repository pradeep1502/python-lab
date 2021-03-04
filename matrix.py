def getMatrix():
    n = int(input("Enter number of rows in matrix : "))
    m = int(input("Enter number of columns in matrix : "))

    A = []
    i = 0
    while(i<n):
        R = input("Enter row "+str(i+1)+" of matrix : ").strip().split()
        if(len(R)!=m):
            print("Wrong size of inputs!")
        else:
            A.append([int(i) for i in R])
            i+=1

    return A

print("First Matrix : ")
X = getMatrix()
print("Second Matrix : ")
Y = getMatrix()

nx = len(X)
mx = len(X[0])
ny = len(Y)
my = len(Y[0])
if(mx!=ny):
    print("Cannot multiply matrices")
else:
    result = [[0]*my for i in range(nx)]
    for i in range(len(X)):
    
        for j in range(len(Y[0])):
            
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    for r in result:
        print(r)