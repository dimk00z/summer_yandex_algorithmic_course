from collections import Counter


def decrypt(word, letter_sequence):
    answer = 0
    word_length, letter_sequence_length = len(word), len(letter_sequence)
    if word_length < letter_sequence_length:
        return answer
    letter_sequence_counter = Counter(letter_sequence)
    word_counter = Counter(word[:letter_sequence_length-1])
    index = 0
    for index in range(letter_sequence_length - 1,
                       word_length):
        word_counter[word[index]] += 1
        if word_counter == letter_sequence_counter:
            answer += 1
        word_counter[word[index - letter_sequence_length + 1]] -= 1
        if word_counter[word[index - letter_sequence_length + 1]] == 0:
            del word_counter[word[index - letter_sequence_length + 1]]
    return answer


with open('input.txt') as file:
    lines = file.readlines()

letter_sequence = lines[1].strip()
word = lines[2].strip()


with open('output.txt', 'w') as file:
    file.write(str(decrypt(word, letter_sequence)))
