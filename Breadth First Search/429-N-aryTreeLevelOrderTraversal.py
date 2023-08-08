class TreeNode:
    def __init__(self, value, children = []) -> None:
        self.children = children
        self.value = value

class Solution:

    def levelOrder(self, root) -> list[list[int]]:
        if root is None:
            return None
        
        result = []
        queue = []
        queue.append(root)

        #bfs
        #traversing for all nodes
        while(queue):
            length = len(queue)
            temp = []
            #traversing curr level
            for i in range(length):
                curr = queue.pop()
                temp.append(curr.value)
                #adding children of curr node to queue
                for child in curr.children:
                    queue.append(child)
            result.append(temp)
        return result

if __name__ == '__main__':
    root = TreeNode(1, [TreeNode(3, [TreeNode(5), TreeNode(6)]), TreeNode(2), TreeNode(4)])
    s = Solution()
    print(s.levelOrder(root))
