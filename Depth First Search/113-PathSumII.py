class TreeNode:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

class Solution:

    def pathSum(self, root, target):

        result = []
        def dfs(root, path):
            if root is None:
                return
            if not root.left and not root.right:
                path.append(root.value)

                #adding curr path to result if leaf node and target is met
                if sum(path) == target:
                    result.append(path)

            #traversing left subtree
            dfs(root.left, path+[root.value])

            #traversing right subtree
            dfs(root.right, path+[root.value])

        dfs(root, [])
        return result
                

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    s = Solution()
    print(s.pathSum(root, 3))

#Time Complexity - O(n)
#Space Complexity - O(1) - not considering recursion stack