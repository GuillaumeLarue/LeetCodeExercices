class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
                i += 1
            else:
                old_last = last_c[s[i]]
                last_c[s[i]] = i
                i = old_last

                # tmp_sub = [s[i]]
                tmp_sub = []
                i += 1
                tmp_count = 0

            max_count = max(max_count, tmp_count)
        return max_count


if __name__ == '__main__':
    solution = Solution()
    solution.lengthOfLongestSubstring(s="PyCharm")
