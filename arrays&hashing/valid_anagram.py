class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        
        for value in s:
            if value in t:
                s_dict[value] = s.count(value)
                t_dict[value] = t.count(value)
            else:
                return False
        
        for key in list(s_dict.keys()):
            if s_dict[key] != t_dict[key]:
                return False
        return True