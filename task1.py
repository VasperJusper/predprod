# считывание файла и создание списка элементов
inp = list(map(lambda x: x.strip().split('*'), open('space.txt', encoding='utf-8').readlines()))
out = open('space_new.txt', encoding='utf-8', mode="w")
out.write('ShipName*planet*coord_place*direction\n')

# функция "починки" данных


def f(n, m, t, x, y):
    if n > 5:
        a = n + x
    else:
        a = -(n + x) * 4 + t
    if m > 3:
        b = m + t + y
    else:
        b = -(n + y) * m
    return [str(a), str(b)]


for e in inp[1:]:
    # получение переменных для функции
    n = int(e[0].split('-')[1][0])
    m = int(e[0].split('-')[1][1])
    t = len(e[1])
    x, y = map(int, e[3].split())

    # замена нулей
    if e[2].split()[0] == '0' and e[2].split()[1] == '0':
        e[2] = ' '.join(f(n, m, t, x, y))
    elif e[2].split()[0] == '0':
        e[2] = ' '.join([f(n, m, t, x, y)[0], e[2].split()[1]])
    elif e[2].split()[1] == '0':
        e[2] = ' '.join([e[2].split()[0], f(n, m, t, x, y)[1]])
    # запись в файл
    out.write('*'.join(e) + '\n')
