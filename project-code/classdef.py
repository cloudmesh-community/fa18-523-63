# This code is written by the project author
# This defines the class which is called upon
# by main.py


from timeit import default_timer as timer
from bubble import bubble_sort
from selection import selection_sort
from merge import merge_sort
#from squareroot import square_root_sort
from shell import shell_sort
from insertion import insertion_sort
from strand import strand_sort
from pysort import python_sort
from heap import heap_sort

class Testing_List:
    def __init__(self,name,listing):
        # Initilization steps
        self.name = name
        listing_copy = listing
        listing_copy2 = listing
        self.listing = listing_copy
        

        ##################################################
        # For each algorithm, the accuracy, time, and list
        # will be tracked using the methods shown below
        ##################################################

        # Python sort will be used as the master sort
        listing_copy_py = listing_copy
        start = timer()
        self.python_sorted_list = python_sort(listing_copy_py)
        end = timer()
        self.python_sorted_time = end-start
        # Bubble Sort will be tested against python sort
        listing_copy_bu = listing_copy
        start = timer()
        self.bubble_sorted_list = bubble_sort(listing_copy_bu)
        end = timer()
        self.bubble_sort_accurate = False
        if self.bubble_sorted_list == self.python_sorted_list:
            self.bubble_sort_accurate = True
        self.bubble_sort_time = end-start
        # Selection sort will be tested against python sort
        listing_copy_sel = listing_copy
        start = timer()
        self.selection_sorted_list = selection_sort(listing_copy_sel)
        end = timer()
        self.selection_sort_accurate = False
        if self.selection_sorted_list == self.python_sorted_list:
            self.selection_sort_accurate = True
        self.selection_sort_time = end-start
        # Merge sort will be tested against python sort
        listing_copy_mer = listing_copy
        start = timer()
        self.merge_sorted_list = merge_sort(listing_copy_mer)
        end = timer()
        self.merge_sort_accurate = False
        if self.merge_sorted_list == self.python_sorted_list:
            self.merge_sort_accurate == True
        self.merge_sort_time = end-start
        #Shell root sort will be tested against python sort
        listing_copy_she = listing_copy
        start = timer()
        self.shell_sorted_list = shell_sort(listing_copy_she)
        end = timer()
        self.shell_accurate = False
        if self.shell_sorted_list == self.python_sorted_list:
            self.shell_accurate = True
        self.shell_time = end-start
        #Insertion sort will be tested against python sort
        listing_copy_ins = listing_copy
        start = timer()
        self.insertion_sorted_list = insertion_sort(listing_copy_ins)
        end = timer()
        self.insertion_accurate = False
        if self.insertion_sorted_list == self.python_sorted_list:
            self.insertion_accurate = True
        self.insertion_time = end-start
        
        
        # Heap sort will be tested against python sort
        listing_copy_hea = listing_copy
        start = timer()
        self.heap_sorted_list = heap_sort(listing_copy_hea)
        end = timer()
        self.heap_accurate = False
        if self.heap_sorted_list == self.python_sorted_list:
            self.heap_accurate = True
        self.heap_time = end-start
        
        #Strand sort will be tested against python sort
        listing_copy_strand = listing_copy2
        
        start = timer()
        
        self.strand_sorted_list = strand_sort(listing_copy_strand)
        end = timer()
        self.strand_accurate = False
        if self.strand_sorted_list == self.python_sorted_list:
            self.strand_root_accurate = True
        self.strand_time = end-start

