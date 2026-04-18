class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        count = 0
        product = 1
        for n in nums:
            if n != 0:
                product *= n
            if n == 0:
                count += 1

        output = list()
        print(count)

        for i in range(len(nums)):
            if count >= 2:
                output.append(0)
            if count == 1:
                if nums[i] != 0:
                    output.append(0)
                else:
                    output.append(product)
            if count == 0:
                output.append(product//nums[i])

        return output

        