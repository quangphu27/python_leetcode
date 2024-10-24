class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        max_length = max(len(a), len(b))

        a = a.zfill(max_length)
        b = b.zfill(max_length)

        for i in range(max_length - 1, -1, -1):
            total = carry + int(a[i]) + int(b[i])
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append('1')

        return ''.join(result[::-1])
