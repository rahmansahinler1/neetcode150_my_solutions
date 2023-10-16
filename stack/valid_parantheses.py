class Solution:
    def isValid(self, s: str) -> bool:
        dict_bracket = {')':'(', '}':'{', ']':'['}
        close_brackets = list(dict_bracket.keys())
        prev = -1
        for i, val in enumerate(s):
            if val in close_brackets:
                if i > 0:
                    if dict_bracket[val] == s[prev]:
                        s = s.replace(dict_bracket[val] + val, '', 1)
                        prev -= 2
                    else:
                        return False
                else:
                    return False
            prev += 1
        
        if not s:
            return True
        else:
            return False
