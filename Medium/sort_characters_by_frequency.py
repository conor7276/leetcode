# Leetcode #451

# More optimal solution O(n*log(n)) 51% runtime 74% memory

class Solution:
    def frequencySort(self, s: str)-> str:
        freq = {}
        for char in s: # add string letters and count them
            if char not in freq: # if letter is not in dict
                freq[char] =1
            else:
                freq[char] +=1
        char_sorted = sorted(freq, key=freq.get, reverse = True)
        #sort the dictionary into a list
        print(char_sorted)
        res = ""
        for char in char_sorted: # add the sorted chars to the new string
            res = res + char*freq[char]
        return res




# Not so optimal solution O(n^2) runtime 19.57%, Memory 74.5%, slow but good on memory
# First Attempt
class Solution:
    def frequencySort(self, s: str) -> str:
        letters = {} #key: letter, value: frequency of letter from string
        for char in s: # count and update the dictionary with values of the string
            if char not in letters: 
                letters.update({char : 1})
            else:
                count = letters.get(char)
                letters.update({char : count + 1})
        
        freqsortword = "" #store the word
        while(letters): #go through all letters until there are no more in the dict

            high = max(letters.values()) # get the highest value in dictionary
            same_length_letters = [] # store all letters that match this value
            for key, value in letters.items():
                if(value == high):
                    same_length_letters.append([key,value])

            same_length_letters.sort() # sort the letters

            for pair in same_length_letters: # add the letters to the string
                for char in range(pair[1]):
                    freqsortword += pair[0]

            for let in same_length_letters: # pop used letters from the dict
                letters.pop(let[0])

        return freqsortword # return the word

