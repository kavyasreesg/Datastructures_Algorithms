# Algorithm:
# for a string to be a palindrome it should have almost one
# character to occur odd number of times and other to occure
# even number of times


string = input("Enter input string : ")

# Idea is to maintain count list for all alphabets

alphabet_array = [0] * 256

for i in range(len(string)):
    alphabet_array[ord(string[i])] = alphabet_array[ord(string[i])] + 1


odd_count = 0

for j in range(len(alphabet_array)):

    if alphabet_array[j] & 1:
        odd_count += 1

    if odd_count > 1:
        print("can't form palindrome")
        break

if odd_count == 1:
    print("can form palindrome")






