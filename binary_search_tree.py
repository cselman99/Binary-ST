from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == TreeNode)
                and self.key == other.key
                and self.data == other.data
                and self.left == other.left
                and self.right == other.right
                )

    def __repr__(self):
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root == None

    def search(self, key): # returns True if key is in a node of the tree, else False
        return self._search(key, self.root)

    def _search(self, key, node):
        if self.is_empty():
            return False
        if key == node.key:
            return True
        if node.right != None and key > node.key:
            node = node.right
            return self._search(key, node)
        elif node.left != None and key < node.key:
            node = node.left
            return self._search(key, node)
        else:
            return False

    def insert(self, key, data=None): # inserts new node w/ key and data
        self._insert(key, self.root, data)

    def _insert(self, key, cur_node, data=None):
        if cur_node == None:
            self.root = TreeNode(key, data)
        elif cur_node.key > key:
            if cur_node.left == None:
                cur_node.left = TreeNode(key, data)
            else:
                cur_node = cur_node.left
                self._insert(key, cur_node, data)
        elif cur_node.key < key:
            if cur_node.right == None:
                cur_node.right = TreeNode(key, data)
            else:
                cur_node = cur_node.right
                self._insert(key, cur_node, data)
        else:
            cur_node.data = data


    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        tree_loc = self.root
        minimum = tree_loc.data
        while tree_loc.left != None:
            tree_loc = tree_loc.left
            minimum = tree_loc.data
        return (tree_loc.key, minimum)

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        tree_loc = self.root
        maximum = tree_loc.data
        while tree_loc.right != None:
            tree_loc = tree_loc.right
            maximum = tree_loc.data
        return (tree_loc.key, maximum)

    def tree_height(self):
        if self.is_empty():
            return None
        return self.th_helper(self.root)

    def th_helper(self, node): 
        if node is None: 
            return -1 
        else : 
            l = self.th_helper(node.left) 
            r = self.th_helper(node.right) 
            return max(l, r) + 1

    def inorder_list(self):
        py_list = []
        node = self.root
        self._inorder_list(node, py_list)
        return py_list

    def _inorder_list(self, node, py_list):
        if node is not None:
            self._inorder_list(node.left, py_list)
            py_list.append(node.key)
            self._inorder_list(node.right, py_list)

    def _preorder_list(self, node, py_list):
        if node is not None:
            py_list.append(node.key)
            self._inorder_list(node.left, py_list)
            self._inorder_list(node.right, py_list)

    def preorder_list(self): 
        py_list = []
        node = self.root
        self._preorder_list(node, py_list)
        return py_list
        
    def level_order_list(self): 
        q = Queue(25000) # Don't change this!
        py_list = []
        q.enqueue(self.root)
        return self._lvl_order(q, self.root, py_list)

    def _lvl_order(self, q, node, py_list):
        cur_node = node
        if self.is_empty():
            return py_list
        if q.size() != 0:
            cur_node = q.dequeue()
            py_list.append(cur_node.key)
        if node.left != None and node.right != None:
            q.enqueue(node.left)
            q.enqueue(node.right)
            self._lvl_order(q, node.left, py_list)
            self._lvl_order(q, node.right, py_list)
        elif node.left != None and node.right == None:
            q.enqueue(node.left)
            self._lvl_order(q, node.left, py_list)
        elif node.left == None and node.right != None:
            q.enqueue(node.right)
            self._lvl_order(q, node.right, py_list)
        while not q.is_empty():
            cur_node = q.dequeue()
            py_list.append(cur_node.key)
        return py_list