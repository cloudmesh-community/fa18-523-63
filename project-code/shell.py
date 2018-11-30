# The project performer is not the author of the below code
# - Author: w3resrouce
# - URL: https://www.w3resource.com/python-exercises/data-
#   structures-and-algorithms/python-search-and-sorting-exercise-7.php
# - Accessed (11/2018)
# This code was adapted for the project needs

def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap

        nlist[position]=current_value
        
def shell_sort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)

      sublistcount = sublistcount // 2
      return alist