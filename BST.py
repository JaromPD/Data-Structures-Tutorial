class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root) # _insert() will be created next.

    def _insert(self, data, node):
        if node.data != data:
            if data < node.data:
                if node.left is None:
                    node.left = BST.Node(data)
                else:
                    self._insert(data, node.left)
            else:
                if node.right is None:
                    node.right = BST.Node(data)
                else:
                    self._insert(data, node.right)
        else:
            pass # May be a good spot for an error message. 

    def __contains__(self, data):
        return self._contains(data, self.root) 
    
    def _contains(self, data, node):
        if data == node.data:
            return True
        else:
            if data < node.data:
                if node.left is None:
                    return False
                else:
                    return self._contains(data, node.left)
            else:
                if node.right is None:
                    return False
                else:
                    return self._contains(data, node.right)
    
    def __iter__(self):
        yield from self._traverse_forward(self.root) # Will be created next.
    
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    def __reversed__(self):
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    def _get_height(self, node):
        if node == None:
            return 0
        left_side = self._get_height(node.left)
        right_side = self._get_height(node.right)
        if left_side > right_side:
            return left_side + 1
        else:
            return right_side + 1 
    
def create_bst_from_sorted_list(sorted_list):
    bst = BST()
    _insert_middle(sorted_list, 0, len(sorted_list) - 1, bst)
    return bst
def _insert_middle(sorted_list, first, last, bst):
    if first > last:
        return
    else:
        middle_i = ((last-first)//2) + first
        bst.insert(sorted_list[middle_i])
        _insert_middle(sorted_list, first, middle_i - 1, bst)
        _insert_middle(sorted_list, middle_i + 1, last, bst)