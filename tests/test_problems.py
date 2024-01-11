import pytest
from solutions.problems import Solution

sol = Solution()


class Test_leetCode:
    @pytest.mark.parametrize('nums, target, expected',
                             [([2, 7, 11, 15], 9, [0, 1]),
                              ([3, 2, 4], 6, [1, 2]),
                              ([3, 3], 6, [0, 1])
                              ])
    def test_twoSum(self, nums, target, expected):
        assert sol.twoSum(nums, target) == expected

    @pytest.mark.parametrize('s, expected',
                             [("abcabcbb", 3),
                              ("bbbbb", 1),
                              ("pwwkew", 3)])
    def test_lengthOfLongestSubstring(self, s, expected):
        assert sol.lengthOfLongestSubstring(s) == expected

    @pytest.mark.parametrize('string, expected', [("babad", "bab"),
                                                  ("cbbd", "bb")])
    def test_longestPalindrome(self, string, expected):
        assert sol.longestPalindrome(string) == expected

    @pytest.mark.parametrize('s, numRows, expected',
                             [("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
                              ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
                              ("A", 1, "A")])
    def test_convert(self, s, numRows, expected):
        assert sol.convert(s, numRows) == expected

    @pytest.mark.parametrize('x, expected',
                             [(123, 321),
                              (-123, -321),
                              (120, 21)])
    def test_reverse(self, x, expected):
        assert sol.reverse(x) == expected
