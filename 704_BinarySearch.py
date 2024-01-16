
def search(nums: list[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right: # Iterative loop until pointers meet
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    print(search([1,2,3,4,5,6,7,8,9,10], 5))