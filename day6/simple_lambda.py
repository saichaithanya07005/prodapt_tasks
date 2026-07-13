import time
start_time = time.perf_counter()

# add = lambda x, y:x + y
# print(add(5, 3))  # Output: 8

find_largest_word = lambda sentence: max(sentence.split(), key=len)
sentence = input("Enter a sentence: ")
largest_word = find_largest_word(sentence)  
print("The largest word is:", largest_word)
end_time = time.perf_counter()
print("Execution time:", end_time - start_time)