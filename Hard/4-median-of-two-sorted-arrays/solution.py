class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays in O(log(min(m,n))) time.
        
        Args:
            nums1: First sorted array
            nums2: Second sorted array
            
        Returns:
            The median value as a float
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            partition1 = (left + right) // 2
            # Partition nums2 such that left half has same number of elements
            partition2 = (m + n + 1) // 2 - partition1
            
            # Handle edge cases for partitions at boundaries
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # We found the correct partition
                # Calculate median based on total length
                if (m + n) % 2 == 0:
                    # Even total length
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    # Odd total length
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                # We're too far right in nums1, go left
                right = partition1 - 1
            else:
                # We're too far left in nums1, go right
                left = partition1 + 1
        
        # Should never reach here with valid input
        raise ValueError("Invalid input arrays")


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 3]
    nums2 = [2]
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {solution.findMedianSortedArrays(nums1, nums2)}")
    print(f"Expected: 2.0\n")
    
    # Test case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {solution.findMedianSortedArrays(nums1, nums2)}")
    print(f"Expected: 2.5\n")
    
    # Test case 3
    nums1 = []
    nums2 = [1]
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {solution.findMedianSortedArrays(nums1, nums2)}")
    print(f"Expected: 1.0")
