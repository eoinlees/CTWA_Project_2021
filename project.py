# Project 2021 
# Initial set up. adding blank files
from random import randint
import time
import pandas


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

# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

# Quick Sort
# Source: https://www.geeksforgeeks.org/python-program-for-quicksort/

def partition(arr, low, high):
	i = (low-1)		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)



# Main Method
timeArray = []
def runTest(numberOfTests, inputSize):
    
    
    #array = randomArray(inputSize)
    
    
    
    # Bubble Sort
    # ****************************************************************************************************************************************************** 
    # NOT SORTING NUMBERS
    bubbleAverageTime = []
    
    for i in range(numberOfTests):
        array = randomArray(inputSize)
        print(array)
        bubbleStartTime = time.time() #start Timer
        print("*"*12)
        print(bubbleSort(array))
        bubbleEndTime = time.time() # End timer
        bubbleElapsedTime = bubbleEndTime - bubbleStartTime #elapsed time
        bubbleAverageTime.append(bubbleElapsedTime)
    
    print("----------------------------------------------------")
    print("Bubble Sort Times: ",bubbleAverageTime)
    
    bubbleElapsedTimeAverage = sum(bubbleAverageTime)/len(bubbleAverageTime)
    timeArray.append(bubbleElapsedTimeAverage)
    
    print("----------------------------------------------------")
    print("Bubble Sort took ", bubbleElapsedTime*1000, " miliseconds")
    print("")
    
    
    
    # Merge Sort
    #arr = randomArray(100)
    # ****************************************************************************************************************************************************** 
    # NOT SORTING NUMBERS
    mergeAverageTime = []
    for i in range(numberOfTests):
        array = randomArray(inputSize)
        mergeStartTime = time.time() #start Timer
        print(mergeSort(array))
        mergeEndTime = time.time() # End timer
        mergeElapsedTime = mergeEndTime - mergeStartTime #elapsed time
        mergeAverageTime.append(mergeElapsedTime)
        
    print("----------------------------------------------------")
    print("Merge Sort Times: ", mergeAverageTime)
    mergeElapsedTimeAverage = sum(mergeAverageTime)/len(mergeAverageTime)
    timeArray.append(mergeElapsedTimeAverage)
    
    print("----------------------------------------------------")
    print("Merge Sort took ", mergeElapsedTimeAverage*1000, " miliseconds")
    print("")
    
    
    # Counting Sort    
    countAverageTime = []
    for i in range(numberOfTests):
        array = randomArray(inputSize)
        countingStartTime = time.time()
        print(count_sort(array))
        countingEndTime = time.time()
        countingElapsedTime = countingEndTime - countingStartTime #elapsed time
        countAverageTime.append(countingElapsedTime)
    
    print("Counting Sort Times: ",countAverageTime)
    countingElapsedTimeAverage = sum(countAverageTime)/len(countAverageTime)
    timeArray.append(countingElapsedTimeAverage)
    
    print("-"*52)
    print("Counting Sort took on average ", countingElapsedTimeAverage*1000, " miliseconds")
    print("")
    
    
    # Insertion Sort - TO BE TESTED AND FIGURED OUT 
    # ******************************************************************************************************************************************************
    array = randomArray(inputSize)
    insertionStartTime = time.time() #start Timer
    insertionSort(array)# Call function
    insertionEndTime = time.time() # End Timer
    insertionElapsedTime = insertionEndTime - insertionStartTime #elapsed time
    timeArray.append(insertionElapsedTime) # Append to array
    print("----------------------------------------------------")
    print("Insertion Sort took ", insertionElapsedTime*1000, " miliseconds")
    print("")
    
    
    # Quick Sort
    # ****************************************************************************************************************************************************** 
    # NOT SORTING NUMBERS
    quickAverageTime = []
    for i in range(numberOfTests):
        array = randomArray(inputSize)
        #print(array) # Test print
        quickStartTime = time.time() #start Timer
        length = len(array)
        print(quickSort(array, 0, length-1)) # Test printing array
        quickEndTime = time.time() # End Timer
        quickElapsedTime = quickEndTime - quickStartTime #elapsed time
        quickAverageTime.append(quickElapsedTime) # Append to array
        
    print("Quick Sort Times: ", quickAverageTime)
    quickElapsedTimeAverage = sum(quickAverageTime)/len(quickAverageTime)
    timeArray.append(quickElapsedTimeAverage)    
    
    print("----------------------------------------------------")
    print("Quick Sort took ", quickElapsedTimeAverage*1000, " miliseconds")
    print("")

    # ******************************************************************************************************************************************************



if __name__ == '__main__':
    runTest(10, 100)
    print("")
    print("")
    print("Time Array TEst -----------------------------")
    print(timeArray)
    print("Time Array TEst -----------------------------")
    print("")
    print("")
    # Print dataframe of results
    headings = ["Sort type", "Time"]
    sortTypes = ["Bubble Sort", "Merge Sort", "Counting Sort", "Insertion Sort", "Qucik Sort"]
    
    data = {"Sort Type":sortTypes, "Time Taken": timeArray}
    df = pandas.DataFrame(data)
    print("="*52)
    print(df) 
    print("="*52)
