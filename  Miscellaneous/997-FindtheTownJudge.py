from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        trust_map = defaultdict(lambda : [0,0])

        #counting the number of people trust trust[i] person and number of people trust[i] trusts
        for i in range(len(trust)):
            trust_map[trust[i][0]][1] += 1
            trust_map[trust[i][1]][0] += 1
        
        #iterating to find out person trusted by n people and trusts 0 people
        for k, v in trust_map.items():
            if v[0] == n-1 and v[1] == 0:
                return k
        
        return -1
    
if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(n = 2, trust = [[1,2]]))

#Time Complexity - O(n)
#Space Complexity - O(n)