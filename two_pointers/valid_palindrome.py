class Solution:
    def isPalindrome(self, s: str) -> bool:
        num_list = ['0', '1', '2', '3', '4',
                    '5', '6', '7', '8', '9']
        latest_counter = len(s) - 1
        for i in range(len(s)):
            word_1 = s[i]
            if word_1.isalpha():
                word_1 = word_1.lower()
            elif word_1 in num_list:
                pass
            else:
                continue
            while latest_counter >= 0:
                if i == latest_counter:
                    return True
                word_2 = s[latest_counter]
                if word_2.isalpha():
                    word_2 = word_2.lower()
                    latest_counter -= 1
                    break
                elif word_2 in num_list:
                    latest_counter -= 1
                    break
                else:
                    latest_counter -= 1
            if word_1 != word_2:
                return False
        
        return True
