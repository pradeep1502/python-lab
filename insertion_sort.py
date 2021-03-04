def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
arr = input("Enter list : ").strip().split()
arr = [int(i) for i in arr]
insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print (arr[i], end= " ") 