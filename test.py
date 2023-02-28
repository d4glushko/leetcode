from typing import List

def sortArrayByParityII(nums: List[int]) -> List[int]:
    even = 0
    odd = 1
    
    while even and odd < len(nums):
        while even < len(nums) and nums[even] % 2 == 0:
            even += 2
            
        while odd < len(nums) and nums[odd] % 2 == 1:
            odd += 2
            
        print(f"{even}, {odd}")
        nums[odd], nums[even] = nums[even], nums[odd]
        odd += 2
        even += 2
        
    return nums

res = sortArrayByParityII([4, 2, 5, 7])
print(res)
