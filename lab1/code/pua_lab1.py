import numpy as np


def check_reflexivity(a, n):
    fl = True
    for i in range(n):
        if a[i][i] == 0:
            fl = False
    return fl


def check_antireflexivity(a, n):
    fl = True
    for i in range(n):
        if a[i][i] != 0:
            fl = False
    return fl


def check_symmetry(a, n):
    fl = True
    for i in range(n):
        for j in range(n):
            if i <= j:
                continue
            if a[i][j] != a[j][i]:
                fl = False
    return fl


def check_transitivity(a, n):
    fl = True
    t = np.dot(a, a)
    for i in range(n):
        for j in range(n):
            if t[i][j] > 1:
                t[i][j] = 1
            if a[i][j] < t[i][j]:
                fl = False
    return fl


def check_antitransitivity(a, n):
    fl = True
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][k] and a[k][j] and a[i][j]:
                    fl = False
    return fl


def insert_reflexivity(a, n):
    for i in range(n):
        a[i][i] = 1
    print('New matrix:')
    print_matrix(a, n)
    return construction_of_closurs(a, n)


def insert_symmetry(a, n):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and a[i][j] != a[j][i]:
                a[j][i] = 1
    print('New matrix:')
    print_matrix(a, n)
    return construction_of_closurs(a, n)


def insert_transitivity(a, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][k] and a[k][j]:
                    a[i][j] = 1

    print('New matrix:')
    print_matrix(a, n)
    return construction_of_closurs(a, n)


def testing_of_properties(a, n):
    bl_ref = check_reflexivity(a, n)
    bl_aref = check_antireflexivity(a, n)
    bl_sym_asym = check_symmetry(a, n)
    bl_tran = check_transitivity(a, n)
    bl_atran = check_antitransitivity(a, n)
    if bl_ref:
        print('The matrix has the property of reflexivity')
    else:
        if bl_aref:
            print('The matrix has the property of antireflexivity')
        else:
            print('The matrix hasn\'t the property of reflexivity and antireflexivity')
    if bl_sym_asym:
        print('The matrix has the property of symmetry')
    else:
        print('The matrix has the property of antisymmetry')
    if bl_tran:
        print('The matrix has the property of transitivity')
    else:
        if bl_atran:
            print('The matrix has the property of antitransitivity')
        else:
            print('The matrix hasn\'t the property of transitivity and antitransitivity')


    if bl_ref and bl_sym_asym and bl_tran:
        print('So, the matrix has the property of equivalence and quasi-order')
    elif bl_ref and (bl_sym_asym == False) and bl_tran:
        print('So, the matrix has the property partial order')
    elif bl_aref and (bl_sym_asym == False) and bl_tran:
        print('So, the matrix has the property strict order')
    return choose_mode(a, n)


def construction_of_closurs(a, n):
    print('Choose one of the following expression')
    print('Press 1 to complete the reflexivity property')
    print('Press 2 to complete the symmetry property')
    print('Press 3 to complete the transitivity property')
    print('Press 4 to exit')
    bl = int(input())
    if bl == 1:
        insert_reflexivity(a, n)
    elif bl == 2:
        insert_symmetry(a, n)
    elif bl == 3:
        insert_transitivity(a, n)
    elif bl == 4:
        choose_mode(a, n)
    else:
        print('Incorrect input')
        construction_of_closurs(a, n)


def choose_mode(a, n):
    print('Choose mode:')
    print('Press 1 to check matrix properties')
    print('Press 2 to complete matrix properties')
    print('Press 3 to exit with program')
    bl = int(input())
    if bl == 1:
        testing_of_properties(a, n)
    elif bl == 2:
        construction_of_closurs(a, n)
    elif bl == 3:
        return
    else:
        print('Incorrect output')


def print_matrix(a, n):
    cnt = 0
    for i in a:
        if (cnt < n):
            print(f'{i}' + ' ')
        else:
            print(f'{i}' + '\n')
            cnt = 0
        cnt += 1


def launch():
    print('Choose mode:')
    print('Press 1 to enter matrix')
    print('Press 2 to enter binary relation elements')
    bl = int(input())
    if bl == 1:
        print('Enter the number of verticies')
        n = int(input())
        print('Enter the matrix values')
        a = []
        for i in range(n):
            a.append([int(j) for j in input().split()])
        print_matrix(a, n)
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
            print(n)
            a = []
            for i in range(n):
                a.append([0 for j in range(n)])
            for i in range(len(br) // 2):
                a[br[cnt] - 1][br[cnt + 1] - 1] = 1
                cnt += 2
            print_matrix(a, n)
            choose_mode(a, n)
    return
launch()