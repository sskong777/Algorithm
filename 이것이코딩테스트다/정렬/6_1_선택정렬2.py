array = [7,5,9,0,3,1,6,2,4,8]



def selectionsort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

selectionsort(array)
print(array)