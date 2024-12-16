"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?
"""

def isPalindrome(x:int) -> bool:
    reversedInteger = 0
    rem = 0
    num = x

    while x > 0:
        reversedInteger *= 10
        rem = x % 10
        x = (x - rem) / 10

        reversedInteger += rem
    
    if num == reversedInteger:
        return True
    else:
        return False

def main():
    print(isPalindrome(121))
    print(isPalindrome(122121))
    print(isPalindrome(1331))

if __name__ == '__main__':
    main()