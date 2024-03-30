# считывание файла и создание списка элементов
inp = list(map(lambda x: x.strip().split('*'), open('space.txt', encoding='utf-8').readlines()))
out = open('space_new.txt', encoding='utf-8', mode="w")

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
    coords = 0

    if e[2].split()[0] == '0' and e[2].split()[1] == '0':
        coords = f(n, m, t, x, y)
    elif e[2].split()[0] == '0':
        coords = f(n, m, t, x, y)[0], e[2].split()[1]
    elif e[2].split()[1] == '0':
        coords = e[2].split()[0], f(n, m, t, x, y)[1]

    if coords and e[0].split('-')[0][-1] == 'V':
        out.write(f"{e[1]} - ({coords[0]}, {coords[1]})\n")
