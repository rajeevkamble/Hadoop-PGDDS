# Rajeev Kamble
# PGDDS-2019 
# Assignment #1 


# function to demonstrate Merge sort
def mergeSort(lArray):
    if len(lArray)>1:
        # continually splits a array in half.
        mid = round(len(lArray)/2)

        # formulate both the halves
        lefthalf = lArray[:mid]
        righthalf = lArray[mid:]

        # recursively invoke a merge sort on both halves
        mergeSort(lefthalf)
        mergeSort(righthalf)

        bCompareCnt=0
        lCompareCnt=0
        rCompareCnt=0

        # merging the two smaller sorted lists into a larger sorted list.
        while bCompareCnt < len(lefthalf) and lCompareCnt < len(righthalf):
            if lefthalf[bCompareCnt] < righthalf[lCompareCnt]:
                lArray[rCompareCnt]=lefthalf[bCompareCnt]
                bCompareCnt=bCompareCnt+1
            else:
                lArray[rCompareCnt]=righthalf[lCompareCnt]
                lCompareCnt=lCompareCnt+1
            rCompareCnt=rCompareCnt+1

        while bCompareCnt < len(lefthalf):
            lArray[rCompareCnt]=lefthalf[bCompareCnt]
            bCompareCnt=bCompareCnt+1
            rCompareCnt=rCompareCnt+1

        while lCompareCnt < len(righthalf):
            lArray[rCompareCnt]=righthalf[lCompareCnt]
            lCompareCnt=lCompareCnt+1
            rCompareCnt=rCompareCnt+1

# function to demonstrate Selection sort
def selectionSort(lArray):
   for passQueue in range(len(lArray)-1,0,-1):

       maxIndex=0

        # making only one exchange for every pass through the list
       for currIndex in range(1,passQueue+1):
        # look for the largest value
           if lArray[currIndex]>lArray[maxIndex]:
               maxIndex = currIndex

    # place value in the proper Index
       tempQueue = lArray[passQueue]
       lArray[passQueue] = lArray[maxIndex]
       lArray[maxIndex] = tempQueue    

# function to demonstrate Quick sort
def quickSort(lArray):
    # recursive function for partition and sorting
   quickSortHelper(lArray,0,len(lArray)-1)

def quickSortHelper(lArray,firstIndex,lastIndex):
   if firstIndex<lastIndex:

       splitpoint = getPivotVal(lArray,firstIndex,lastIndex)

       quickSortHelper(lArray,firstIndex,splitpoint-1)
       quickSortHelper(lArray,splitpoint+1,lastIndex)

def getPivotVal(lArray,firstIndex,lastIndex):
   pivotvalue = lArray[firstIndex]

   leftmark = firstIndex+1
   rightmark = lastIndex

   bComplete = False
   while not bComplete:

       while leftmark <= rightmark and lArray[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while lArray[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           bComplete = True
       else:
           tempQueue = lArray[leftmark]
           lArray[leftmark] = lArray[rightmark]
           lArray[rightmark] = tempQueue

   tempQueue = lArray[firstIndex]
   lArray[firstIndex] = lArray[rightmark]
   lArray[rightmark] = tempQueue


   return rightmark

import pandas as pd
import numpy as np
import datetime

# read csv file and get a column in dataframe
echonest_df = pd.read_csv("C:\\Users\\Rajeev\\Documents\\Python Scripts\\Mergesort\\echonest.csv")
echonest_df.drop('Unnamed: 0',inplace=True,axis=1)
echonest_df.drop([0,1,2],inplace=True,axis=0)
echonest_df.reset_index(inplace=True)
echonest_df.drop("index",inplace=True,axis=1)
echonest_df["echonest.248"] = echonest_df["echonest.248"].astype(float)

# dataframe to array
vArray = echonest_df["echonest.248"].to_numpy()
print("Total unsorted items in array:" + str(len(vArray)))

# dedicated copies for each sorting
vArrayMerge = np.copy(vArray)
vArraySelection = np.copy(vArray)
vArrayQuick = np.copy(vArray)

time = datetime.datetime.now()
print(vArrayMerge)
print("Merge Sort Start Time:" + str(datetime.datetime.now()))
mergeSort(vArrayMerge)
print("Merge Sort End Time:" + str(datetime.datetime.now()))
print("Merge Sort Total Time:" + str(datetime.datetime.now() - time))
print(vArrayMerge)

time = datetime.datetime.now()
print("Selection Sort Start Time:" + str(datetime.datetime.now()))
selectionSort(vArraySelection)
print("Selection Sort End Time:" + str(datetime.datetime.now()))
print("Selection Sort Total Time:" + str(datetime.datetime.now() - time))
print(vArraySelection)

time = datetime.datetime.now()
print("Quick Sort Start Time:" + str(datetime.datetime.now()))
quickSort(vArrayQuick)
print("Quick Sort End Time:" + str(datetime.datetime.now()))
print("Quick Sort Total Time:" + str(datetime.datetime.now() - time))
print(vArrayQuick)

# Results view
# Total unsorted items in array:13129
# [262.92974854 325.58108521 356.7557373  ...  89.18032837  12.50396633 302.9463501 ]

# Merge Sort Start Time:2019-06-13 00:50:15.946584
# Merge Sort End Time:2019-06-13 00:50:16.178262
# Merge Sort Total Time:0:00:00.233676
# [ -1.68783438  -1.68783438  -1.68783438 ...  12.50396633  12.50396633 302.9463501 ]

# Selection Sort Start Time:2019-06-13 00:50:16.181193
# Selection Sort End Time:2019-06-13 00:50:48.009491
# Selection Sort Total Time:0:00:31.829291
# [-1.68783438e+00 -1.50766671e+00 -1.50443566e+00 ...  4.42203418e+03  4.70806885e+03  4.79069678e+03]

# Quick Sort Start Time:2019-06-13 00:50:48.012466
# Quick Sort End Time:2019-06-13 00:50:48.192557
# Quick Sort Total Time:0:00:00.181138
# [-1.68783438e+00 -1.50766671e+00 -1.50443566e+00 ...  4.42203418e+03  4.70806885e+03  4.79069678e+03]