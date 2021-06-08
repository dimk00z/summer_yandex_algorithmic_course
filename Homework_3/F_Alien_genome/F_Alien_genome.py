'''
WIVYKHBSZLOGOROTIPKLQJWUVXLEZPAGPCDUPUZIDRJTMSHVDUEALKOILER
HYAASSTKFMSSTLQENNEIDYDMTTQPJHOYMYFLTCRQTARJHGFILQYENKPRCQHMEUZKQFZTXJFDBIMJJEKWMHFLKZBCUCCKYSGLVZ
7
'''


def get_coincidence(DNA_1, DNA_2):

    count = 0
    for position in range(len(lines[0])-2):
        current_genome = lines[0][position:position+2]
        count += DNA_2.count(current_genome)
    return str(count)


with open('input.txt') as file:

    lines = file.readlines()
    DNA_1 = lines[0].strip()
    DNA_2 = lines[1].strip()


with open('output.txt', 'w') as file:
    file.write(get_coincidence(DNA_1, DNA_2))
