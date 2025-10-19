"""
get text
get words
get word_count
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
get max_length
get sorted_words
for word in sorted_words:
    print f "{word:<{max_length}} : {word_count[word]}"
"""
# Record the string entered by the user
text = input("Text: ")
# Split the string into a list of words
words = text.split()
# Initialize a dictionary to count the number of occurrences of each word
word_count = {}

# Iterate through the list of words to count occurrences
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Find the length of the longest word for formatted output
max_length = max(len(word) for word in word_count.keys())

# Sort the words alphabetically
sorted_words = sorted(word_count.keys())

# Output each word and its count in the required format
for word in sorted_words:
    print(f"{word:<{max_length}} : {word_count[word]}")