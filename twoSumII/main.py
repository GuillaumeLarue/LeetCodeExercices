from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while (numbers[left] + numbers[right]) != target:
            if (numbers[left] + numbers[right]) > target:
                right -= 1
            elif (numbers[left] + numbers[right]) < target:
                left += 1
        return [left + 1, right + 1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        # Too long
        l = len(numbers)
        mx = l - 1
        mn = 0
        while numbers[mx] > target and mx >= 0 and numbers[mx - 1] >= 0:
            mx -= 1
            # print(mx)
        while numbers[mn] < -target and mn < l - 1 and numbers[mn + 1] >= 0:
            mn += 1
            # print(mn)
        for i in range(mx + 1):
            for j in range(mn, mx + 1):
                # mn-1 ?
                if i == j:
                    continue
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
