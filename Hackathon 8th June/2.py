import sys

string = sys.stdin.readline()
str_list = list(string.split())

char_length = 0

for i in str_list:
    char_length += len(i)

print("Words: ", len(str_list))
print("Characters: ", char_length)
print("Reversed: ", " ".join(str_list[::-1]))
print("Title Case: ", string.title())
