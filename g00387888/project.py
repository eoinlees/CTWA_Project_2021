# Project 2021 
# Initial set up. adding blank files
from random import randint
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Random Array
# Creates a random array from the discreen uniform distribution
def randomArray(n):
    array = []
    for i in range (0,n,1): # low, high, size
        # source: https://docs.python.org/3/library/random.html
        array.append(randint(0,100))
    return array

#Print 100 numbers array # Test function 
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
    
    for i in range(len(arr)):
        return("%d" %arr[i])

# Merge Sort
# Source: https://www.geeksforgeeks.org/merge-sort/

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

# Code to print the list for testing sort
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Counting Sort
# Source: https://www.geeksforgeeks.org/counting-sort/

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

# Insertion Sort
# Source: https://www.geeksforgeeks.org/insertion-sort/

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

# Partition function
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

# Global variables
globalTimeArray = [] # Initate blank time array for results

# Run Method - to run all sorting algorithms on function call 

def runTest(numberOfTests, inputSize):
    timeArray = [] # Local time array for adding to global list on iteration
    # Bubble Sort
    bubbleAverageTime = [] # Local bubble list for adding to time array on iteration
    
    for i in range(numberOfTests):
        array = randomArray(inputSize)
        #print("Unsorted Array for ", inputSize, "input: ", array) # Print statements for testing
        bubbleStartTime = time.time() #start Timer
        #print("*"*12)
        bubbleSort(array)
        #print("Sorted Bubble array: ", array)
        #print("*"*12)
        bubbleEndTime = time.time() # End timer
        bubbleElapsedTime = (bubbleEndTime - bubbleStartTime)*1000 #elapsed time - in milliseconds
        bubbleElapsedTime = round(bubbleElapsedTime, 2)
        bubbleAverageTime.append(bubbleElapsedTime)
    
    #print("----------------------------------------------------")
    #print("Bubble Sort Times: ",bubbleAverageTime)
    
    bubbleElapsedTimeAverage = sum(bubbleAverageTime)/len(bubbleAverageTime) # Calculation average time taken
    timeArray.append(bubbleElapsedTimeAverage) # apending average time to local time array
    
    #print("----------------------------------------------------")
    #print("Bubble Sort took ", bubbleElapsedTime, " miliseconds")
    #print("")
    
    # Merge Sort
    mergeAverageTime = [] # Local merge list for adding to time array on iteration
    
    for i in range(numberOfTests):
        array = randomArray(inputSize)
        #print("The unsorted array for ", inputSize, "is: ", array) #Test print
        mergeStartTime = time.time() #start Timer
        mergeSort(array)
        #print("The Merge sorted array for ", inputSize, "is: ", array)
        mergeEndTime = time.time() # End timer
        mergeElapsedTime = (mergeEndTime - mergeStartTime)*1000 #elapsed time - in milliseconds
        mergeElapsedTime = round(mergeElapsedTime, 2)
        mergeAverageTime.append(mergeElapsedTime)
        
    #print("----------------------------------------------------")
    #print("Merge Sort Times: ", mergeAverageTime)
    mergeElapsedTimeAverage = sum(mergeAverageTime)/len(mergeAverageTime) # Calculation average time taken
    timeArray.append(mergeElapsedTimeAverage) # apending average time to local time array
    
    #print("----------------------------------------------------")
    #print("Merge Sort took on Average of ",numberOfTests," tests: ", mergeElapsedTimeAverage, " miliseconds")
    #print("")
    
    
    # Counting Sort    
    countAverageTime = [] # Local count array for adding to time array on iteration
    
    for i in range(numberOfTests):
        array = randomArray(inputSize)
        #print("The unsorted array for ", inputSize, "is: ", array) #Test print
        countingStartTime = time.time()
        count_sort(array)
        #print("The counting sorted array for ", inputSize, "is: ", array)
        countingEndTime = time.time()
        countingElapsedTime = (countingEndTime - countingStartTime)*1000 #elapsed time - in milliseconds
        countingElapsedTime = round(countingElapsedTime, 2)
        countAverageTime.append(countingElapsedTime) 
    
    #print("Counting Sort Times: ",countAverageTime)
    countingElapsedTimeAverage = sum(countAverageTime)/len(countAverageTime) # Calculation average time taken
    timeArray.append(countingElapsedTimeAverage) # apending average time to local time array
    
    #print("-"*52)
    #print("Counting Sort took on average ", countingElapsedTimeAverage, " miliseconds")
    #print("")
    
    
    # Insertion Sort 
    insertionAverageTime = [] # Local insertion array for adding to time array on iteration
    
    for i in range(numberOfTests):
        array = randomArray(inputSize)
        #print("The unsorted array for ", inputSize, "is: ", array) #Test print
        insertionStartTime = time.time() #start Timer
        insertionSort(array)# Call function
        #print("The Insertion sorted array for ", inputSize, "is: ", array)
        insertionEndTime = time.time() # End Timer
        insertionElapsedTime = (insertionEndTime - insertionStartTime)*1000 #elapsed time - in milliseconds
        insertionElapsedTime = round(insertionElapsedTime, 2)
        insertionAverageTime.append(insertionElapsedTime) # Append to array
    
    #print("Insertion Sort Times: ", insertionAverageTime)
    insertionElapsedTimeAverage = sum(insertionAverageTime)/len(insertionAverageTime) # Calculation average time taken
    timeArray.append(insertionElapsedTimeAverage)    # apending average time to local time array
        
    #print("----------------------------------------------------")
    #print("Insertion Sort took ", insertionElapsedTime, " miliseconds")
    #print("")
    
    
    # Quick Sort
    quickAverageTime = [] # Local quick array for adding to time array on iteration
    
    for i in range(numberOfTests):
        array = randomArray(inputSize)
        #print("The unsorted array for ", inputSize, "is: ", array) #Test print
        quickStartTime = time.time() #start Timer
        length = len(array)
        quickSort(array, 0, length-1) # Test printing array
        #print("The Quick sorted array for ", inputSize, "is: ", array)
        quickEndTime = time.time() # End Timer
        quickElapsedTime = (quickEndTime - quickStartTime)*1000 #elapsed time - in milliseconds
        quickElapsedTime = round(quickElapsedTime, 2) # tidy up result
        quickAverageTime.append(quickElapsedTime) # Append to array
        
    #print("Quick Sort Times: ", quickAverageTime)
    quickElapsedTimeAverage = sum(quickAverageTime)/len(quickAverageTime) # Calculation average time taken
    timeArray.append(quickElapsedTimeAverage)    # apending average time to local time array
    
    #print("----------------------------------------------------")
    #print("Quick Sort took ", quickElapsedTimeAverage, " miliseconds")
    #print("")

    globalTimeArray.append(timeArray) # Apend all average values from the n input to global list before next iteration



# Main method that runs when program is executed in console.
if __name__ == '__main__':
    totalStartTime = time.time() # timer to print length algorithm takes to run
    
    # Use this code to test code functionality. It should take less than 4 seconds to run. 
    size = [100, 250, 500, 750, 1000] # To test functionality - use for review of code
    
    # This variable relates to the results published in the report and the table and graph associated. 
    #size = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000] # Full test results - Warning, takes 10 mins to execute
    
    # iterate 10 times for each value. 
    for i in size:
        runTest(10, i) # run each algorithm 10 times 
    

    #print("Time Array-----------------------------")# Test print global array
    #round(globalTimeArray, 3) #[i * 1000 for i in globalTimeArray]
    #print("Time Array-----------------------------")

    
    #set dataframe of results
    sortTypes = ["Bubble Sort", "Merge Sort", "Counting Sort", "Insertion Sort", "Qucik Sort"]
    df =  pd.DataFrame(data=globalTimeArray, index=size, columns=sortTypes)
    
    #Print dataframe
    print("")
    print("")
    print("="*72)
    print(" "*3, "Average time taken to run each sorting algorithm in milliseconds")
    print("="*72)
    print(df) 
    print("="*72)
    
    
    totalEndTime = time.time()
    
    # Print time taked to execute program
    totalTimeElapsed = totalEndTime - totalStartTime
    print("")
    print("Program took ", round(totalTimeElapsed, 3), " seconds to run")
    
    
    # Testing functions
    
    #Save data in csv to plot graphs in seperate program quicker
    #df.to_csv('sortingDataframe.csv')
    
    
    # Plot data    
    plot = sns.lineplot(data=df,markers=True,dashes=False) # plot using seaborn
    plot.set(xlabel='Array Size', ylabel='Time taken (milliseconds)') # label axis
    #plt.yscale("log") # Uncomment to graph log scale results for larger number of inputs

    plt.show() # Show plot
