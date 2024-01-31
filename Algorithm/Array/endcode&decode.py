def encode( strs: [str]) -> str:
    encoded = ""
    for i in strs:
        encoded += str(len(i)) + '@' + i
    return encoded

def decode( s: str) -> [str]:
    
    decoded = []
    i = 0
    while i<(len(s)):
        j = i
        while s[j]!='@':
            j+=1
        size = int(s[i:j])
        st = ""
        i= j+1
        st += s[i:(i+size)]
        decoded.append(st)
        i = (i+size)
    return decoded


# Test Case 1
strs = ["hello", "world", "github"]
encoded_str = encode(strs)
decoded_str = decode(encoded_str)
assert decoded_str == strs

# Test Case 2
strs = ["abc", "def", "ghi"]
encoded_str = encode(strs)
decoded_str = decode(encoded_str)
assert decoded_str == strs

# Test Case 3
strs = []
encoded_str = encode(strs)
decoded_str = decode(encoded_str)
assert decoded_str == strs

# Test Case 4
strs = ["123", "456", "789"]
encoded_str = encode(strs)
decoded_str = decode(encoded_str)
assert decoded_str == strs