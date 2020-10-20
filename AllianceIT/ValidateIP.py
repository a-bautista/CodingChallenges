class Solution:
    def validIPAddress(self, IP: str) -> str:
        # edge case
        if IP == '0.0.0.0':
            return "IPv4"

        if IP.count('.') == 3:
            res = self.helper_ipv4(IP)

        elif IP.count(':') == 7:
            res = self.helper_ipv6(IP)
        else:
            res = "Neither"
        return res

    def helper_ipv4(self, IP):
        num = IP.split(".")
        accepted_range = {str(x) for x in range(0, 256)}
        for n in num:
            if len(n) > 3:
                return "Neither"
            elif n not in accepted_range:
                return "Neither"

        return "IPv4"

    def helper_ipv6(self, IP):
        accepted_values = '0123456789ABCDEFabcdef'

        num = IP.split(":")
        # edge case: 2001:0db8:85a3::0:8A2E:0370:7334
        # there's a missing values so you have 7 values and 1 None
        num1 = list(filter(None, num))
        if len(num1) < 8:
            return "Neither"

        for n in num:
            if len(n) > 4:
                return "Neither"
            for x in n:
                if x not in accepted_values:
                    return "Neither"
        return "IPv6"

        # Input
        # Valid IPv4:
        #   172.16.254.1
        #   0.0.0.0
        #   numbers can go from 0 to 255 and there's only 3 numbers in each space

        # invalid IPv4:
        # 259.93.1.0
        # 01.8.3.1

        # valid IPv6
        #   2001:0db8:85a3:0:0:8A2E:0370:7334
        #   values can be numbers or letters from A to F and leading zeroes are allowed
        #   and there's only 4 numbers in each space

        # invalid IPv6
        # 20051:9831::1

        # my dividers are the . and the :

        # Output: IPv4, IPv6 or Neither