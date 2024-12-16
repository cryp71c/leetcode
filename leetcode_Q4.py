"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

"""

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    sorted_array = sorted(nums1+nums2)
    if len(sorted_array) % 2 == 0:
        return ((sorted_array[int(len(sorted_array)/2)-1]+sorted_array[int(len(sorted_array)/2)])/2)
    else:
        return sorted_array[int(len(sorted_array)/2)]
    

def main():
    print(findMedianSortedArrays([56, 89, 23, 12, 37, 71, 4, 95, 64, 50], [33, 62, 17, 98, 41, 28, 76, 84, 59, 14]))
    print(findMedianSortedArrays([1,2], [3,4]))
    print(findMedianSortedArrays([1,2], [3,4,5]))


if __name__ == '__main__':
    main()