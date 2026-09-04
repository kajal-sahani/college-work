"""
Lab Exercise 3 - Program 3
Frequency Counter using Dictionaries
Student: Kajal
"""

print("=" * 50)
print("        FREQUENCY COUNTER")
print("=" * 50)

text = input("\nEnter a sentence or paragraph:\n")

# Convert to lowercase and split into words
words = text.lower().split()

# Count frequency using dictionary
freq = {}
for word in words:
    # Remove basic punctuation
    word = word.strip(".,!?;:\"'()[]{}")
    if word:
        freq[word] = freq.get(word, 0) + 1

print("\n----- Word Frequency -----")
print(f"{'Word':<20}{'Count':>8}")
print("-" * 30)

# Sort by frequency (descending)
for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{word:<20}{count:>8}")

print("=" * 50)
