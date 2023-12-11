import pandas as pd 
import time

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.size = capacity
        self.usage = {}                


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.         
        if key in self.cache:
            return self.cache[key]
        
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache:
            pass
        elif len(self.cache) < self.size:
            self.cache[key] = value
            self.usage[key] = time.time()
        else:
            #remove the oldest item
            oldest_key = min(self.usage, key=self.usage.get)
            self.cache.pop(oldest_key)
            self.usage.pop(oldest_key)
            self.cache[key] = value
            self.usage[key] = time.time()
               
 
#Testing
our_cache = LRU_Cache(5)

## Test Case0 with empty one

print(our_cache.get(1)) #returns -1 since its empty

#proposed text case
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))    # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))  # returns 3


#My own 3 Test cases

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

our_cache.set(21, 21)
print(our_cache.get(6)) # returns 6

## Test Case 2
our_cache.set(11, 11) 
print(our_cache.get(21)) # returns 21

## Test Case 3
our_cache.set(11, 11) 
print(our_cache.get(2)) # returns -1


# Explanaition
#-  For implementing data structure Least Recently Used (LRU) Cashe I designed a class where object is dictinary(hash map) and with 2 functions which returns and insert item with O(1) time efficiency, since look up in Hash map is constant time O(1).

#- Space efficiency in current example with the size of LRU as 5 is constant. With size of LRU Cache growing, I expeft it to be space efficiency = n
