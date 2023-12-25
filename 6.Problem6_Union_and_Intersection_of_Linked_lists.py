
#----------------------------------------
#Problem6. Union_and_Intersection_of_Linked_lists.py
#----------------------------------------

## Time and Space complexity


# <br> UNION: 
# <br> Time Complexity:

# <br> finding the union involves traversing both linked lists and adding unique elements to a new linked list or set.
# The time complexity for union is O(m + n), where m and n are the lengths of the two linked lists.

# <br> Space Complexity:

# <br> The space complexity is O(m + n) to store the union.
# If modifying one of the existing linked lists, the space complexity might be O(min(m, n)) if you are using additional data structures to keep track of elements.
# Intersection of Two Linked Lists:
# Time Complexity:


# <br> INTERSECTION:
# <br> Time Complexity:

# <br> In my solution I traverse both linked lists and use dictionary Data sructur eto store elements/keys of first linked lList and then look up elemnets of second Linked list in distionary (hash table).
# Thus, finding the intersection involves traversing both linked lists and identifying common elements.
# The time complexity for intersection is O(m + n)), where m and n are the lengths of the two linked lists.

# <br>Space Complexity:

# <br>Building the Dictionary:

# <br>Space complexity: O(m), where m is the length of the first linked list.
# Each node from the first linked list is stored in the dictionary.

# <br>Result Intersection- Linked List:

# <br>The space complexity for the result linked list is O(min(m, n)) in the worst case.
# The overall space complexity is O(m), dominated by the space required to store the nodes from the first linked list in the dictionary.

# <br>My approach is efficient in terms of time complexity, and using a dictionary for lookups helps achieve O(m + n) time complexity. The space complexity is also reasonable.




#------------------- Implementation --------------------- 
import pandas as pd 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    

def union(llist_1, llist_2):
    
   
    #1. create resulted linked list from the linked list1
    #2.iterate on other linked list and append each element to the resulted linked list
    
    result = llist_1
    #result.append(llist_2.head)
    node = llist_2.head
    while node.next:
        
        result.append(node)
        node = node.next
    result.append(node)
    return result



def intersection(llist_1, llist_2):
    
    
    #1.create dictionary out of Linked list 1 with keys as numbers and values as a counter
    #2. iterate through linked list 2 , if element is in dictinary, then add element to result Liked list and deduct -1 from counter. If counter reachs 0, delet that key from dictionary
    #3. resulted linked list
    
    #1:
    result2 = LinkedList()
    dict_llink1 = {}
    node = llist_1.head
    while node.next:
        if node.value in dict_llink1:
            dict_llink1[node.value] += 1
        else:
            dict_llink1[node.value] = 1
        node = node.next
    #last Node
    if node.value in dict_llink1:
            dict_llink1[node.value] += 1
    else:
        dict_llink1[node.value] = 1
    
    #2:
    node = llist_2.head
    while node.next:
        if node.value in dict_llink1:
            result2.append(node.value)
            dict_llink1[node.value] -=1
            if dict_llink1[node.value] == 0:
                del dict_llink1[node.value]
            
        node = node.next
    if node.value in dict_llink1:
            result2.append(node.value)
            
    
    return result2



## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))


## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))



## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1


linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,7,8,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


## Test Case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,7,8,21,1]
element_2 = [1,7,8,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


# Test Case 3


linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,7,8,21,1,1,1,1,1,1,1,1000,1000,1000,1000,1000]
element_2 = [1,1,1000,1000,1,7,8,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

## Test case4 (corner case):
linked_list_6 = LinkedList()
linked_list_7 = LinkedList()

element_1 = []
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_6.append(i)

for i in element_2:
    linked_list_7.append(i)

print (union(linked_list_6,linked_list_7))
print (intersection(linked_list_6,linked_list_7))


## Corner case 5:

linked_list_8 = LinkedList()
linked_list_9 = LinkedList()

element_1 = [1,1,1,2,2,2,3,3,3]
element_2 = [3,3,1,1,2,2]

for i in element_1:
    linked_list_8.append(i)

for i in element_2:
    linked_list_9.append(i)

print (union(linked_list_8,linked_list_9))
print (intersection(linked_list_8,linked_list_9))


