# Project 2021 
# Initial set up. adding blank files
from random import randint
import time



# Test Print function
def test():
    print("This is a test function")
    
test()

# Random Array
def randomArray(n):
    array = []
    for i in range (0,n,1):
        # source: https://docs.python.org/3/library/random.html
        array.append(randint(0,1000))
    return array

#Print 100 numbers array
#print(randomArray(1000))

# Bubble Sort
# Source: https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def bubbleSort(arr):
    
    n = len(arr)
        
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

#start Timer
startTime = time.time()

arr = randomArray(1000)
bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
    


# End timer
endTime = time.time()

#elapsed time
elapsedTime = endTime - startTime
print("----------------------------------------------------")
print("Bubble Sort took ", elapsedTime*100, " miliseconds")

#Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Code to print the list

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
#start Timer
startTime = time.time()
# Driver Code
if __name__ == '__main__':
    #arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    
# End timer
endTime = time.time()

#elapsed time
elapsedTime = endTime - startTime
print("----------------------------------------------------")
print("Merge Sort took ", elapsedTime*100, " miliseconds")

