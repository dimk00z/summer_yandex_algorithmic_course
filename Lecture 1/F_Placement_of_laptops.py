

def get_table_sizes(
        Laptop_width_1, Laptop_height_1,
        Laptop_width_2, Laptop_height_2):
    pass


with open('input.txt') as file:
    Laptop_width_1, Laptop_height_1, Laptop_width_2, Laptop_height_2 = map(
        int, file.read().split())
print(Laptop_width_1, Laptop_height_1, Laptop_width_2, Laptop_height_2)
