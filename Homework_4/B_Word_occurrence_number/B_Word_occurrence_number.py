with open('input.txt') as file:
    lines = file.readlines()
words = {}
result = []
for line in lines:
    word_per_line = line.split()
    for word in word_per_line:
        if word not in words:
            words[word] = 0
            result.append(0)
        else:
            words[word] += 1
            result.append(words[word])

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, result)))
