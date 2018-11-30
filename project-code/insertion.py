# The project performer is not the author of the below code
# - Author: Interactive Python
# - URL: http://interactivepython.org/courselib/static/
#        pythonds/SortSearch/TheInsertionSort.html
# - Accessed (11/2018)
# This code was adapted for the project needs

def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
     return alist