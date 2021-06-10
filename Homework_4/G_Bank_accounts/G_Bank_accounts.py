def update_bank_account(bank_accounts, customer_name, money):
    if customer_name in bank_accounts:
        bank_accounts[customer_name] += money
    else:
        bank_accounts[customer_name] = money


def get_balance(bank_accounts, customer_name):
    return 'ERROR'


def do_bank_operation(banks_operations) -> str:
    result = []
    bank_accounts = {}
    for bank_operation in banks_operations:
        bank_operation = bank_operation.split()
        if bank_operation[0] == 'BALANCE':
            result.append(get_balance(
                bank_accounts, customer_name=bank_operation[1]))
            continue
        if bank_operation[0] == 'INCOME':
            # добавить расчет
            continue
        customer_name = bank_operation[1]
        if bank_operation[0] == 'DEPOSIT':
            update_bank_account(bank_accounts, customer_name,
                                bank_operation[2])
            continue
        if bank_operation[0] == 'WITHDRAW':
            update_bank_account(bank_accounts, customer_name,
                                -1*bank_operation[2])
            continue
        if bank_operation[0] == 'TRANSFER':
            update_bank_account(bank_accounts, bank_operation[2],
                                bank_operation[3])
            update_bank_account(bank_accounts, customer_name,
                                -1*bank_operation[2])
            continue
    print(bank_accounts)
    #     customer, product, product_count = line.split()
    #     if customer not in customers:
    #         customers[customer] = {}
    #     if product not in customers[customer]:
    #         customers[customer][product] = 0
    #     customers[customer][product] += int(product_count)
    # for customer in sorted(customers):
    #     result.append(f'{customer}:')
    #     for product, product_count in sorted(customers[customer].items()):
    #         result.append(f'{product} {product_count}')
    return '\n'.join(result)


with open('input.txt') as file:
    banks_operations = file.readlines()

with open('output.txt', 'w') as file:
    file.write(do_bank_operation(banks_operations))
