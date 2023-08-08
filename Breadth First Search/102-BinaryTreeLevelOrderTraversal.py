class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class Solution:
    def levelOrderTraversal(self, root):
        if root == None:
            return []
        
        result = []

        #bfs
        def traverse(root):
            queue = []
            queue.append(root)
            #traversing for all nodes
            while(len(queue) > 0):
                level = []
                currentLen = len(queue)
                #traversing the current level
                for i in range(0, currentLen):
                    #getting the current node
                    temp = queue.pop(0)
                    level.append(temp.val)
                    if temp.left:
                        #adding left child
                        queue.append(temp.left)
                    if temp.right:
                        #adding right child
                        queue.append(temp.right)
                result.append(level)
        traverse(root)
        return result

#Time Complexity - O(n)
#Space Complexity - O(n)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.levelOrderTraversal(root))


# Time Complexity -> O(n)
# Space Complexity -> O(n) 