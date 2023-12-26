
# #----------------------------------------
# #Problem3.Huffman_codding
# #----------------------------------------
# ## Explanation

# <br>  For Encoding text data I used Data Structure Tree and implemented used Prioroty queue with Linked list of Nodes. Also I used dictionary/hash map for storing unique characters of text and its frequency

# #----------------------- Time and Space complexity -----------------

# <br> Time Complexity:
# <br> #-----------------------

# <br> 1.Building the Huffman Tree (build_huffman_tree):

# <br> Time Complexity:
# Counting Character Frequencies (Building the Dictionary):

# The time complexity for counting the frequency of each character in the input text using a dictionary is O(m), where m is the length of the input text.
# Each character is processed once.

# <br> Building the Linked List from Dictionary Entries:

# Constructing the linked list from the dictionary entries involves creating a node for each unique character and its frequency.
# The time complexity for this step is O(n), where n is the number of unique characters.
# In the worst case, you may need to insert each node into the linked list.
# <br>  => The overall time complexity so far is O(m + n), where m is the length of the input text and n is the number of unique characters.


# <br> 2.Building Huffman Codes (build_huffman_codes):

# The time complexity is O(n), where n is the number of nodes in the Huffman tree.
# Each node is visited exactly once.


# <br> 3.Encoding the Text (huffman_encode):

# The time complexity of encoding the text is O(m), where m is the length of the input text.
# Each character in the input text is replaced with its Huffman code.



# <br> 4. Decoding the Text (huffman_decode):

# The time complexity of decoding the text is O(m), where m is the length of the encoded text.
# We traverse the Huffman tree for each bit in the encoded text.
# *The overall time complexity* is dominated by the building of the Huffman tree, resulting in O(n  + m).

# #-----------------------
# <br> Space Complexity:
# <br> #--------------------

# <br> 1. Building Huffman Tree:

# The space complexity of storing the Huffman tree is O(n), where n is the number of unique characters in the input text.
# This includes the nodes and pointers in the tree structure.
# <br> 2. Huffman Codes:

# The space complexity for storing the Huffman codes is O(n), where n is the number of unique characters.
# Each unique character has an associated Huffman code.

# <br> 3. Encoded Text:

# The space complexity for storing the encoded text is O(m), where m is the length of the input text.
# The encoded text can be longer than the original text in the worst case.
# The overall space complexity is O(n), where n is the number of unique characters, and it is dominated by the space required to store the Huffman tree and codes.







# -------------------- Implementation --------------------------------

import pandas as pd
import sys

## 1. Building Huffman tree and encoding data

class TreeNode:

    def __init__(self, character, frequency):
        self.left = None
        self.right = None
        self.character = character
        self.frequency = frequency
        self.bit = None
        

def assign_bits_to_huffman_tree(root, bit=''):
    """
    Assigns bits (0 for left child, 1 for right child) to each node in the Huffman tree.
    Modifies the 'bit' attribute of each node.

    Args:
    - root: The root of the Huffman tree.
    - bit: The bit assigned to the current node.
    """
    if root is not None:
        root.bit = bit
        assign_bits_to_huffman_tree(root.left, bit + '0')
        assign_bits_to_huffman_tree(root.right, bit + '1')
        
        
# Print the result
def print_huffman_tree(root):
    if root is not None:
        print(f"Node character: {root.character}, Frequency: {root.frequency}, Bit: {root.bit}")
        print_huffman_tree(root.left)
        print_huffman_tree(root.right)

def path_from_node_to_root(root, character):
    if root is None:
        return None

    elif root.character == character:
        return root.bit
           
    
    left_answer = path_from_node_to_root(root.left, character)
    
    if left_answer is not None:
        return left_answer

    right_answer = path_from_node_to_root(root.right, character)

    if right_answer is not None:
         return right_answer
    
    return None


def huffman_encoding(data):
    
    if  data is None or len(data) <= 1:
        return None, None
    
    #1. determine the frequency of each character in the message
    
    data_dict = {}
    for char in data:
        if char not in data_dict:
            data_dict[char] = 1
        else:
            data_dict[char] += 1        
    
    #2.Implement List of Nodes, sort it to make it function as a priority queue
    
    priority_queue = []
    
    for i in range(len(data_dict)):
        least_freq_char = min(data_dict, key=data_dict.get)
        new_node = TreeNode(character=least_freq_char, frequency = data_dict[least_freq_char])
        priority_queue.append(new_node)
        data_dict.pop(least_freq_char)
        

    #3.Pop out two Nodes with least frequency from priority queue
    
    while len(priority_queue) > 1:
        first_node = priority_queue.pop(0)
        second_node = priority_queue.pop(0)
       
       #4. create a new Node as a sum of those two nodes, with left child as a lower value, right child as a higher value.
  
        new_sum_node = TreeNode(frequency = (first_node.frequency + second_node.frequency),character = None)
        new_sum_node.left = first_node
        new_sum_node.right = second_node   
    
    #5. put this new Node back in priority queue  and sort updated priority queue
        priority_queue.append(new_sum_node)
       
        #sort updated prioroty queue
        priority_queue = sorted(priority_queue, key = lambda x: (x.frequency))
        
        
       
    #6. define the root of a hofman tree
    if priority_queue != []:
        huffman_tree_root = priority_queue[0]
    else:
        huffman_tree_root = None
    
    #7. For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child.
    
    assign_bits_to_huffman_tree(root = huffman_tree_root, bit = '')
    
    
    #encoding data:
    encoded_data = ''
    #print(data)
    for char in data:
        encoded_char = path_from_node_to_root(root = huffman_tree_root , character = char)
        encoded_char = ''.join(map(str, encoded_char))
        encoded_data = str(encoded_data) + str(encoded_char)


    return  encoded_data, huffman_tree_root


## 2. Implementation of Decoding

def huffman_decoding(data,tree):
    
    #1.Declare a blank decoded string
    decoded_data = ''
    tree_root = tree
    #2.Pick a bit from the encoded data, traversing from left to right.
    #3.Start traversing the Huffman tree from the root.
    #4.If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.

    
    if  data is None or len(data) <= 1:
        return None
    
    for digit in data:
        if digit == '0' and tree_root.left is not None:
            tree_root = tree_root.left

        elif digit == '1' and tree.right is not None:
            tree_root = tree_root.right

    #5.If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.    
        if (tree_root.left is None and tree_root.right is None):
            decoded_data = decoded_data + tree_root.character
            tree_root = tree
            
    
    
    return decoded_data

#Test case1 :

data = 'q'

encoded_data,huffman_tree = huffman_encoding(data)
print('encoded_data=',encoded_data) #returns None since only 1 chaacter, no encoding needed

decoded_data = huffman_decoding(data = encoded_data, tree = huffman_tree)

print('decoded_data=',decoded_data) #returns None since only 1 chaacter, no encoding needed

#----- Lesson testing cases -----
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    print(tree.left.bit)

    decoded_data = huffman_decoding(encoded_data, tree=tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

#----------------------
## Test Case 2
if __name__ == "__main__":
    codes = {}

    my_test2 = "I would like to be good in Software Engeneering to become better as Data Scientist"

    print ("The size of the data is: {}\n".format(sys.getsizeof(my_test2)))
    print ("The content of the data is: {}\n".format(my_test2))

    encoded_data, tree = huffman_encoding(my_test2)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    

    decoded_data = huffman_decoding(encoded_data, tree=tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))


#---------------------
## Test Case 3
if __name__ == "__main__":
    codes = {}

    my_test3 = """its a Bird, it’s a plane, it’s a ball of flames Bracing myself for the fall for the great escape
    Woah landing straight into my hands yeah
I just had ask all about it
I decided I’m keeping it on me
For the time I’ll be in the dark lonely
And why would I let you go
I don’t know
know you know something that I don’t

show me, show me everything that you got, God
I opened the door and I fell into ya..

I keep on swimming in space
I can’t stop floating away
Now I keep on swimming in space
I keep on floating away

Now it’s a monster. a wave, onto bigger things
but come as they may noticing they keep calling me
Woah swimming right into to my hands yeah
I just had to ask all about it
I decided to keep em' all on me
For the time I be in the dark lonely
And why would I leave you lost,
I don’t know
Finally I’m not the only one

show me, show me everything that you got, God
I opened the door and I fell into ya

I keep on swimming in space
I can’t stop floating away
Now I keep on swimming in space
I keep on floating away

 Woah landing straight into my hands yeah
I just had ask all about it
I decided I’m keeping it on me
For the time I’ll be in the dark lonely
And why would I let you go
I don’t know
know you know something that I don’t

show me, show me everything that you got, God
I opened the door and I fell into ya..

I keep on swimming in space
I can’t stop floating away
Now I keep on swimming in space
I keep on floating away

Now it’s a monster. a wave, onto bigger things
but come as they may noticing they keep calling me
Woah swimming right into to my hands yeah
I just had to ask all about it
I decided to keep em' all on me
For the time I be in the dark lonely
And why would I leave you lost,
I don’t know
Finally I’m not the only one

show me, show me everything that you got, God
I opened the door and I fell into ya

I keep on swimming in space
I can’t stop floating away
Now I keep on swimming in space
I keep on floating away
"""

    print ("The size of the data is: {}\n".format(sys.getsizeof(my_test3)))
    print ("The content of the data is: {}\n".format(my_test3))

    encoded_data, tree = huffman_encoding(my_test3)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    

    decoded_data = huffman_decoding(encoded_data, tree=tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))



## Test case4:

if __name__ == "__main__":
    codes = {}

    my_test4 = 'aaaaaaaaaaaaaa'

#     print ("The size of the data is: {}\n".format(sys.getsizeof(my_test4)))
#     print ("The content of the data is: {}\n".format(my_test2))

    encoded_data, tree = huffman_encoding(my_test4)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))
    

    decoded_data = huffman_decoding(encoded_data, tree=tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the decoded data is: {}\n".format(decoded_data))


print(' encoded_data=', encoded_data)
print(' decoded_data=', decoded_data)



#-------

## Test case5:

if __name__ == "__main__":
    codes = {}

    my_test5 = 'a'

#     print ("The size of the data is: {}\n".format(sys.getsizeof(my_test4)))
#     print ("The content of the data is: {}\n".format(my_test2))

    encoded_data, tree = huffman_encoding(my_test5)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))
    

    decoded_data = huffman_decoding(encoded_data, tree=tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the decoded data is: {}\n".format(decoded_data))


print(' encoded_data=', encoded_data)
print(' decoded_data=', decoded_data)


#-------------

## Test case6:

if __name__ == "__main__":
    codes = {}

    my_test6 = ''

#     print ("The size of the data is: {}\n".format(sys.getsizeof(my_test4)))
#     print ("The content of the data is: {}\n".format(my_test2))

    encoded_data, tree = huffman_encoding(my_test6)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))
    

    decoded_data = huffman_decoding(encoded_data, tree=tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the decoded data is: {}\n".format(decoded_data))


print(' encoded_data=', encoded_data)
print(' decoded_data=', decoded_data)

