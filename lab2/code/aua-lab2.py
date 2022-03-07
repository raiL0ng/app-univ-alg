import numpy as np

# Построение матрицы по бинарному отношению
def go_to_matrix(br, n):
    n = -1
    for pair in br:
        tmp = max(pair)
        n = max(tmp, n)
    n += 1
    a = []
    for i in range(n):
        a.append([0 for j in range(n)])
    for pair in br:
        a[pair[0]][pair[1]] = 1
    return np.array(a)


# Построение бинарного отношения по матрице
def go_to_set(a, n):
    s = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                s.append((i, j))
    return s


# Построение эквивалентности
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
    return


# Построение фактор-множества
def get_factor_set(a, n):
    s = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if a[i][j]:
                tmp.append(j)
        if tmp not in s:
            s.append(tmp)
    return s


# Построение системы представителей классов
def get_representative_system(fset, n):
    repsys = []
    for i in range(n):
        repsys.append((min(fset[i]), fset[i]))
    return repsys


# Построение множества общих делителей
def get_set_of_common_dividers(num, exptn):
    dvdrs = []
    for i in range(1, int(num / 2) + 1):
        if num % i == 0 and i not in exptn:
            dvdrs.append(i) 
    if num not in exptn:
        dvdrs.append(num)
    return dvdrs


# Построение списка элементов и их общих делителей
def get_level_list(dvdrs):
    div_dict = {}
    for el in dvdrs:
        dividers_list = []
        for div in dvdrs:
            if el % div == 0:
                dividers_list.append(div)
        div_dict[el] = (dividers_list)
    return div_dict


# Нахождение минимальных элементов
def get_minimal_elem(dvdrs_list, dvdrs):
    minel_len = len(dvdrs_list[dvdrs[0]])
    min_el_list = []
    for key in dvdrs_list:
        tmp = len(dvdrs_list[key])
        if minel_len > tmp:
            minel_len = tmp
    for key in dvdrs_list:
        if minel_len == len(dvdrs_list[key]):
            min_el_list.append([key, dvdrs_list[key]])
    return min_el_list


# Нахождение максимальных элементов
def get_maximal_elem(dvdrs_list, dvdrs):
    maxel_len = len(dvdrs_list[dvdrs[0]])
    max_el_list = []
    for key in dvdrs_list:
        tmp = len(dvdrs_list[key])        
        if maxel_len < tmp:
            maxel_len = tmp
    for key in dvdrs_list:
        if maxel_len == len(dvdrs_list[key]):
            max_el_list.append([key, dvdrs_list[key]])
    return max_el_list


# Нахождение наименьшего элемента
def get_least_elem(min_elems):
    if len(min_elems) == 1:
        return min_elems[0][0]
    else:
        return -1


# Нахождение наибольшего элемента
def get_greatest_elem(max_elems):
    if len(max_elems) == 1:
        return max_elems[0][0]
    else:    
        return -1


# Получение диаграммы Хассе
def get_diagramm_Hasse(dvdrs_list, min_elems):
    diagramm = []
    lvl = 1
    cur_len = len(min_elems[0][1])
    el_and_lvl = []
    for key in dvdrs_list:
        tmp_len = len(dvdrs_list[key])
        if cur_len < tmp_len:
            lvl += 1
            cur_len = tmp_len
        el_and_lvl.append([key, lvl])
    
    tmp_len = len(el_and_lvl)
    for i in range(tmp_len):
        next_lvl = el_and_lvl[i][1] + 1
        prev_lvl = el_and_lvl[i][1] - 1
        arr_next_lvl = []
        arr_prev_lvl = []
        for j in range(tmp_len):
            if el_and_lvl[j][1] == next_lvl:
                arr_next_lvl.append(el_and_lvl[j][0])
            if el_and_lvl[j][1] == prev_lvl:
                arr_prev_lvl.append(el_and_lvl[j][0])
        diagramm.append((el_and_lvl[i][0], el_and_lvl[i][1], arr_prev_lvl, arr_next_lvl))
        i += 1    
    return diagramm


# Вывод матрицы
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
    print('{ ', end='')
    for i in range(n):
        if i == n - 1:
            print('(' + str(br[i][0] + 1) + ', ' + str(br[i][1] + 1), end=')')
        else:
            print('(' + str(br[i][0] + 1) + ', ' + str(br[i][1] + 1), end='), ')
    print(' }')


# Вывод фактор-множества
def print_factor_set(s, n):
    print('Factor-set:')
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
    

# Вывод системы представителей
def print_representative_system(repsys, n):
    print('Class representative system:')
    elems = []
    sets = []
    print('{ ', end='')
    for i in range(n):
        if i == n - 1:
            print('{' + str(repsys[i][0] + 1) + '}', end='')
        else:
            print('{' + str(repsys[i][0] + 1) + '}, ', end='')
    print(' } ' + 'where ', end='')
    for i in range(n):
        if i == n - 1:
            print('{' + str(repsys[i][0] + 1) + '}', end='')
            print(' from ', end='')
            print('{', end='')
            m = len(repsys[i][1])
            for j in range(m):
                if j == m - 1:
                    print(str(repsys[i][1][j] + 1), end='')
                else:
                    print(str(repsys[i][1][j] + 1), end=', ')
            print('}')
        else:
            print('{' + str(repsys[i][0] + 1) + '}', end='')
            print(' from ', end='')
            print('{', end='')
            m = len(repsys[i][1])
            for j in range(m):
                if j == m - 1:
                    print(str(repsys[i][1][j] + 1), end='')
                else:
                    print(str(repsys[i][1][j] + 1), end=', ')
            print('}', end=', ')


#

# Построение диаграммы Хассе (меню)
def construction_of_Hasse_diagramm():
    print('Enter some number')
    num = int(input())
    print('Enter exception numbers, else press 0')
    s = input()
    exptn = [int(i) for i in s.split(' ')]
    dvdrs = get_set_of_common_dividers(num, exptn)
    dvdrs_list = get_level_list(dvdrs)
    
    min_elems = get_minimal_elem(dvdrs_list, dvdrs)
    max_elems = get_maximal_elem(dvdrs_list, dvdrs)
    least_elem = get_least_elem(min_elems)
    greatest_elem = get_greatest_elem(max_elems)
    print('Minimal elements:', end=' ')
    for el in min_elems:
        print(el[0], end=' ')
    print('')
    print('Maximal elements:', end=' ')
    for el in max_elems:
        print(el[0], end=' ')
    print('')
    print('Least element:', end=' ')
    if least_elem == -1:
        print('None')
    else:
        print(least_elem)
    print('Greatest element:', end= ' ')
    if greatest_elem == -1:
        print('None')
    else:
        print(greatest_elem)
    
    print('Do you want to crate Hasse\'s diagramm?)')
    print('(1 - yes, 0 - no)')
    bl = input()
    if bl == '1':
        get_diagramm_Hasse(dvdrs_list, min_elems)
    elif bl == '0':
        return choose_mode()
    else:
        print('Incorrect input!')
        return choose_mode()


# Построение фактор-множества (меню)
def construction_of_factor_sets():
    print('Select the way to specify a binary relation:')
    print('Press 1 to enter matrix')
    print('Press 2 to enter binary relation elements')
    print('Press 3 to exit from programm')
    bl = input()
    if bl == '1':
        print('Enter the number of verticies')
        n = int(input())
        print('Enter the matrix values')
        a = []
        for i in range(n):
            a.append([int(j) for j in input().split()])
        a = np.array(a)

        get_equivalence(a, n)

    elif bl == '2':
        print('Enter an even amount of numbers on one line')
        s = input()
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

            get_equivalence(a, n)
    elif bl == '3':
        return

    print_matrix(a, n)
    br = go_to_set(a, n)
    print_binary_relation(br, len(br))
    
    
    fset = get_factor_set(a, n)
    print_factor_set(fset, len(fset))

    repsys = get_representative_system(fset, len(fset))
    print_representative_system(repsys, len(repsys))

    return choose_mode()

# Главное меню
def choose_mode():
    print('Choose mode:')
    print('Press 1 to get factor-set')
    print('Press 2 to create Hasse\'s diagramm')
    print('Press 3 to create a lattice of concepts')
    print('Press 4 to exit')
    bl = input()
    if bl == '1':
        construction_of_factor_sets()
    elif bl == '2':
        construction_of_Hasse_diagramm()
    elif bl == '3':
        print('dfdf')
    elif bl == '4':
        return
    else:
        print('Incorrect output')
        return choose_mode()

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


choose_mode()
