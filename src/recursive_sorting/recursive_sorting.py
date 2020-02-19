'''
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled
'''

# TO-DO: complete the helpe function below to merge 2 sorted arrays
# def merge_sort(arr):
#   #base case
  if len(arr) == 1:
    return arr 

  #split array and assing them to l1 and l2
  l1 = arr[:len(arr)//2]  
  l2 = arr[len(arr)//2:]
  
  #continue splitting via recursion
  l1 = merge_sort(l1)
  l2 = merge_sort(l2)
  
  return merge(l1, l2)
  
    
def merge( arr_a, arr_b): 
  arr_c = []
  
  while len(arr_a) & len(arr_b) != 0:
    if(arr_a[0] > arr_b[0]):
      arr_c.append(arr_b[0])
      arr_b.pop(arr_b[0])
    else:
      arr_c.append(arr_a[0])
      arr_a.pop(arr_a[0])

  while( len(arr_a) > 0):
    arr_c.append(arr_a[0])
    arr_a.pop(arr_a[0])

  while(len(arr_b) > 0):
    arr_c.append(arr_b[0])
    arr_b.pop(arr_b[0])

  return arr_c
    

def merge_sort(arr):
#   #base case
  if len(arr) == 1:
    return arr 

  #split array and assing them to l1 and l2
  l1 = arr[:len(arr)//2]  
  l2 = arr[len(arr)//2:]
  
  #continue splitting via recursion
  l1 = merge_sort(l1)
  l2 = merge_sort(l2)
  
  return merge(l1, l2)
  
    
def merge( arr_a, arr_b): 
  arr_c = []
  
  while len(arr_a) & len(arr_b) != 0:
    if(arr_a[0] > arr_b[0]):
      arr_c.append(arr_b[0])
      arr_b.pop(arr_b[0])
    else:
      arr_c.append(arr_a[0])
      arr_a.pop(arr_a[0])

  while( len(arr_a) > 0):
    arr_c.append(arr_a[0])
    arr_a.pop(arr_a[0])

  while(len(arr_b) > 0):
    arr_c.append(arr_b[0])
    arr_b.pop(arr_b[0])

  return arr_c
    

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
