import pandas as pd 
import os


## --------------------  OS Module Exploration Code ------------------------
### Locally save and call this file ex.py ##

## Code to demonstrate the use of some of the OS modules in python

import os

## Let us print the files in the directory in which you are running this script
print (os.listdir("."))

## Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

## Does the file end with .py?
print ("./ex.py".endswith(".py"))

## Does the file end with .py?
print ("./ex.ipynb".endswith(".ipynb"))

for File in os.listdir("."):
    if os.path.isfile(File):
        print(File)
    else:
        print("false")
        
        
for File in os.listdir("."):
    if File.endswith(".ipynb"):
        print("true")
    else:
        print("false")
        
        
        
for File in os.listdir("."):
    if os.path.isdir(File):
        print("true")
    else:
        print("false")
        
        
for File in os.listdir("."):
    if os.path.isfile(File):
        print(os.path.dirname(os.path.realpath(File)))
    else:
        print("false")

os.path.join("/Algorytms_Datastructures_Nanodegree/Project2_datastructures/Problem1_LRU_Cache","test")


# Path 
test_path = '/Users/katerynaisaieva/Desktop/Nanodegree_Projects/Algorytms_Datastructures_Nanodegree/Project2_datastructures/Problem2_File_Recursion/testdir/'
  
# Get the directory name   
# from the specified path 

#dirname = os.path.dirname(test_path) 

for File in os.listdir(test_path):
    print(File)
    if  os.path.isdir(os.path.join(test_path,File)):
        print('it is directory')
  
# Print the directory name   
# print(dirname) 

#-----------------------------------------------------------------------------

#----------------------------------------
#Problem2.File_Recursion - Explanation
#----------------------------------------

# #- For implementing efficient search function I used recursion. It goes deep into all directories one by one in a top down manner and:
# <br> 1. print out all paths of all searched files
# <br> 2. and then gows into each directory if it exists and recursivally does the same steps 1. and 2. until all is checked

# ### Time and Space Efficiency:

# #### Key answer: Linear Time Complexity and Constant Space efficiency

# 1. TIme efficiency. Traversal Time: The implemented search function efficiently traverses the directory tree in a top-down manner. It explores each directory and its subdirectories in a depth-first fashion.
# <br> => Linear Time Complexity: The time complexity is generally O(n), where n is the total number of files and directories in the tree. It visits each file and directory once.


# 2. Space efficiency. Memory Usage:  The implemented search functionis memory-efficient as it doesn't load the entire directory tree into memory at once. Instead, it returns a generator object that yields a tuple for each directory it visits. The tuple contains the current directory, a list of its subdirectories, and a list of its files.
# <br> => Constant Space Overhead: The memory used by  implemented search function is proportional to the depth of the directory tree, not the total number of files. The generator ensures that only a small portion of the directory tree is loaded into memory at any given time.

# <br> In summary,  implemented search function is generally considered both time and space-efficient. It is well-suited for efficiently processing directory trees of various sizes, and its memory usage is optimized by yielding results incrementally. 

# <br> PS. However, the efficiency depends on the underlying file system and the size of the directory tree being traversed.




#---------------------------------- Implementation ----------------------------

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    path = path
    suffix = suffix
    
    # check if path exists
    if not (os.path.exists(path) and os.path.isdir(path)):
        return print("Directory does not exist")


    
    #recurtion
    for File in os.listdir(path):
        if  File.endswith("."+suffix)== True: 
            print(os.path.join(path))
        
        if  os.path.isdir(os.path.join(path,File)): 
            sub_path = os.path.join(path,File)
            find_files(suffix='c',path=sub_path)
    
    
    return None


## Test Case 1

find_files(suffix = 'c', path= '/Users/katerynaisaieva/Desktop/Nanodegree_Projects/Algorytms_Datastructures_Nanodegree/Project2_datastructures/Problem2_File_Recursion/testdir/')

## Test Case 2

find_files(suffix = '', path= '/Users/katerynaisaieva/Desktop/Nanodegree_Projects/Algorytms_Datastructures_Nanodegree/Project2_datastructures/Problem2_File_Recursion/testdir/')

## Test Case 3 (Empty)

find_files(suffix = 'c', path= '/Users/katerynaisaieva/Desktop/Nanodegree_Projects/Algorytms_Datastructures_Nanodegree/Project2_datastructures/Problem2_File_Recursion/testdir/subdir2')

# Test case 4 (sending invalid diretory path):

path1 = '/Users/katerynaisaieva/Desktop/Nanodegree_Projects/Algorytms_Datastructures_Nanodegree/Project2_datastructures/Problem2_File_Recursion/testdir/subdir2'
print(find_files('.h', path1 + '/abc'))
