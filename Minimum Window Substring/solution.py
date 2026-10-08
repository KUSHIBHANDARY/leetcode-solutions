from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = {}

        left = 0
        have = 0
        need = len(target)

        result = ""
        result_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == need:
                if right - left + 1 < result_len:
                    result = s[left:right + 1]
                    result_len = right - left + 1

                left_char = s[left]
                window[left_char] -= 1

                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1

                left += 1

        return result