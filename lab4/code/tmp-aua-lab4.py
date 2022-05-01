import numpy as np
import math
from itertools import product


def print_set(s, n):
    print('{', end=' ')
    k = 1
    for el in s:
        if k == n:
            print(el, '}')
        else:
            print(str(el) + ',', end=' ')
        k += 1


def create_subsemigroup():
    print('Enter set values:')
    s = input()
    set_list = [i for i in s.split(' ')]
    print('Enter Cayley table values:')
    c_tbl = []
    for i in range(len(set_list)):
      c_tbl.append([j for j in input().split()])     
    print('Enter subset values:')
    s = input()
    subset_list = [i for i in s.split(' ')]
    new_subset = subset_list.copy()
    while True:
        tmp_set = []
        for el1 in set_list:
            for el2 in new_subset:
                tmp_set.append(c_tbl[set_list.index(el2)][set_list.index(el1)])
        subsemigroup = set(new_subset).union(set(tmp_set))
        if (subsemigroup == set(new_subset)):
            break
        else:
            new_subset = list(subsemigroup)
    
    subsemigroup = list(subsemigroup)
    subsemigroup.sort()
    print('Your subsemigroup:', end='')
    print_set(subsemigroup, len(subsemigroup))
    choose_mode()


def create_bin_rel_semigroup():
    print('Enter elements of binary relation:')
    s = input()
    br_list = [i for i in s.split(' ')]
    n = len(br_list)
    print('Enter matrices dimension')
    d = int(input())
    matrices_list = {}
    for i in range(n):
        print(f'Enter matrix values for binary relation \"{br_list[i]}\":')
        matrix = [list(map(int, input().split())) for i in range(d)]
        matrix = np.array(matrix).reshape(d, d)
        matrices_list[br_list[i]] = matrix
    
    new_set = br_list.copy()
    l = 2
    correlations = []
    while True:
        combinations = []
        for i in range(l, l + 1):
            comb = list(product(''.join([str(elem) for elem in br_list]), repeat=i))
            combinations += comb
        for comb in combinations:
            cur_matrix = matrices_list[comb[0]].copy()
            word = comb[0]
            for el_i in range(1, len(comb)):
                cur_matrix *= matrices_list[comb[el_i]]
                word += comb[el_i]
            fl = True
            for key, value in matrices_list.items():
                if (np.array_equal(cur_matrix, value)):
                    fl = False
                    eq_word = key
                    break
            if fl:
                matrices_list[word] = cur_matrix
                new_set.append(word)
            else:
                correlations.append(str(word + '->' + eq_word))
        if l == len(br_list):
            break
        l += 1
    
    print("Your presentations: ")
    for key, value in matrices_list.items():
        print(key, ":\n", value)
    
    print("Your correlations: ")
    for el in correlations:
        print(el)
    choose_mode()

def create_semigroup_via_set():
    print('Enter semigroup values')
    s = input()
    semigroup = [i for i in s.split(' ')]
    n = len(semigroup)
    print('Enter transformation set values:')
    s = input()
    set_list = [i for i in s.split(' ')]
    m = len(set_list)    
    translation_list = []
    for i in range(m):
        print(f"Enter transformation values '{set_list[i]}' via elements of semigroup: ")
        translation = input().split()
        translation_list.append(translation)    

    combinations = []
    for i in range(1, m + 1):
        comb = list(product(''.join([str(elem) for elem in set_list]), repeat=i))
        combinations += comb
    
    ans = {}
    for comb in combinations:
        correlation_list = []
        for i in semigroup:
            semigroup_elem = i
            for generator in comb:
                if semigroup_elem not in semigroup:
                    semigroup_elem = "*"
                else:
                    semigroup_elem = translation_list[set_list.index(generator)] \
                                                     [semigroup.index(semigroup_elem)]
            correlation_list.append(semigroup_elem)
        ans[comb] = correlation_list

    result = {}
    correlations = {}
    for key, value in ans.items():
        if not any(np.array_equal(value, i) for i in result.values()):
            result[key] = value
        else:
            for k, v in result.items():
                if np.array_equal(v, value):
                    correlations[key] = k

    print("Your presentations: ")
    for key, value in result.items():
        print(key, ":\n", value)

    print("Your corelations: ")
    for key, value in correlations.items():
        print(key, "->", value)

    choose_mode()


def create_semigroup_via_set_simply():
    print('Enter elements of set:')
    s = input()
    set_list = [i for i in s.split(' ')]
    print('Number of elements in presentation:') 
    k = int(input())
    presentation = {}
    for i in range(k):
        print(f'Enter element №{i + 1}')
        key = input()
        print(f'Enter equivalent of element №{i + 1}')
        val = input()
        presentation[key] = val
    semigroup = set_list.copy()
    l = 2
    while True:
        combinations = []
        for i in range(l, l + 1):
            comb = list(product(''.join([str(elem) for elem in set_list]), repeat=i))
            for el in comb:
                tmp = ''
                for i in el:
                  tmp += str(i)
                combinations.append(tmp)
        check_semgr = semigroup.copy()
        for comb in combinations:
            k = 1
            while True:
                tmp = str(comb)
                for key, val in presentation.items():
                    if key in comb and comb not in semigroup:
                        comb = comb.replace(key, val)
                if tmp == comb:
                    break
            if comb not in semigroup:
                semigroup.append(comb)
        if set(check_semgr) == set(semigroup):
            break
        l += 1

    print("Your semigroup:")
    print(semigroup)
    choose_mode()

# Главное меню
def choose_mode():
    print('Choose mode:')
    print('Press 1 to create subsemigroup')
    print('Press 2 to create binary relation semigroup')
    print('Press 3 to create semigroup via set')
    print('Press 4 to exit')
    bl = input()
    if bl == '1':
        create_subsemigroup()
    elif bl == '2':
        create_bin_rel_semigroup()
    elif bl == '3':
        create_semigroup_via_set()
    elif bl == '4':
        return
    else:
        print('Incorrect output')
        return choose_mode()


choose_mode()