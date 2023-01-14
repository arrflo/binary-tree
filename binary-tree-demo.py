# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. in_order_traversal(): performs in order traversal of a binary tree
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    #for min
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    #for max
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    #for in order traversal
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    #for post order traversal
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    #for pre order traversal
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

print ("------------------------------ M E N U ----------------------------------")
print ()
print ("1 - finds the element that comes first alphabetically in the binary tree")
print ("2 - finds the element that comes last alphabetically in the binary tree")
print ("3 - performs in order traversal of a binary tree")
print ("4 - performs post order traversal of a binary tree")
print ("5 - performs pre order traversal of a binary tree")
print ("6 - exit")
print ()
print ("-------------------------------------------------------------------------")
print ()


while True:
    user_in = int(input("Choose which one to do (1-6): "))
    myname_ = ['r','o','m','a','l','y','n','b','u','f','d']
    nametree = build_tree(myname_)
    if user_in == 1:
        print ("The element that comes first in alphabetical order is:",nametree.find_min())
    if user_in == 2:
        print ("The element that comes last in alphabetical order is:",nametree.find_max())
    if user_in == 3:
        print ("The in order traversal of the binary tree is:",nametree.in_order_traversal())
    if user_in == 4:
        print ("The post order traversall of the binary tree is:",nametree.post_order_traversal())
    if user_in == 5:
        print ("The pre order traversal of the binary tree is:",nametree.pre_order_traversal())
    if user_in == 6:
        ask = input("are you sure you want to exit?(y/n): ")
        if ask == 'y':
            break


