def update_bank_account(bank_accounts, customer_name, money):
    if customer_name in bank_accounts:
        bank_accounts[customer_name] += money
    else:
        bank_accounts[customer_name] = money


def get_balance(bank_accounts, customer_name):
    if customer_name in bank_accounts:
        return str(bank_accounts[customer_name])
    return 'ERROR'


def income(bank_accounts, percents):
    for customer_name in bank_accounts:
        if bank_accounts[customer_name] > 0:
            bank_accounts[customer_name] = int(
                bank_accounts[customer_name] + (bank_accounts[
                    customer_name] * percents/100))


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
            income(bank_accounts, percents=int(bank_operation[1]))
            continue
        customer_name = bank_operation[1]
        if bank_operation[0] == 'DEPOSIT':
            update_bank_account(bank_accounts, customer_name,
                                int(bank_operation[2]))
            continue
        if bank_operation[0] == 'WITHDRAW':
            update_bank_account(bank_accounts, customer_name,
                                -1*int(bank_operation[2]))
            continue
        if bank_operation[0] == 'TRANSFER':
            update_bank_account(bank_accounts, bank_operation[2],
                                int(bank_operation[3]))
            update_bank_account(bank_accounts, customer_name,
                                -1*int(bank_operation[3]))

    return '\n'.join(result)


with open('input.txt') as file:
    banks_operations = file.readlines()

with open('output.txt', 'w') as file:
    file.write(do_bank_operation(banks_operations))
