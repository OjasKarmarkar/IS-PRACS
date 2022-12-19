import hashlib


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.hash = hashlib.sha256(str(data).encode("utf-8")).hexdigest()
        self.left = left
        self.right = right


class MerkelTree:
    def __init__(self, leaves):
        self.root = Node(leaves)
        open = [self.root]
        while len(open) > 0:
            new_item = open.pop(0)
            data_split = new_item.data
            half_data_len = int(len(data_split)/2)
            
            if half_data_len > 0:
                new_leaves = [Node(data_split[:half_data_len]), Node(
                    data_split[half_data_len:])]

                new_item.left = new_leaves[0]
                new_item.right = new_leaves[1]

                open.extend(new_leaves)

    def print_tree(self):
        open = [self.root]
        while len(open) > 0:
            new_item = open.pop(0)
            
            print("Content: ", new_item.data)
            print("Hash: ", new_item.hash)
            print("\n", new_item.hash)
            
            new_right = new_item.right
            new_left = new_item.left
            
            if new_right is not None:
                open = [new_right] + open
                
            if new_left is not None:
                open = [new_left] + open
            


tree = MerkelTree(["This", "is", "an", "example", "of", "a", "merkel", "tree"])
tree.print_tree()
