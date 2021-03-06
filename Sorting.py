

#Code for heap 

def leftChild(i):
    return 2*i+1

def parent(i):
    return i//2

def rightChild(i):
    return 2*i+2



def heapify(arr,i,heapSize):
    #print("called for",arr,i)
    left=leftChild(i)
    right=rightChild(i)
    largest=i
    if left<heapSize and arr[left]>arr[i]:
        largest=left

    else:
        largest=i


    if right<heapSize and arr[right]>arr[largest]:
        largest=right


    if(largest!=i):
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,largest,heapSize)

    
def buildHeap(arr):
    
    for i in range((len(arr)-1)//2,-1,-1):
        
        heapify(arr,i,len(arr))



def heapSort(arr):
    heapSize=len(arr)
    buildHeap(arr)
    for i in range(len(arr)-1,0,-1):
    
        arr[0],arr[i]=arr[i],arr[0]
        heapSize-=1
        heapify(arr,0,heapSize)


arr=[27,17,3,16,13,10,1,5,7,12,4,8,9,0]

heapSort(arr)
print(arr)
        

    

#######################################################################
















def bubbleSort(arr):
    ''' worst case:bubble sort algorithm will do n(n+1) comparison in
        best case:n comparison for already sorted array
        
        '''
    switchMade=True;
    comp=0
    i=0
    while(i<len(arr)-1 and switchMade):
        
        switchMade=False
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                
                arr[j],arr[j+1]=arr[j+1],arr[j]
                switchMade=True
            comp+=1
        if not switchMade:
            return;

        i+=1;
    print(comp)


def insertionSort(arr):
    '''best case:already sorted array will do n comp.
     worse case:reverse sorted array will do n*n comp.
     engineering tweek:best for small cases due to constatnt factor'''
    comp=0
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        
        while j>=0 and arr[j]>key:
            comp+=1
            arr[j+1]=arr[j]
            j-=1

        arr[j+1]=key
    print(comp+1)
    
##
##arr=[9,8,7,6,5,4,3,2,1]
##insertionSort(arr)
##print(arr)


def merge(arr,start,end,mid):
    left_arr=[None]*(mid-start+1)
    right_arr=[None]*(end-mid)

    for i in range(0,len(left_arr)):
        left_arr[i]=arr[start+i]


    
    for i in range(0,len(right_arr)):
        right_arr[i]=arr[mid+i+1]

    i=0
    j=0
    left_arr.append(float('inf'))
    right_arr.append(float('inf'))
    for k in range(start,end+1):
        if left_arr[i]<=right_arr[j]:
            arr[k]=left_arr[i]
            i+=1
        elif left_arr[i]>right_arr[j]:
            arr[k]=right_arr[j]
            j+=1

        

    #print(left_arr,right_arr,arr)
        




def mergeSortRecursive(arr,start,end):
    if(start<end):
        mid=start+(end-start)//2
        mergeSortRecursive(arr,start,mid)
        mergeSortRecursive(arr,mid+1,end)
        merge(arr,start,end,mid)

def mergeSort(arr):
    start=0
    end=len(arr)-1

    mergeSortRecursive(arr,start,end)
    
        

##
##arr=[9,8,7,6,5,4,3,2,1]
##mergeSort(arr)
##print(arr)
