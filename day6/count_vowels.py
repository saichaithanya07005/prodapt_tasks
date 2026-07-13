def count_vowels(text):
    count = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u') + text.count('A') + text.count('E') + text.count('I') + text.count('O') + text.count('U')
    return count

print(count_vowels("Hello, World!"))