class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        partition = []

        #checking is s[i:j+1] is a plaindrome
        def isPal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(index):
            if index >= len(s):
                result.append(list(partition))
                return
            for i in range(index, len(s)):
                #partitioning at index till i and recursively calling dfs for rest of the string
                if isPal(index, i):
                    partition.append(s[index: i+1])
                    dfs(i+1)
                    partition.pop()
        
        dfs(0)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.partition(s = "aab"))

#Time Complexity - O(n*2^n)
#Space Complexity- O(1) - not considering recursion stack