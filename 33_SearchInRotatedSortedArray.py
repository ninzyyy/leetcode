
def search(nums: list[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] > nums[left]:
                if nums[middle] > target >= nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1

nums = [4, 5, 6, 7, 0 , 1, 2]
target = 0
print(search(nums,target))