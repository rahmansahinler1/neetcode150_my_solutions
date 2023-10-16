class Codec:
    def encode(self, strs):
        encoded_str = ''
        
        for value in strs:
            encoded_str += str(len(value)) + '#' + value
        
        return encoded_str

    def decode(self, s):
        decoded_str = ''
        numbers = ['0', '1', '2', '3', '4',
                   '5', '6', '7', '8', '9']
        i = 0
        
        for i, value in enumerate(s):
            if i > 0:
                if value == '#':
                    j = i
                    while (s[j - 1] in numbers) and (j - 1 >= 0):
                        j-= 1
                    length = int(s[j:i])
                    if j != i:
                        decoded_str += s[i+1: i+length+1]
            
        return decoded_str
