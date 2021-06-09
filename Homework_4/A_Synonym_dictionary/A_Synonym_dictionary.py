with open('input.txt') as file:
    lines = file.readlines()
synonym_dictionary = {}
for line in lines[1:-1]:
    word1, word2 = line.split()
    synonym_dictionary[word1] = word2
    synonym_dictionary[word2] = word1

with open('output.txt', 'w') as file:
    file.write(synonym_dictionary.get(lines[-1].split()[0]))
