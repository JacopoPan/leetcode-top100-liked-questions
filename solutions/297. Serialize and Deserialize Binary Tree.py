"""
Runtime: 828 ms, faster than 5.01% of Python3 online submissions for Serialize and Deserialize Binary Tree.
Memory Usage: 19.1 MB, less than 32.99% of Python3 online submissions for Serialize and Deserialize Binary Tree.
"""
from typing import List
from typing import Optional

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        ptrs = [root]
        while len(ptrs) > 0:
            new_ptrs = []
            for p in ptrs:
                if p is not None:
                    data.append(p.val)
                    new_ptrs.append(p.left)
                    new_ptrs.append(p.right)
                else:
                    data.append('null')
            ptrs = new_ptrs
        listToStr = ' '.join([str(elem) for elem in data])
        return listToStr
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = list(data.split(" "))
        if data[0] == 'null':
            return None
        else:
            root = TreeNode(data[0])
            data = data[1:]
            ptrs = [root]
            while len(ptrs) > 0:
                new_ptrs = []
                for p in ptrs:
                    if data[0] == 'null':
                        p.left = None
                    else:
                        p.left = TreeNode(data[0])
                        new_ptrs.append(p.left)
                    if data[1] == 'null':
                        p.right = None
                    else:
                        p.right = TreeNode(data[1])
                        new_ptrs.append(p.right)
                    data = data[2:]
                ptrs = new_ptrs
            return root

def main():
    ser = Codec()
    deser = Codec()
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    root.left = node2
    root.right = node3
    node3.left = node4
    node3.right = node5
    ans = deser.deserialize(ser.serialize(root))
    list_ans = []
    ptrs = [ans]
    while len(ptrs) > 0:
        new_ptrs = []
        for p in ptrs:
            if p is not None:
                list_ans.append(p.val)
                new_ptrs.append(p.left)
                new_ptrs.append(p.right)
            else:
                list_ans.append('null')
        ptrs = new_ptrs
    print('Output:', list_ans)
    print('Expected:', ['1','2','3','null','null','4','5','null','null','null','null'])

if __name__ == "__main__":
    main()
