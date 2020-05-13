#N^2
def bubbleSoport(arr):
    newArr = arr
    n = len(arr)
    for i in range(n):## outer loop
        for j in range(0,n-1-i):## inner loop
            if newArr[j]>newArr[j+1]: 
                newArr[j],newArr[j+1] = newArr[j+1], newArr[j] ## swap elements          
    return newArr
       
#NLOG(N)             
def quickSort(arr):
    right = []
    mid = [] 
    left = []
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i == pivot :
           mid.append(i)
        elif i > pivot:
           right.append(i)       
    return  quickSort(left) + mid + quickSort(right)
    
  # n^2
def selctionSort(arr):
    newArr = arr
    n = len(arr)
    for i in range (n):
        mid = i 
        for j in range(i+1,n):
            if newArr[mid] > newArr[j]:
                mid = j
    newArr[i], newArr[mid] = newArr[mid], newArr[i]
    print ("complexity time is N^2")
    return newArr
        
