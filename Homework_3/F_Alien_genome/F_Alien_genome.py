'''
WIVYKHBSZLOGOROTIPKLQJWUVXLEZPAGPCDUPUZIDRJTMSHVDUEALKOILER
HYAASSTKFMSSTLQENNEIDYDMTTQPJHOYMYFLTCRQTARJHGFILQYENKPRCQHMEUZKQFZTXJFDBIMJJEKWMHFLKZBCUCCKYSGLVZ
7
'''


def get_coincidence(DNA_A, DNA_B):
    set_b = set()
    for position in range(len(DNA_B)-1):
        set_b.add(DNA_B[position:position+2])
    count = 0
    for position in range(len(DNA_A)-1):
        current_genome = DNA_A[position:position+2]
        if current_genome in set_b:
            count += 1
    return str(count)


with open('input.txt') as file:

    lines = file.readlines()
    DNA_A = lines[0].strip()
    DNA_B = lines[1].strip()


with open('output.txt', 'w') as file:
    file.write(get_coincidence(DNA_A, DNA_B))
