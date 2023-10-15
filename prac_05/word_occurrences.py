"""
Word Occurrences
Estimate: 30 minutes
Actual:   22 minutes
"""

text = 'this is a collection of words of nice words this is a fun thing it is'

words_to_count = {}
words = text.split(' ')


for part in words:
    try:
        words_to_count[part] += 1
    except KeyError:
        words_to_count[part] = 1

max_length_word = max(len(word) for word in words_to_count.keys())

word_counts = sorted(list((words_to_count.items())))

for word, count in word_counts:
    print(f"{word:{max_length_word}} : {count}")

