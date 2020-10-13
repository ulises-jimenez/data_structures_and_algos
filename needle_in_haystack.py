haystack = "mississippi"
needle = "pi"

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        shifts = len(haystack) - len(needle) + 1
        for shift in range(shifts):
            if haystack[shift: shift + len(needle)] == needle:
                return shift

        return -1



sol = Solution().strStr(haystack=haystack, needle=needle)
print(sol)
