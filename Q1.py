from typing import List 
import re

def find_min(nums: List[int]) -> int:
    left, right = 0 , len(nums) - 1
    
    if nums[left] < nums [right]:
        return nums[left]
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums [right]:
            left = mid + 1
        
        else:
            right = mid
    
    return nums[left]

if __name__ == "__main__":
    user_input = input("Enter an Array")
    nums = [int(x) for x in re.findall(r'-?\d', user_input)]
    if nums:
        result = find_min(nums)
        print(result)
    else:
        print("Error")