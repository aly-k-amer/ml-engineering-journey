"""
Day 2 Warm-up: Quick Review
Name: Aly Khaled
"""

# Warm-up Exercise: Clean and analyze this text
text = "Python is AMAZING! I love Python programming. Python is powerful."

# TODO 1: Convert to lowercase and remove punctuation
import string
lowercase_text = text.lower()
no_punctuation = ""
for char in lowercase_text:
  if char not in string.punctuation:
    no_punctuation += char
print("No Punctiation: ", no_punctuation)
# TODO 2: Count how many times each word appears
word_list = text.lower().split()
word_count = {}
for word in word_list:
  clean_word = word.strip('.,?!')
  if clean_word in word_count:
    word_count[clean_word] += 1
  else:
    word_count[clean_word] = 1
print("Word frequencies:", word_count)
# TODO 3: Print the most common word
sorted_words = sorted(
  word_count.items(),
  key = lambda x: x[1],
  reverse = True
)
print("Most Common Word: ",sorted_words[:1])

print("Warm-up complete!")
