string = input("Enter string : ")
character = input("Enter character to remove : ")

list_of_chars = list(string)

for i in range(len(list_of_chars)):
    if list_of_chars[i] == character:
        list_of_chars[i] = ''

print(''.join(list_of_chars))
