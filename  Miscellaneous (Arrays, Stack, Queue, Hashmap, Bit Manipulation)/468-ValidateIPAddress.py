class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        #checking all conditions of ipv4
        def ipv4(ip):
            if len(ip) != 4:
                return False
            for i in ip:
                if len(i) == 0:
                    return False
                if (len(i) > 1 and i[0] == '0') or (not i.isdigit()) or int(i) < 0 or int(i) > 255:
                    return False
            return True
        
        #checking all conditions of ipv6
        def ipv6(ip):
            hexdigits = '0123456789abcdefABCDEF'
            if len(ip) != 8:
                return False
            for i in ip:
                if len(i) == 0 or len(i) > 4 or not all(c in hexdigits for c in i):
                    return False
            return True
        
        #checking if queryIP is ipv4 or ipv6
        if '.' in queryIP:
            if ipv4(queryIP.split('.')):
                return "IPv4"
        elif ':' in queryIP:
            if ipv6(queryIP.split(':')):
                return "IPv6"
        return "Neither"
    
if __name__ == '__main__':
    s = Solution()
    print(s.validIPAddress(queryIP = "1e1.4.5.6"))

#Time Complexity - O(1)
#Space Complexity - O(1)