l = []

file = open('input', 'r')
for line in file:
    l.append(line)
file.close()

for i in range(len(l)):
    l[i] = l[i][:-1]


def cas1(l):
    res1 = 0
    res2 = 0
    for i in range(len(l)):
        if (res1 != 0):
            break;
        nb1 = int(l[i])
        for j in range(i, len(l), 1):
            nb2 = int(l[j])
            if( nb1 + nb2 == 2020):
                res1 = nb1
                res2 = nb2
                break;
    res = res1 * res2
    return res

print(cas1(l))


def cas2(l):
    res1 = 0
    res2 = 0
    res3 = 0

    for i in range(len(l)):
        if (res1 != 0):
            break;
        nb1 = int(l[i])
        for j in range(i, len(l), 1):
            nb2 = int(l[j])
            if( nb1 + nb2 <= 2020):
                for k in range(j, len(l), 1):
                    nb3 = int(l[k])
                    if( nb1 + nb2 + nb3 == 2020):
                            res1 = nb1
                            res2 = nb2
                            res3 = nb3
    res = res1 * res2 * res3
    return res

print(cas2(l))