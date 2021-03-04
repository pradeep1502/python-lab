def search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return 1
  
    return -1
arr= input("Enter list of linear : ").strip().split()
x= input("enter number to search: ")
print(search(arr,x))