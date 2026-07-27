class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]: #sempre dá esqueda para direita
                j+= 1
                nums[j] = nums[i]

        return j + 1
        
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2,2,3]
    resultado = sol.removeDuplicates(nums)
    print(resultado)
    print(nums)