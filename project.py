# Project 2021 
# Initial set up. adding blank files
from random import randint
import time

timeArray = []

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
bubbleStartTime = time.time()

arr = randomArray(1000)
bubbleSort(arr)

#Test print array

#print ("Sorted array is:")
#for i in range(len(arr)):
#    print ("%d" %arr[i]),
    


# End timer
bubbleEndTime = time.time()

#elapsed time
bubbleElapsedTime = bubbleEndTime - bubbleStartTime
print("----------------------------------------------------")
print("Bubble Sort took ", bubbleElapsedTime*100, " miliseconds")
timeArray.append(bubbleElapsedTime)
# https://www.geeksforgeeks.org/merge-sort/
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
mergeStartTime = time.time()
# Driver Code
if __name__ == '__main__':
    #arr = [12, 11, 13, 5, 6, 7]
    #print("Given array is", end="\n")
    #printList(arr)
    mergeSort(arr)
    #print("Sorted array is: ", end="\n")
    #printList(arr)
    
# End timer
mergeEndTime = time.time()

numberOfTests = [100,100,100]
#elapsed time
mergeElapsedTime = mergeEndTime - mergeStartTime
timeArray.append(mergeElapsedTime)
print("----------------------------------------------------")
print("Merge Sort took ", mergeElapsedTime*100, " miliseconds")

headings = ["Sort type", "Time"]




import pandas


# Source: https://www.geeksforgeeks.org/counting-sort/


# Python program for counting sort
# which takes negative numbers as well

# The function that sorts the given arr[]
def count_sort(arr):
	max_element = int(max(arr))
	min_element = int(min(arr))
	range_of_elements = max_element - min_element + 1
	# Create a count array to store count of individual
	# elements and initialize count array as 0
	count_arr = [0 for _ in range(range_of_elements)]
	output_arr = [0 for _ in range(len(arr))]

	# Store count of each character
	for i in range(0, len(arr)):
		count_arr[arr[i]-min_element] += 1

	# Change count_arr[i] so that count_arr[i] now contains actual
	# position of this element in output array
	for i in range(1, len(count_arr)):
		count_arr[i] += count_arr[i-1]

	# Build the output character array
	for i in range(len(arr)-1, -1, -1):
		output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
		count_arr[arr[i] - min_element] -= 1

	# Copy the output array to arr, so that arr now
	# contains sorted characters
	for i in range(0, len(arr)):
		arr[i] = output_arr[i]

	return arr


# Driver program to test above function
countingStartTime = time.time()

count_sort(arr)

countingEndTime = time.time()

#elapsed time
countingElapsedTime = countingEndTime - countingStartTime

timeArray.append(countingElapsedTime)

print("----------------------------------------------------")
print("Counting Sort took ", countingElapsedTime*100, " miliseconds")


# Python program for implementation of Insertion Sort
# Source: https://www.geeksforgeeks.org/insertion-sort/
# Function to do insertion sort

def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key

        return arr


# Driver code to test above
insertionStartTime = time.time()

insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])

insertionEndTime = time.time()

#elapsed time
insertionElapsedTime = insertionEndTime - insertionStartTime

timeArray.append(insertionElapsedTime)

print("----------------------------------------------------")
print("Insertion Sort took ", insertionElapsedTime*100, " miliseconds")












# Print dataframe of results
sortTypes = ["Bubble Sort", "Merge Sort", "Counting Sort", "Insertion Sort"]
data = {"Sort Type":sortTypes, "Time Taken": timeArray }
df = pandas.DataFrame(data)
print("=========================")
print(df) 
