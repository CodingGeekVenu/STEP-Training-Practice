'''
Problem - 3:  GE Healthcare

Input = Paragraph of text
Output = Encrypted text

Rules - 
- Lowercase - a = 1 z = 26
- Uppercase - A = 27 Z = 52
- Space = 0
- Full Stop (.) = 99
'''

def encrypt_text(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    elif char.isupper():
        return ord(char) - ord('A') + 27
    elif char == ' ':
        return 0
    elif char == '.':
        return 99
    else:
        return None

def encrypt_paragraph(paragraph):
    encrypted_chars = []
    for char in paragraph:
        encrypted_char = encrypt_text(char)
        if encrypted_char is not None:
            encrypted_chars.append(str(encrypted_char))
    return ' '.join(encrypted_chars)

text = "COVID crisis has taught us several lessons and together we have overcome this great challenge. The COVID pandemic sent shock waves through the world economy and triggered the largest global economic crisis in more than a century. The crisis led to a dramatic increase in inequality within and across countries. Preliminary evidence suggests that the recovery from the crisis will be as uneven as its initial economic impacts, with emerging economies and economically disadvantaged groups needing much more time to recover from pandemic-induced losses of income and livelihoods. Now there is a sense of introspection in people. India has emerged stronger."

print(encrypt_paragraph(text))