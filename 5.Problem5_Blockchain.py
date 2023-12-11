import pandas as pd
import time 

## Calculate hash function for a dictionary of data
import hashlib

def hash_dictionary(dict_data, hash_algorithm='sha256'):
    hashed_dict = {}

    for key, value in dict_data.items():
        # Convert the value to a bytes-like object (assumes value is a string)
        value_bytes = str(value).encode('utf-8')

        # Choose the hash algorithm (default is SHA-256)
        hash_func = hashlib.new(hash_algorithm)

        # Update the hash with the value bytes
        hash_func.update(value_bytes)

        # Get the hexadecimal representation of the hash
        hashed_value = hash_func.hexdigest()

        # Store the hashed value in the new dictionary
        hashed_dict[key] = hashed_value
        

    return list(hashed_dict.values())[0]

# Example usage:
dict_data = {'key1': 'abc', 'key2': 'def', 'key3': 'abcde'}
hashed_result = hash_dictionary(dict_data)

#print(f"Original Dictionary: {dict_data}")
print(f"Hashed Dictionary: {hashed_result}")

sha_data = {'data' : ['EUR', 100, 'sent','Natalia']}
hash_dictionary(dict_data = sha_data)

# -------------- Ploblem5 Implementation -------------------

## Blockchain implementation

class Block:
        
    def __init__(self,  data, previous_hash = None):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
        
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') +
                  
                   str(self.previous_hash).encode('utf-8')) 
        
        return sha.hexdigest()
    
    def __str__(self):
        return str(self.data)

    
    


class Blockchain():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """ Append a value as a head, which will be a tail as well """    
        if self.head is None:
            self.head = Block(data)
            self.tail = self.head

        else:
            """ Append a value to the tail """   
            self.tail.next = Block(data)
            self.tail = self.tail.next
        
        return self.head
    
    
#------------------Visualization ----------------------
import matplotlib.pyplot as plt
import networkx as nx
import math

def visualize_linked_list_horizontal(head):
        G = nx.DiGraph()

        current_node = head
        pos = {}
        x_position = 0

        while current_node:
            G.add_node(current_node.data)
            pos[current_node.data] = (x_position, 0)
            x_position += 100  # Move right for the next node

            if current_node.next:
                G.add_edge(current_node.data, current_node.next.data)

            current_node = current_node.next

        nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", arrows=True)
        plt.show()
        

def visualize_linked_list_vertical(head):
    G = nx.DiGraph()

    current_node = head
    num_nodes = 0

    while current_node:
        G.add_node(current_node.data)
        num_nodes += 1
        current_node = current_node.next

    positions = {}

    for i, node in enumerate(G.nodes):
        angle = (i / num_nodes) * 2 * math.pi
        x = 0  # Center the nodes along the y-axis
        y = -math.cos(angle) - 0.5 * i  # Adjust the y-coordinate to prevent overlap
        positions[node] = (x, y)

    # Draw nodes
    nx.draw(G, positions, with_labels=False, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", arrows=True)

    # Draw node labels to the right
    for node, (x, y) in positions.items():
        plt.text(x + 0.1, y, node, fontsize=8, ha='left', va='center')

    plt.gca().set_aspect('equal', adjustable='box')  # Ensure equal aspect ratio
    plt.axis('off')  # Turn off the axis
    plt.show()
    
#    ---------------------------------------------
### Blockchain Test Case 1:
Transactions = Blockchain()
#data: [currency_name,amount,'sent'/'received', reciever/sender name]
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)

#adding transactions to Blockchain "Transactions"
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)


current_block = Transactions.head
while current_block != None:
    print(current_block.data)
    current_block = current_block.next
    
# Visualizing Blockchain    
visualize_linked_list_vertical(Transactions.head)

#----------------------------
## Blockchain Test Case 2 (long entry):

Transactions = Blockchain()
#data: [currency_name,amount,'sent'/'received', reciever/sender name]
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)
Kate = Block( data = ['EUR', 100, 'sent','Natalia'], previous_hash = None)
Denis = Block( data  = ['AUS', 200, 'sent','Vladimir'], previous_hash = Kate.hash)
Natalia = Block( data  = ['UKR_HRV', 2999, 'received','Kate'], previous_hash = Denis.hash)
Vladimir = Block( data = ['RUS', 1000, 'received','Denis'], previous_hash = Natalia.hash)


#adding transactions to Blockchain "Transactions"
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)
Transactions.append(Kate)
Transactions.append(Denis )
Transactions.append(Natalia)
Transactions.append(Vladimir)



current_block = Transactions.head
while current_block != None:
    print(current_block.data)
    current_block = current_block.next
    
    
#------------------------------    
## Blockchain Test Case 3 (empty case):

Transactions = Blockchain()
#data: [currency_name,amount,'sent'/'received', reciever/sender name]
current_block = Transactions.head
while current_block != None:
    print(current_block.data)
    current_block = current_block.next
    
# returns nothing , since its empty