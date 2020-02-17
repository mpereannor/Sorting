# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)): 
      #loop number one, don't know why we need to do len(arr) - 1 instead of len(arr)
      
        lowest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range( i, len(arr)):
        
          if arr[lowest_index] > arr[j]:
            lowest_index = j

        # TO-DO: swap
        # arr[i] = arr[lowest_index]
        arr[i], arr[lowest_index] = arr[lowest_index], arr[i], 
  
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
  
  

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr