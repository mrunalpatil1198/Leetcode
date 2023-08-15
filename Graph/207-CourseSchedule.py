from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        indegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]

        #creating adjacency list and getting indegrees of all courses
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
        
        q = deque()
        
        #adding courses to queue that do not need any prerequisities
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        visited = 0
        
        #Topological sort
        while q:
            curr = q.popleft()
            visited += 1

            for neighbor in adj[curr]:
                #removing the edge from curr to neighbor as the prerequisite is satisfied
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return visited == numCourses
    
if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(numCourses = 2, prerequisites = [[1,0]]))

#Time Complexity - O(m+n)
#Space Complexity - O(m+n)
