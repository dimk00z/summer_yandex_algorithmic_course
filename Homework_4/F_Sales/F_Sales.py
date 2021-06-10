
def get_sales(sale_lines) -> str:
    result = []
    customers = {}
    for line in sale_lines:
        customer, product, product_count = line.split()
        if customer not in customers:
            customers[customer] = {}
        if product not in customers[customer]:
            customers[customer][product] = 0
        customers[customer][product] += int(product_count)
    for customer in sorted(customers):
        result.append(f'{customer}:')
        for product, product_count in sorted(customers[customer].items()):
            result.append(f'{product} {product_count}')
    return '\n'.join(result)


with open('input.txt') as file:
    sale_lines = file.readlines()

with open('output.txt', 'w') as file:
    file.write(get_sales(sale_lines))
