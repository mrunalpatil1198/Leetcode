class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root) -> list[list[int]]:
        result = []

        if not root:
            return root

        #bfs
        def traverse(root):
            queue = []
            queue.append(root)
            #traversing for all nodes
            while(queue):
                currentLen = len(queue)
                level = []
                #traversing curr level
                for i in range(currentLen):
                    temp = queue.pop(0)
                    level.append(temp.val)
                    if temp.left:
                        #adding left child
                        queue.append(temp.left)
                    if temp.right:
                        #adding right child
                        queue.append(temp.right)
                result.append(level)
            return result

        #reversing the result of normal bfs for bottom-up travesal
        return reversed(traverse(root))
    
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    print(list(s.levelOrderBottom(root)))
    
#Time Complexity - O(n)
#Space Complexity - O(n)