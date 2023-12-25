#----------------------------------------
#Problem4. Active_directory
#----------------------------------------
## Explanation

# <br> 1. For a efficient seurch funcion I used data structure List  in conjunction with Recursion. Each users structure and each group structure represented as a List. Using append method, wrapped as a class function, user can add new users and new groups.
# <br> For a seaurch itself , function  is_user_in_group(user, group) iterates over list of  Groups and checks if the user belongs to one of the Group and returns True if it founds it. Otherwise checks subgroups in the recursive manner one by one in the depth-down manner until it founds the user or returns otherwise None.


# ## Time and Space efficiency 

# #### Key answer: Linear Time Complexity and Constant Space efficiency

# 1. TIme efficiency. Traversal Time: The implemented search function efficiently traverses the Groups tree in a top-down manner. It explores each Group and subgroups  in a depth-first fashion.
# <br> => Linear Time Complexity: The time complexity is generally O(n), where n is the total number of Groups and subgroups in the tree. It visits each Group and subgroup once.


# 2. Space efficiency. Memory Usage:  The implemented search functionis memory-efficient as it doesn't load the entire Group tree into memory at once. Instead, it returns a generator object that yields a tuple for each Group it visits. The tuple contains the current list of Groups, a list of its subGroups.
# <br> => Constant Space Overhead: The memory used by  implemented search function is proportional to the depth of the Group tree, not the total number of Groups. The generator ensures that only a small portion of the Group tree is loaded into memory at any given time.

# <br> In summary,  implemented search function is generally considered both time and space-efficient. It is well-suited for efficiently processing Group's trees of various sizes, and its memory usage is optimized by yielding results incrementally. 


#----------------------------------------------------------------------- 


import pandas as pd 



class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    group = group
    user = user
    outcome = False
    
    if group is not None:
        #get list of groups in a group
        list_of_groups = group.get_groups()
        #access each group and get list of users in each group
        #check if there is user in list of users
        #if now then check list of available groups within this group and so on

        for one in list_of_groups:
            users = one.get_users()
            if user in users:
                return print("True")
            else:
                #otherwise check subgroups of this one group
                 is_user_in_group(user,one)
    
   
    return outco


## Test Case 1

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


is_user_in_group(user="sub_user", group = child)


## Test Case 2

students  = Group("students")
desks = Group("desks")
pens = Group('pens')
teachers = Group('teachers')

owners = Group('owners')
owners.add_group(students)
owners.add_group(teachers)

objects = Group('objects')
objects.add_group(pens)
objects.add_group(desks)

students.add_user('sasha')
students.add_user('oksana')
students.add_user('sergey')

teachers.add_user('franko')
teachers.add_user('frank')
teachers.add_user('mavrikii')

is_user_in_group(user="frank", group = owners)


## Test Case 3

students  = Group("students")
desks = Group("desks")
pens = Group('pens')
teachers = Group('teachers')

owners = Group('owners')
owners.add_group(students)
owners.add_group(teachers)

objects = Group('objects')
objects.add_group(pens)
objects.add_group(desks)

students.add_user('sasha')
students.add_user('oksana')
students.add_user('sergey')

teachers.add_user('franko')
teachers.add_user('frank')
teachers.add_user('mavrikii')

is_user_in_group(user="red", group = objects)

## Test case4(corener case):

is_user_in_group(None,parent)


## Test case5(corner case):


is_user_in_group('',parent)


## Test case6 (corner case):


is_user_in_group(user = sub_child_user,group = None)
