class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:

        #Approach - a graph is bipartite if we can color it using only 2 colors. 1 represents one color and -1 represents other color.

        #create a list to store color of every node
        colors = [0 for _ in range(len(graph))]

        #dfs on graph for coloring
        #i: ith node
        #color: color of ith node
        def dfs(i, color):

            #check if the node is already colored, if yes, check if with the right color
            if colors[i] != 0:
                return colors[i] == color
            
            #assign color to curr node
            colors[i] = color

            #dfs on all neighbors of curr node
            for neighbor in graph[i]:

                #recur and color all the neighbors with opposite of the curr color
                if not dfs(neighbor, -color):

                    #return False if we were not able to color any of the neighbor
                    return False
            
            #return True if we were able to color all the nodes successfully
            return True
        

        #try coloring all the nodes of the graph
        for i in range(len(graph)):

            #if not already colored, dfs on the curr node with color as 1
            if colors[i] == 0:
                if not dfs(i, 1):
                    #return False if we were not able to color
                    return False
                
        #return True if we were able to color all the nodes successfully
        return True
    
if __name__ == '__main__':
    s = Solution()
    print(s.isBipartite(graph = [[1,2,3],[0,2],[0,1,3],[0,2]]))

#Time Complexity - O(V + E)
#Space Complexity - O(V) 