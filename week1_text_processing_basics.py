"""
Day 1: Text Processing Fundamentals
Goal: Understand text manipulation without NLP libraries
Name: Aly Khaled
Date: January 4, 2026
"""

# Exercise 1: Basic text cleaning (15 min)
text = """
Hello World! This is a Sample Text with MIXED case, 
punctuation... and some     extra spaces. 
Email me at test@example.com or visit https://example.com
"""

print("=== Exercise 1: Basic Text Cleaning ===")
# TODO: Convert to lowercase
lowercase_text = text.lower()
print("Lowercase:", lowercase_text[:50], "...")

# TODO: Remove punctuation
import string
no_punctuation = ""
for char in lowercase_text:
    if char not in string.punctuation:
        no_punctuation += char
print("No punctuation:", no_punctuation[:50], "...")

# TODO: Remove extra spaces
cleaned_text = " ".join(no_punctuation.split())
print("Cleaned:", cleaned_text[:50], "...")

# TODO: Split into words (tokenization)
words = cleaned_text.split()
print(f"Total words: {len(words)}")
print("First 10 words:", words[:10])

print("\n=== Exercise 2: Word Frequency Counter ===")
sample_text = """
machine learning is amazing. deep learning is a subset of machine learning.
natural language processing uses machine learning for text analysis.
"""

# TODO: Create a dictionary counting how many times each word appears
word_count = {}
words_list = sample_text.lower().split()
for word in words_list:
    # Remove punctuation from word
    clean_word = word.strip('.,!?')
    if clean_word in word_count:
        word_count[clean_word] += 1
    else:
        word_count[clean_word] = 1

print("Word frequencies:", word_count)

# TODO: Find the 5 most common words
# Sort by count (descending)
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print("Top 5 words:", sorted_words[:5])

# TODO: Calculate what percentage of words appear only once
words_appearing_once = sum(1 for count in word_count.values() if count == 1)
total_unique_words = len(word_count)
percentage = (words_appearing_once / total_unique_words) * 100
print(f"Words appearing once: {percentage:.1f}%")

print("\n=== Exercise 3: Simple Text Statistics ===")
sentences = [
    "This is a short sentence.",
    "This is a much longer sentence with many more words in it.",
    "Short one."
]

# TODO: Calculate average sentence length (in words)
total_words = 0
for sentence in sentences:
    words_in_sentence = len(sentence.split())
    total_words += words_in_sentence
average_length = total_words / len(sentences)
print(f"Average sentence length: {average_length:.1f} words")

# TODO: Find the longest sentence
longest = ""
for sentence in sentences:
    if len(sentence.split()) > len(longest.split()):
        longest = sentence
print(f"Longest sentence: {longest}")

# TODO: Count total unique words across all sentences
all_words = set()
for sentence in sentences:
    words = sentence.lower().replace('.', '').split()
    for word in words:
        all_words.add(word)
print(f"Total unique words: {len(all_words)}")

# TODO: Identify words that appear in multiple sentences
word_sentence_count = {}
for sentence in sentences:
    words = set(sentence.lower().replace('.', '').split())
    for word in words:
        if word in word_sentence_count:
            word_sentence_count[word] += 1
        else:
            word_sentence_count[word] = 1

repeated_words = [word for word, count in word_sentence_count.items() if count > 1]
print(f"Words in multiple sentences: {repeated_words}")

print("\n=== Day 1 Complete! ===")
