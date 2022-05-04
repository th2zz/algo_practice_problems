class Solution:
    def twoSum(self, numbers, target):
        numbers.sort()
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [numbers[left], numbers[right]]
        return [-1, -1]
