import collections
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        #create a dictionary to store the clones of all nodes
        clones = {node.val : Node(node.val, [])}

        #maintain a queue for bfs
        q = collections.deque()
        q.append(node)

        #bfs on graph
        while q:
            curr = q.popleft()
            #get the clone of curr node
            curr_clone = clones[curr.val]

            for neighbor in curr.neighbors:

                #if neighbor node is not seen before, add it to the dictionary of clones and queue
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                
                #add the cloned neighbor to the current node clone
                curr_clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]
    
#Time Complexity: O(V + E)
#Space Complexity: O(V)
    


