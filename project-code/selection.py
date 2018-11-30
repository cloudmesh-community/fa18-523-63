# The project performer is not the author of the below code
# - Author: Interactive Python
# - URL: http://interactivepython.org/runestone/static/
#        pythonds/SortSearch/TheSelectionSort.html
# - Accessed (11/2018)
# This code was adapted for the project needs

def selection_sort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
   return alist