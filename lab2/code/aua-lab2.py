import matplotlib.pyplot as plt

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
def get_minimal_elem(slices_list, is_div_mode, set_x, strt=0):
    if is_div_mode:
        minel_len = len(slices_list[set_x[0]])
        min_el_list = []
        for key in slices_list:
            tmp = len(slices_list[key])
            if minel_len > tmp:
                minel_len = tmp
        for key in slices_list:
            if minel_len == len(slices_list[key]):
                min_el_list.append(key)
        return min_el_list
    else:
        min_el_list = []
        for i in range(strt, len(slices_list)):
            fl = True
            for j in range(strt, len(slices_list[i])):
                if slices_list[i][j] != 0 and i != j:
                    fl = False
            if fl:
                min_el_list.append(set_x[i])
        return min_el_list


# Нахождение максимальных элементов
def get_maximal_elem(slices_list, is_div_mode, set_x, strt=0):
    if is_div_mode:
        maxel_len = len(slices_list[set_x[0]])
        max_el_list = []
        for key in slices_list:
            tmp = len(slices_list[key])        
            if maxel_len < tmp:
                maxel_len = tmp
        for key in slices_list:
            if maxel_len == len(slices_list[key]):
                max_el_list.append(key)
        return max_el_list
    else:
        max_el_list = []
        for i in range(strt, len(slices_list)):
            fl = True
            for j in range(strt, len(slices_list[i])):
                if slices_list[j][i] != 0 and i != j:
                    fl = False
            if fl:
                max_el_list.append(set_x[i])
        return max_el_list


# Нахождение наименьшего элемента
def get_least_elem(min_elems):
    if len(min_elems) == 1:
        return min_elems[0]
    else:
        return -1


# Нахождение наибольшего элемента
def get_greatest_elem(max_elems):
    if len(max_elems) == 1:
        return max_elems[0]
    else:    
        return -1


# Получение диаграммы Хассе
def get_diagramm_Hasse(dvdrs_list, is_div_mode, set_x):
    diagramm = []
    lvl = 0
    el_and_lvl = []
    if is_div_mode:
        while dvdrs_list != {}:
            min_elems = get_minimal_elem(dvdrs_list, True, set_x)
            lvl += 1  
            for el in min_elems:
                set_x.remove(el)
                el_and_lvl.append([el, lvl])
                del dvdrs_list[el]
                for key in dvdrs_list:
                    if el in dvdrs_list[key]:  
                        dvdrs_list[key].remove(el)
    else:
        k = 0
        while k != len(set_x):
            min_elems = get_minimal_elem(dvdrs_list, False, set_x, k)
            lvl += 1
            for el in min_elems:
                el_and_lvl.append([el, lvl])
                k += 1
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
        diagramm.append(( el_and_lvl[i][0], el_and_lvl[i][1]
                        , arr_prev_lvl, arr_next_lvl) )
    return diagramm
        


# Нахождение системы замыкания
def get_closure_system(objs, attrs, a, ob_len, at_len):
    set_z = [objs]
    for i in range(at_len):
        cur_slice = []
        for j in range(ob_len):
            if a[j][i]:
                cur_slice.append(objs[j])
            else:
                continue
        for subset in set_z:
            tmp = list(set(cur_slice) & set(subset))
            tmp.sort()
            if tmp not in set_z:
                set_z.append(tmp)
    return set_z


# Нахождение решетки концептов
def get_lattice_of_concepts(set_z, objs, attrs, a, ob_len, at_len):
    set_iso = {}
    for i in range(ob_len):
        cur_slice = []
        for j in range(at_len):
            if a[i][j]:
                cur_slice.append(attrs[j])
        set_iso[objs[i]] = cur_slice
    set_isomorph = []
    for el in set_z:
        tmp = set([])
        for i in range(len(el)):
            if i == 0:
                tmp = set(set_iso[el[i]])
            else:
                tmp = tmp & set(set_iso[el[i]])
        if el == []:
            set_isomorph.append([el, attrs])
        else:
            tmp = list(tmp)
            tmp.sort()
            set_isomorph.append([el, tmp])
    
    return set_isomorph


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


def print_Hasse_diagramm(data, is_div_mode, set_list, set_x):
    plt.title("Диаграмма Хассе")
    
    # Построение ключ: уровень, значение: все элементы
    # на текущем уровне
    el_and_lvl = {}    
    for hasse_el in data:
        el_and_lvl[hasse_el[1]] = []
    for hasse_el in data:
        el_and_lvl[hasse_el[1]].append(hasse_el[0])
    
    lim = len(el_and_lvl) * 2
    plt.xlim(0, lim)
    plt.ylim(0, lim)
    x = {}
    y = {}
    # Нахождение координат элементов
    for key in el_and_lvl:
        step = len(el_and_lvl[key]) + 1
        cur = lim / step
        step = cur
        for el in el_and_lvl[key]:
            x[el] = cur
            y[el] = float(key)
            cur += step
    box = { 'facecolor':'cyan',
            'edgecolor': 'black',
            'boxstyle': 'circle',
            'linewidth': '2' }

    if is_div_mode:
        lines = []
        for elem in data:
            tmp = []
            for i in range(len(elem[3])):
                if elem[3][i] % elem[0] == 0:
                    tmp.append(elem[3][i])
            for el in tmp:
                lines.append([elem[0], el])
        
        for line in lines:
            plt.plot([x[line[0]], x[line[1]]], [y[line[0]], y[line[1]]], 'r')
        
        for key in x:
            plt.text( x[key], y[key], str(key),
                      bbox = box,
                      horizontalalignment = 'center',
                      color = 'black',
                      fontsize = 9 )
        plt.show()    
    else:
        lines = []
        for i in range(len(set_list)):
            for j in range(len(set_list[i])):
                if set_list[i][j] and j < i:
                    for el in data[i][2]:
                        if set_x[j] == el:
                            lines.append([data[i][0], set_x[j]])
        for line in lines:
            plt.plot([x[line[0]], x[line[1]]], [y[line[0]], y[line[1]]], 'r')
        
        for key in x:
            plt.text( x[key], y[key], key,
                      bbox = box,
                      horizontalalignment = 'center',
                      color = 'black',
                      fontsize = 9 )
        plt.show()

# Построение решетки концептов (меню)
def construction_lattice_of_concepts():
    print('Enter set of objects:')
    s = input()
    objs = [i for i in s.split(' ')]
    print('Enter set of attributes:')
    s = input()
    attrs = [i for i in s.split(' ')]
    print('Enter a binary relation matrix:')
    a = []
    ob_len = len(objs)
    at_len = len(attrs)
    for i in range(ob_len):
        tmp = input().split()
        for j in range(len(tmp)):
            tmp[j] = int(tmp[j])
        a.append(tmp)
    print('Closure system:', end=' ')
    set_z = get_closure_system(objs, attrs, a, len(objs), len(attrs))
    print(set_z)
    print('Lattice of concepts:', end= ' ')
    set_isomorph = get_lattice_of_concepts(set_z, objs, attrs, a, ob_len, at_len)
    print(set_isomorph)

    return choose_mode()
    
# Построение диаграммы Хассе (меню)
def construction_of_Hasse_diagramm():
    print('Select the way:')
    print('Press 1 to enter some number')
    print('Press 2 to enter set and matrix')
    bl = input()
    if bl == '1':
        print('Enter some number')
        num = int(input())
        print('Enter exception numbers, else press 0')
        s = input()
        exptn = [int(i) for i in s.split(' ')]
        dvdrs = get_set_of_common_dividers(num, exptn)

        dvdrs_list = get_level_list(dvdrs)

        min_elems = get_minimal_elem(dvdrs_list, True, dvdrs)
        max_elems = get_maximal_elem(dvdrs_list, True, dvdrs)
        least_elem = get_least_elem(min_elems)
        greatest_elem = get_greatest_elem(max_elems)
        print('Minimal elements:', end='{ ')
        for el in min_elems:
            print(el, end=' ')
        print('}')
        print('Maximal elements:', end='{ ')
        for el in max_elems:
            print(el, end=' ')
        print('}')
        print('Least element:', end=' ')
        if least_elem == -1:
            print('None')
        else:
            print('{',least_elem, '}')
        print('Greatest element:', end= ' ')
        if greatest_elem == -1:
            print('None')
        else:
            print('{', greatest_elem, '}')

        print('Do you want to create Hasse\'s diagramm?)')
        print('(1 - yes, 0 - no)')
        bl = input()
        if bl == '1':
            diagramm = get_diagramm_Hasse(dvdrs_list, True, dvdrs)
            print(diagramm)
            print_Hasse_diagramm(diagramm, True, dvdrs_list, dvdrs)
        elif bl == '0':
            return choose_mode()
        else:
            print('Incorrect input!')

    elif bl == '2':
        print('Enter some set of elements')
        s = input()
        br = [i for i in s.split(' ')]

        print('Enter the matrix values')
        a = []
        for i in range(len(br)):
            a.append([int(j) for j in input().split()])
        min_elems = get_minimal_elem(a, False, br)
        max_elems = get_maximal_elem(a, False, br)
        least_elem = get_least_elem(min_elems)
        greatest_elem = get_greatest_elem(max_elems)
        print('Minimal elements:', end='{ ')
        for el in min_elems:
            print(el, end=' ')
        print('}')
        print('Maximal elements:', end=' ')
        for el in max_elems:
            print(el, end=' ')
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

        print('Do you want to create Hasse\'s diagramm?)')
        print('(1 - yes, 0 - no)')
        bl = input()
        if bl == '1':
            diagramm = get_diagramm_Hasse(a, False, br)
            print_Hasse_diagramm(diagramm, False, a, br)
        elif bl == '0':
            return choose_mode()
        else:
            print('Incorrect input!')
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

        get_equivalence(a, n)

    elif bl == '2':
        print('Enter an even amount of numbers on one line')
        s = input()
        br = [int(i) for i in s.split(' ')]
        if len(br) % 2 != 0:
            print('Incorrect input')
            choose_mode()
        else:
            cnt = 0
            n = max(br)
            a = []
            for i in range(n):
                a.append([0 for j in range(n)])
            for i in range(len(br) // 2):
                a[br[cnt] - 1][br[cnt + 1] - 1] = 1
                cnt += 2

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
        construction_lattice_of_concepts()
    elif bl == '4':
        return
    else:
        print('Incorrect output')
        return choose_mode()


choose_mode()