sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)

"""we can use this also to find the longest word in a sentence. The code takes a sentence as input, splits it into words, and then iterates through each word to find the longest one. Finally, it prints the longest word found in the sentence.
longest_word = max(words, key=len)"""