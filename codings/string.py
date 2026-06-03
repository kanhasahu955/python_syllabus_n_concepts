# # reverse a string
# # compress a string
# # decompress a string
# # remove duplicates from a string
# # remove spaces from a string
# # remove punctuation from a string
# # remove numbers from a string
# # remove special characters from a string
# # remove vowels from a string
# # remove consonants from a string
# # remove digits from a string
# # remove uppercase letters from a string
# # remove lowercase letters from a string
# # remove whitespace from a string
# # match parentheses are balanced


# class String:
#     def __init__(self,string:str):
#         self.string = string

#     def reverse_string(self)->str:
#         # return self.string[::-1]
#         reversed_string = ''
#         for char in self.string:
#             reversed_string = char + reversed_string
#         return reversed_string

#     def compress_string(self)->str:
#         compressed_string = ""
#         count = 1 
#         for i in range(1,len(self.string)):
#             if self.string[i] == self.string[i-1]:
#                 count += 1
#             else:
#                 compressed_string += self.string[i-1] + str(count)
#                 count = 1
#         compressed_string += self.string[-1] + str(count)
#         return compressed_string

#     def decompress_string(self)->str:
#         decompressed_string = ""
#         for i in range(0,len(self.string),2):
#             decompressed_string += self.string[i] * int(self.string[i+1])
#         return decompressed_string
    
#     def remove_duplicates(self)->str:
#         return ''.join(sorted(set(self.string)))

#     def remove_spaces(self)->str:
#         return self.string.replace(" ", "")
    
#     def remove_punctuation(self)->str:
#         return ''.join(char for char in self.string if char.isalpha())
    
#     def remove_numbers(self)->str:
#         return ''.join(char for char in self.string if not char.isdigit())
    
#     def remove_special_characters(self)->str:
#         return ''.join(char for char in self.string if char.isalpha())
    
#     def remove_vowels(self)->str:
#         return ''.join(char for char in self.string if char.lower() not in 'aeiou')
    
#     def remove_consonants(self)->str:
#         return ''.join(char for char in self.string if char.lower() in 'aeiou')
        
#     def remove_digits(self)->str:
#         return ''.join(char for char in self.string if not char.isdigit())

#     def remove_uppercase_letters(self)->str:
#         return ''.join(char for char in self.string if char.islower())

#     def remove_lowercase_letters(self)->str:
#         return ''.join(char for char in self.string if char.isupper())

#     def remove_whitespace(self)->str:
#         return ''.join(char for char in self.string if char != ' ')
        
#     def match_parentheses_are_balanced(self)->bool:
#         stack = []
#         for char in self.string:
#             if char == '(':
#                 stack.append(char)
#             elif char == ')':
#                 if not stack:
#                     return False
#                 stack.pop()
#         return len(stack) == 0

#     def is_palindrome(self)->bool:
#         return self.string == self.string[::-1]
    
#     def is_anagram(self,other_string:str)->bool:
#         return sorted(self.string) == sorted(other_string)

# string = String("Hello")
# print(f'Reverse string {string.string}: {string.reverse_string()}')


# reversed_string = ""
for char in "Hello":
    reversed_string = char + reversed_string
print(reversed_string)

# compress a string
string = "aaaabbccccc"
compressed_string = ""
count = 1
for i in range(1,len(string)):
    if string[i] == string[i-1]:
        count += 1
    else:  
        compressed_string += string[i-1] + str(count)
        count = 1
compressed_string += string[-1] + str(count)
print(compressed_string)


# decompress a string
compressed_string = "a4b2c5"
decompressed_string = ""
for i in range(0,len(compressed_string),2):
    decompressed_string += compressed_string[i] * int(compressed_string[i+1])
print(decompressed_string)

# remove duplicates from a string
string = "aaabbbccc"
unique_string = ""
for char in string:
    if char not in unique_string:
        unique_string += char
print(unique_string)


def is_balanced(s):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in "({[":
            stack.append(char)

        elif char in ")}]":
            if not stack:
                return False

            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0


print(is_balanced("({[]})"))   # True
print(is_balanced("({[})"))    # False
print(is_balanced("((()))"))   # True
print(is_balanced("(()"))      # False