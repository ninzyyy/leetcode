
def search(nums: list[int], target: int) -> int:
        count = -1
        for n in nums:
            count += 1
            if n == target:
                return count
        return -1

if __name__ == "__main__":
    print(search([1,2,3,4,5,6,7,8,9,10], 5))