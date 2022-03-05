import numpy as np


# Проверка свойства рефлексивности
def check_reflexivity(a, n):
    isReflexive = True
    for i in range(n):
        if a[i][i] == 0:
            isReflexive = False
            return isReflexive
    return isReflexive


# Проверка свойства антирефлексивности
def check_antireflexivity(a, n):
    isAntireflexive = True
    for i in range(n):
        if a[i][i] != 0:
            isAntireflexive = False
            return isAntireflexive
    return isAntireflexive


# Проверка свойства симметричности
def check_symmetry(a, n):
    isSymmetry = True
    t = a.transpose()
    for i in range(n):
        for j in range(n):
            if a[i][j] != t[i][j]:
                isSymmetry = False
                return isSymmetry
    return isSymmetry


# Проверка свойства антисимметричности
def check_antisymmetry(a, n):
    isAntisymmetry = True
    t = a.transpose()
    for i in range(n):
        for j in range(n):
            if i != j and a[i][j] * t[i][j] != 0:
                isAntisymmetry = False
                return isAntisymmetry
    return isAntisymmetry


# Проверка свойства транзитивности
def check_transitivity(a, n):
    isTransitive = True
    t = np.dot(a, a)
    for i in range(n):
        for j in range(n):
            if t[i][j] > 1:
                t[i][j] = 1
            if a[i][j] < t[i][j]:
                isTransitive = False
                return isTransitive
    return isTransitive


def get_equivalence(a, n):
    for i in range(n):
        a[i][i] = 1
        for j in range(n):
            if a[i][j] == 1 and a[i][j] != a[j][i]:
                a[j][i] = 1
    for m in range(n):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if a[i][k] and a[k][j]:
                        a[i][j] = 1
    return construction_of_closures(a, n)


def get_factor_set(a, n):
    s = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if a[i][j] == 1:
                tmp.append(j)
        s.append(tmp)
    return s


def go_to_matrix(s, n):
    cnt = 0
    n = max(br)
    print(n)
    a = []
    for i in range(n):
        a.append([0 for j in range(n)])
    for i in range(len(br) // 2):
        a[br[cnt] - 1][br[cnt + 1] - 1] = 1
        cnt += 2
    return np.array(a)


def go_to_set(a, n):
    s = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                s.append((i, j))
    return s


def print_matrix(a, n):
    cnt = 0
    print('Your matrix:')
    for i in a:
        if (cnt < n):
            print(f'{i}' + ' ')
        else:
            print(f'{i}' + '\n')
            cnt = 0
        cnt += 1


# Вывод бинарного отношения
def print_binary_relation(br, n):
    print('Your binary relation:')
    print('{', end='')
    for i in range(n):
        if i == n - 1:
            print('(' + str(br[i][0] + 1) + ', ' + str(br[i][1] + 1), end=')')
        else:
            print('(' + str(br[i][0] + 1) + ', ' + str(br[i][1] + 1), end='), ')
    print('}')


def print_factor_set(s, n):
    print('{ ', end='')
    for i in range(n):
        print('{', end='')
        m = len(s[i])
        for j in range(m):
            if j == m - 1:
                print(str(s[i][j] + 1), end='')
            else:
                print(str(s[i][j] + 1), end=', ')
        if i == n - 1:
            print('}', end='')
        else:
            print('}', end=', ')
    print(' }')
    

# Проверка матрицы на свойства и их классификация
def testing_of_properties(a, n):
    bl_ref = check_reflexivity(a, n)
    bl_aref = check_antireflexivity(a, n)
    bl_sym = check_symmetry(a, n)
    bl_asym = check_antisymmetry(a, n)
    bl_tran = check_transitivity(a, n)
    print('Properties:')
    if bl_ref:
        print('The binary relation is reflexive')
    else:
        if bl_aref:
            print('The binary relation is antireflexive')
        else:
            print('The binary relation is not reflexive and antireflexive')
    if bl_sym:
        print('The binary relation is symmetry')
    else:
        if bl_asym:
            print('The binary relation is antisymmetry')
        else:
            print('The binary relation is not symmetry and antisymmetry')
    if bl_tran:
        print('The binary relation is transitive')
    else:
        print('The binary relation is not transitive')

    if bl_ref and bl_tran:
        print('The binary relation is quasi-order')
    if bl_ref and bl_sym and bl_tran:
        print('The binary relation is equivalence')
    elif bl_ref and bl_asym and bl_tran:
        print('The binary relation is partial order')
    elif bl_aref and bl_asym and bl_tran:
        print('The binary relation is strict order')
    return choose_mode(a, n)


# Построение замыканий
def construction_of_closures(a, n):
    print_matrix(a, n)

    frel = get_factor_set(a, n)
    print_factor_set(frel, len(frel))

    print('Choose one of the following expression')
    print('Press 1 to get equivalence')
    print('Press 2 to exit')

    bl = int(input())
    if bl == 1:
        get_equivalence(a, n)
    elif bl == 2:
        choose_mode(a, n)
    else:
        print('Incorrect input')
        construction_of_closures(a, n)


# Выбор способа задачи бинарного отношения
def choose_mode(a, n):
    print('Choose mode:')
    print('Press 1 to check matrix properties')
    print('Press 2 to get equivalence')
    print('Press 3 to main menu')
    bl = int(input())
    if bl == 1:
        testing_of_properties(a, n)
    elif bl == 2:
        get_equivalence(a, n)
    elif bl == 3:
        return launch()
    else:
        print('Incorrect output')


# Главное меню
def launch():
    print('Select the way to specify a binary relation:')
    print('Press 1 to enter matrix')
    print('Press 2 to enter binary relation elements')
    print('Press 3 to exit from programm')
    bl = int(input())
    if bl == 1:
        print('Enter the number of verticies')
        n = int(input())
        print('Enter the matrix values')
        a = []
        for i in range(n):
            a.append([int(j) for j in input().split()])
        a = np.array(a)
        print_matrix(a, n)
        print_binary_relation(a, n)
        choose_mode(a, n)
    elif bl == 2:
        print('Enter an even amount of numbers on one line')
        s = input()
        print(s)
        br = [int(i) for i in s.split(' ')]
        if len(br) % 2 != 0:
            print('Incorrect input')
            launch()
        else:
            cnt = 0
            n = max(br)
            a = []
            for i in range(n):
                a.append([0 for j in range(n)])
            for i in range(len(br) // 2):
                a[br[cnt] - 1][br[cnt + 1] - 1] = 1
                cnt += 2
            a = np.array(a)
            br = go_to_set(a, n)
            print_matrix(a, n)
            print_binary_relation(br, len(br))
            choose_mode(a, n)
    elif bl == 3:
        return
    return


launch()
