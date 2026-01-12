"""
Day 2: Text Analysis - Working with Multiple Documents
Name: Aly Khaled
Date: January 12, 2026
Goal: Learn to compare and analyze multiple texts
"""

# ==========================================
# Exercise 1: Working with Multiple Documents (30 min)
# ==========================================

documents = [
    "Python is a great programming language for machine learning",
    "Machine learning requires understanding of Python and mathematics",
    "Natural language processing is a subset of machine learning"
]

print("=== Exercise 1: Multi-Document Analysis ===\n")

# TODO 1.1: Count total words across all documents
print("--- TODO 1.1: Total Word Count ---")
total_word_count = 0

for i, doc in enumerate(documents, 1):
    words = doc.split()
    word_count = len(words)
    total_word_count += word_count
    print(f"Document {i}: {word_count} words")

print(f"Total words across all documents: {total_word_count}\n")

# TODO 1.2: Find documents that contain the word "machine"
print("--- TODO 1.2: Find Documents with 'machine' ---")

def find_documents_with_word(word_to_find, document_list):
    found_documents = []
    target_word_lower = word_to_find.lower()
    
    for doc in document_list:
        if target_word_lower in doc.lower():
            found_documents.append(doc)
    
    return found_documents

search_word = "machine"
result_list = find_documents_with_word(search_word, documents)

print(f"Documents containing '{search_word}':")
for i, doc in enumerate(result_list, 1):
    print(f"  {i}. {doc}")
print(f"Total: {len(result_list)} documents\n")

# TODO 1.3: Find the longest document (by word count)
print("--- TODO 1.3: Longest Document ---")

def find_longest_document(doc_list):
    max_word_count = 0
    longest_doc_index = -1
    longest_doc = ""
    
    for index, doc_content in enumerate(doc_list):
        words = doc_content.split()
        current_word_count = len(words)
        
        if current_word_count > max_word_count:
            max_word_count = current_word_count
            longest_doc_index = index
            longest_doc = doc_content
    
    return longest_doc_index, max_word_count, longest_doc

index, count, content = find_longest_document(documents)

print(f"Longest document (Index {index}):")
print(f"  Word count: {count}")
print(f"  Content: \"{content}\"\n")

# TODO 1.4: Create a list of ALL unique words across all documents
print("--- TODO 1.4: All Unique Words ---")

unique_words = set()

for doc in documents:
    words = doc.lower().split()
    for word in words:
        unique_words.add(word)

unique_words_sorted = sorted(unique_words)

print(f"Total unique words: {len(unique_words_sorted)}")
print(f"Unique words: {unique_words_sorted}")

# ==========================================
# Exercise 2: Text Comparison (30 min)
# ==========================================

text1 = "I love Python programming and machine learning"
text2 = "I enjoy Python coding and deep learning"

print("\n=== Exercise 2: Comparing Two Texts ===\n")

# TODO 2.1: Find words that appear in BOTH texts
print("--- TODO 2.1: Common Words ---")

def find_common_words(text1, text2):
    words_set1 = set(text1.lower().split())
    words_set2 = set(text2.lower().split())
    common_words = words_set1.intersection(words_set2)
    return common_words

common = find_common_words(text1, text2)

print(f"Text 1: \"{text1}\"")
print(f"Text 2: \"{text2}\"")
print(f"\nWords in BOTH texts: {sorted(common)}")
print(f"Total: {len(common)} common words\n")

# TODO 2.2: Find words that appear ONLY in text1
print("--- TODO 2.2: Words Only in Text 1 ---")

def find_unique_words_text1(text1, text2):
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    words_only_in_text1 = set1.difference(set2)
    return words_only_in_text1

unique_to_text1 = find_unique_words_text1(text1, text2)

print(f"Words ONLY in text1: {sorted(unique_to_text1)}")
print(f"Total: {len(unique_to_text1)} unique words\n")

# TODO 2.3: Find words that appear ONLY in text2
print("--- TODO 2.3: Words Only in Text 2 ---")

def find_unique_words_text2(text1, text2):
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    words_only_in_text2 = set2.difference(set1)
    return words_only_in_text2

unique_to_text2 = find_unique_words_text2(text1, text2)

print(f"Words ONLY in text2: {sorted(unique_to_text2)}")
print(f"Total: {len(unique_to_text2)} unique words\n")

# TODO 2.4: Calculate similarity percentage
print("--- TODO 2.4: Similarity Percentage ---")

def calculate_similarity_percentage(text1, text2):
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    
    common_words = set1.intersection(set2)
    total_unique_words = set1.union(set2)
    
    num_common = len(common_words)
    num_total_unique = len(total_unique_words)
    
    if num_total_unique == 0:
        return 0.0
    
    similarity_score = (num_common / num_total_unique) * 100
    return round(similarity_score, 2)

similarity = calculate_similarity_percentage(text1, text2)

print(f"Text 1: \"{text1}\"")
print(f"Text 2: \"{text2}\"")
print(f"\nCommon words: {len(find_common_words(text1, text2))}")
print(f"Total unique: {len(set(text1.lower().split()) | set(text2.lower().split()))}")
print(f"Similarity: {similarity}%\n")

# ==========================================
# Exercise 3: Text Statistics Extractor (30 min)
# ==========================================

article = """
Machine learning is transforming technology. It powers recommendation systems.
Companies use machine learning for predictions. Machine learning needs data.
Good data quality is essential for machine learning success.
"""

print("\n=== Exercise 3: Article Statistics ===\n")

# TODO 3.1: Split into sentences
# Hint: Split by period, clean up empty strings


# TODO 3.2: Calculate average words per sentence


# TODO 3.3: Find the most common word (excluding common words like "is", "for", "the")
# Hint: Create a list of words to exclude, then count frequencies


# TODO 3.4: Count how many times "machine learning" appears (as a phrase, not separate words)
# Hint: Search for "machine learning" in the lowercased text


print("\n=== Day 2 Complete! ===")
