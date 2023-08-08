class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class Solution:
    def zigzagTraversal(self, root):
        result = []

        #bfs
        def traverse(root):
            if root is None:
                return
            odd = False
            queue = []
            queue.append(root)
            #traversing for all nodes
            while(queue):
                currentLen = len(queue)
                level = []
                #traversing the current level
                for i in range(currentLen):
                    #getting the current node
                    temp = queue.pop(0)
                    level.append(temp.val)
                    if temp.left:
                        #adding left child
                        queue.append(temp.left)
                    if temp.right:
                        #adding right child
                        queue.append(temp.right)
                if odd:
                    #for zig-zag, at odd levels, reversing the nodes
                    level.reverse()
                result.append(level)
                odd = not odd
                
               
        traverse(root)
        return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.zigzagTraversal(root))


# Time Complexity -> O(n)
# Space Complexity -> O(n) 