class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output_ = 0
        for r in range(len(s)):
            if s[r] not in seen:
                output_ = max(output_, r - l + 1)
            else:
                if seen[s[r]] < l:
                    output_ = max(output_, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output_

    def longestPalindrome(self, s: str) -> str:
        maxpol, n = '', len(s)
        if n == 1:
            return s
        for i in range(n - 1):
            for j in range(i + len(maxpol), n):
                if self.pol(s[i:j + 1]):
                    maxpol = s[i:j + 1]
        return maxpol

    def pol(self, s: str):
        for i in range(len(s)):
            if s[i] != s[~i]:
                return False
        return True

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)

    def reverse(self, x: int) -> int:
        if x < 0:
            s = str(x)[:0:-1]
            num = int('-' + s)
        else:
            num = int(str(x)[::-1])

        if -2 ** 31 <= num < 2 ** 31 - 1:
            return num
        return 0

