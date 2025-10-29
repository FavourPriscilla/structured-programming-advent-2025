from collections import Counter

# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Use Counter to count occurrences of each word
word_count = Counter(words)

# Display the result
print("\nWord Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")
