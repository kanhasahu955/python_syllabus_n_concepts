# count characters in a string
s = "hello world"
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1    
print(char_count)
