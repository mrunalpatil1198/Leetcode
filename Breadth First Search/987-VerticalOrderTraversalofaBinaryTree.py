class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    def verticalTraversal(self, root) -> list[list[int]]:
        
        if not root:
            return []
        
        results = defaultdict(list)
        
        #adding node val, col index and row index of root
        queue = [(root, 0, 0)]
        
        #bfs
        #traversing for all nodes
        while queue:
            #getting the curr node
            node, col, row = queue.pop(0)

            #updating the result list
            results[(col,row)].append(node.val)

            #sorting according to values
            results[(col,row)].sort()
            if node.left:
                #adding left child to queue with curr col-1 and curr row+1
                queue.append((node.left, col-1, row+1))
            if node.right:
                #adding right child to queue with curr col+1 and curr row+1
                queue.append((node.right, col+1, row+1))
            
        res = defaultdict(list)

        #sorting according to col as we need vertical order
        positions = sorted(results.keys(), key=tuple)
        
        #getting all the values col wise from left to right
        for position in positions:
            col, row = position
            res[col].extend(results[position])

        return res.values()
    
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    print(list(s.verticalTraversal(root)))

