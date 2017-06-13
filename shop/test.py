def getDepth(root):
    if root is None:
        return 0
    else:
        return max(getDepth(root.left), getDepth(root.right))+1

def isBalance(root, leng):
    if Iniitree(root, leng) is None:
        return True
    elif abs(getDepth(root.right) - getDepth(root.left)) > 1:
        return False
    else:
        return isBalance(root.right) & isBalance(root.left)


class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


def InsertElement(root, node):
    if root:
        if node.data < root.data:
            if root.left:
                InsertElement(root.left, node)
            else:
                root.left = node
        else:
            if root.right:
                InsertElement(root.right, node)
            else:
                root.right = node
    else:
        return 0

def Iniitree(datasourse, leng):
    root = Node(datasourse[0])

    for x in range(1, leng):
        node = Node(datasourse[x])
        InsertElement(root, node)
    return root




data = [1, 2, 3, 9, 8]
isBalance(data, 5)

