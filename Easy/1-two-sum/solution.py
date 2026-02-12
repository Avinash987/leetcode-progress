class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Find two numbers in the array that add up to the target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing indices of the two numbers
        """
        # Hash map to store number -> index mapping
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our map
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # No solution found (shouldn't happen per problem constraints)
        return []


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.twoSum(nums1, target1)}")
    print(f"Expected: [0, 1]\n")
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.twoSum(nums2, target2)}")
    print(f"Expected: [1, 2]\n")
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.twoSum(nums3, target3)}")
    print(f"Expected: [0, 1]")
