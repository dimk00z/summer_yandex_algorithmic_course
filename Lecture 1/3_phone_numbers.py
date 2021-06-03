import re


def satitize_phone(phone_number):
    phone_number = re.sub(
        r'[-()]', '', phone_number.replace(
            '+7', '8').strip())
    if len(phone_number) < 11:
        phone_number = f'8495{phone_number}'
    return phone_number


with open('input.txt') as file:
    phones = [satitize_phone(line) for line in file.readlines()]

reqired_phone = phones[0]
matched_phones = []
for phone in phones[1:]:
    if reqired_phone == phone:
        matched_phones.append('YES\n')
    else:
        matched_phones.append('NO\n')

with open('output.txt', 'w') as file:
    file.writelines(matched_phones)
