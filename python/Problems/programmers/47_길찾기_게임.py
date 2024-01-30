class TreeNode:
    def __init__(self, info, left=None, right=None):
        self.number = info[2]
        self.data = info[:2]
        self.left = left
        self.right = right


def solution(nodeinfo):
    nodeinfo = [[*info, idx + 1] for idx, info in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x: x[1], reverse=True)
    root = TreeNode(nodeinfo[0])
    for info in nodeinfo[1:]:
        addNode(root, info)
    preorderList = []
    postorderList = []
    preorder(root, preorderList)
    postorder(root, postorderList)
    return [preorderList, postorderList]


# info : (x,y,number)
def addNode(root, info):
    if info[0] > root.data[0]:
        if not root.right:
            root.right = TreeNode(info)
        else:
            addNode(root.right, info)
    if info[0] < root.data[0]:
        if not root.left:
            root.left = TreeNode(info)
        else:
            addNode(root.left, info)


def preorder(root, order):
    if root != None:
        order.append(root.number)
        preorder(root.left, order)
        preorder(root.right, order)


def postorder(root, order):
    if root != None:
        postorder(root.left, order)
        postorder(root.right, order)
        order.append(root.number)


nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
print(solution(nodeinfo))
