import numpy as np

# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def cmp(a, b):
    return 1 if a > b else 0 if a == b else -1

def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")




# must be in-place sort
def merge_sort(arr,cmp):
    merge(arr, 0, len(arr), cmp)

def merge(arr, l, r, cmp):
    if r - l > 1:
        m = int((l + r)/2)
        merge(arr, l, m, cmp)
        merge(arr, m, r, cmp)
        sort(arr, l, m, r, cmp)

def sort(arr, l, m, r, cmp):
    L = arr[l:m]
    R = arr[m:r]
    ix1 = 0
    ix2 = 0

    for i in range(l, r):
        if ix1 < len(L) and (ix2 >= len(R) or (cmp(L[ix1],R[ix2]) <= 0)):
            arr[i] = L[ix1]
            ix1 += 1
        else:
            arr[i] = R[ix2]
            ix2 += 1 

# must be in-place sort
def quick_sort(arr, cmp):
  if len(arr) <= 1: return arr
  pivot = arr[np.random.randint(len(arr))]
  arr_large, arr_small, arr_equal = [], [], []
  for e in arr:
    #if e > pivot:
    if cmp(e, pivot) == 1:
      arr_large.append(e)
    #elif e < pivot:
    elif cmp(e, pivot) == -1:
      arr_small.append(e)
    else:
      arr_equal.append(e)
  arr_small = quick_sort(arr_small, cmp)
  arr_large = quick_sort(arr_large, cmp)
  arr = arr_small + arr_equal + arr_large
  return arr