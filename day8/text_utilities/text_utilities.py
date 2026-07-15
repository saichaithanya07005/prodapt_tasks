def word_count(text):
    return len(text.split())

def unique_words(text):
    return list(set(text.split()))

def string_reversal(text):
    return text[::-1]

def main():
    text = input("Enter the input string: ")
    print(f" Total words in '{text}' is {word_count(text)}")
    print(f" The unique words are {unique_words(text)}")
    print(f"Rever of the input string is {string_reversal(text)}")