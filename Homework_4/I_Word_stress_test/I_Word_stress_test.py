def check_errors(
        dictionary, sentence):
    errors = 0
    for word in sentence:
        lower_form = word.lower()
        if lower_form in dictionary and \
            word not in dictionary[lower_form] \
                or len([letter for letter in word if letter.isupper()]) != 1:
            errors += 1
    return str(errors)


with open('input.txt') as file:
    lines = file.readlines()
dictionary = {}
dictionany_length = int(lines[0])
if dictionany_length:
    for word in lines[1:-1]:
        word = word.strip()
        lower_form = word.lower()
        if lower_form not in dictionary:
            dictionary[lower_form] = set()
        dictionary[lower_form].add(word)
sentence = lines[-1].split()


with open('output.txt', 'w') as file:
    file.write(check_errors(
        dictionary, sentence))
