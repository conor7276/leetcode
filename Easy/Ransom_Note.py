# 383 RansomNote https://leetcode.com/problems/ransom-note
# Runtime Beats 62.17% 84ms Memory 14.1 MB Beats 52.69%
# O(N + log(n))
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if(len(ransomNote) > len(magazine)):
            return False

        else:
            # search each letter of ransomNote in magzine
            for letter in ransomNote:
                if letter in magazine:
                    #if found then then delete that character of magazine
                    magazine = magazine.replace(letter, '', 1)
                else:
                    #otherwise return false
                    return False
            return True