# %%
for i in range(1,9): print(i)

# %%
amount = 1

if amount in range(0,2):
  print(f"Found {amount}")
else:
  print("not found")

# %%
class Node:                     # each element of a linked list 
    def __init__(self, value):  
        self.value = value      # will have a value
        self.next = None        # and a reference to the next element in the LL

class LinkedList:

    def __init__(self, value, amount):
        self.head = None
        self.tail = None
        self.length = 0
        if amount < 1: return None
        elif amount == 1:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            for i in range(2, amount + 1):
                print(i)
                new_node = Node(value)
                self.head = new_node
                self.tail = new_node
                self.length += 1

    def append(self, value):
        new_node = Node(value)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

ll = LinkedList(221,10)
print(ll)


