def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           return greater
       greater+=1


a= int(input("enter 1st number: "))
b= int(input("enter 2nd number: "))

print("The L.C.M. is", compute_lcm(a,b))


