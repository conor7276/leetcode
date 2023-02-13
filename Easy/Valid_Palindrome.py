#125 Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters
#  into lowercase letters and removing all non-alphanumeric characters,
#   it reads the same forward and backward.
#  Alphanumeric characters include letters and numbers.
# Optimal Solution O(N) using two pointers in the second loop
# Runtime 67% Memory 68%
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = ""
        for char in s: # check if the word has non alphanumeric characters and remove them
            if(char.isalnum() == False):
                continue
            else:
                word += char

        back_char = len(word)
        for front_char in range(len(word)): # use two pointers to traverse through the string
            back_char -= 1
            if(word[front_char] != word[back_char]):
            # if the pointers are not the same it is not a palindrome
                return False
            
        return True