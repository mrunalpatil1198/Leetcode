class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        
        #edge case
        if not connections or len(connections) == 0:
            return []
        
        #Building a graph as adjancency list
        graph = [[] for i in range(n)]
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])

        #create list for maintaing the discovery time and low link values for each node
        discovery = [-1 for _ in range(n)]
        lowest = [0 for _ in range(n)]
        result = []

        #maintain a counter for time
        time = 0

        #Tarjan's Algorithm (dfs with track of discovery time and low link values)
        #lowest[u] indicates the earliest visited vertex (the vertex with minimum discovery time) that can be reached from a subtree rooted with u. A node u is head if disc[u] = low[u]
        def dfs(node, parent):
            if discovery[node] != -1:
                return
            nonlocal time
            time += 1
            discovery[node] = time
            lowest[node] = time
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
                if lowest[neighbor] > discovery[node]:
                    result.append([neighbor, node])
                lowest[node] = min(lowest[node], lowest[neighbor])


        dfs(0, -1)
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]))
            
#Time Complexity - O(V + E)
#Space Complexity - O(2V)