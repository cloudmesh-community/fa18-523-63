# This code is written by the project author
# This is the driver code for the project

import random
from classdef import Testing_List      
        
def main():
    random.seed(1)
    val_dict = {"one_hundred_rns" : Testing_List("test",[random.random()for i in range(100)])} 
    val_dict.update({"one_thousand_rns" : Testing_List("test",[random.random()for i in range(1000)])})
    val_dict.update({"ten_thousand_rns" : Testing_List("test",[random.random()for i in range(10000)])})
    val_dict.update({"one_hun_thou_rns" : Testing_List("test",[random.random()for i in range(100000)])})
    
    
    
if __name__ == "__main__":
    main()
