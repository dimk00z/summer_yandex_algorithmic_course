with open('input.txt') as file:
    lines = file.readlines()
words = {}
for line in lines:
    word_per_line = line.split()
    for word in word_per_line:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
most_frequent_value = max(words.values())
most_frequent_word = sorted([word for word,
                             value in words.items()
                             if value == most_frequent_value])[0]
with open('output.txt', 'w') as file:
    file.write(most_frequent_word)
