import numpy as np
import math
from itertools import product


INF = 100000


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
    subset = [i for i in s.split(' ')]
    subset_copy = subset.copy()
    for k in range(0, INF):
        tmp_sub = []
        for i in subset_copy:
            for j in subset:
                tmp_sub.append(c_tbl[subset_copy.index(i)][subset.index(j)])
        subsemigroup = set(subset_copy).union(set(tmp_sub))
    
    subsemigroup = list(subsemigroup)
    subsemigroup.sort()
    print('Your subsemigroup:', subsemigroup)
    choose_mode()


def find_correlation(ans):
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


def create_bin_rel_semigroup():
    print('Enter number of binary relations:')
    n = int(input())
    print('Enter matrices dimension')
    d = int(input())
    matrices_list = {}
    for i in range(1, n + 1):
        print(f'Enter matrix values for binary relation №{i}:')
        matrix = [list(map(int, input().split())) for i in range(d)]
        matrix = np.array(matrix).reshape(d, d)
        matrices_list[str(i)] = matrix
    
    combinations = []
    for i in range(1, n + 1):
        comb = list(product(''.join([str(elem) for elem in range(1, n + 1)]), repeat=i))
        combinations += comb

    for comb in combinations:
        cur_matrix = matrices_list[comb[0]].copy()
        word = comb[0]
        for comb_i in range(1, len(comb)):
            cur_matrix *= matrices_list[comb[comb_i]]
            word += comb[comb_i]
        matrices_list[word] = cur_matrix
    
    find_correlation(matrices_list)
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

    find_correlation(ans)
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