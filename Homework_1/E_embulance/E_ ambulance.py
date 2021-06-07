'''
объясняю 
пусть n - количество квартир на этаже
тогда в одном подъезде m * n квартир 
k2 = (p2 - 1) * m * n + (n2 - 1) * n + альфа
(p2 - 1) * m * n - это сколько у нас квартир в подъездах до нашего
(n2 - 1) * n - это сколько квартир в нашем подъезде в этажах ниже нашего 
альфа - число меньшее чем n обозначающее (от 1 до n вроде)

Всё как тут написано, только альфа - от 0 до n-1, и выражал n, изменяя альфа. 
То есть n=(k2-альфа)/(m*(p2-1) +(n2-1)), перебирал альфа, с целью, чтобы делилось нацело,
и при этом альфа должна быть < n. Альфа - это номер квартиры на этаже, но с нуля. 
Основная идея такая, дальше появляются приколы, когда таких n оказывается несколько например),
тестов нормально так пришлось посмотреть
'''


def get_P1_and_N1(k1, m, k2, p2, n2):
    '''
    m - количество этажей
    k1 - номер квартиры
    k2 - номер пред квартиры
    p2 - подъезд  k2
    n2 - этаж k2 
    '''
    if m == 1 and p2 == 1:
        return 1, 1
    return p1, n1


with open('input.txt') as file:
    k1, m, k2, p2, n2 = map(int, file.read().split())


p1, n1 = get_P1_and_N1(k1, m, k2, p2, n2)

with open('output.txt', 'w') as file:
    file.write(f'{p1} {n1}')
