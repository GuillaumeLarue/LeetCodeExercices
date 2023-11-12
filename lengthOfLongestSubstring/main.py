class Solution:
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        i = 0
        tmp_count = 0
        max_count = 0
        tmp_sub = []
        last_c = {}
        while i < len(s):
            a = s[i]
            if s[i] not in tmp_sub:
                last_c[s[i]] = i
                tmp_sub.append(s[i])
                tmp_count += 1
            else:
                old_last = last_c[s[i]]
                last_c[s[i]] = i
                i = old_last
                tmp_sub = []
                tmp_count = 0
            i += 1

            max_count = max(max_count, tmp_count)
        return max_count

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding windows
        l = 0
        seen = {}
        res = 0
        for r in range(len(s)):
            if s[r] not in seen:
                res = max(res, r - l + 1)
            else:  # s[i] in seen
                if seen[s[r]] >= l:
                    l = seen[s[r]] + 1
                else:
                    res = max(res, r - l + 1)
            seen[s[r]] = r
        return res