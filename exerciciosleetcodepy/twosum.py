class Solution(object):
    def twoSum(self, nums, target):
        array = []
        for i in range(len(nums) - 1): #primeiro número
            for j in range(i+1, len(nums)): #segundo numero
                soma = nums[i] + nums[j]
                if soma == target:
                    array.append(i)
                    array.append(j)
                    return array
        return array


if __name__ == "__main__":
    sol = Solution()
    resultado = sol.twoSum([3,2,3], 6)
    print(resultado)