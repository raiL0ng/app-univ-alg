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


# def create_bin_rel_semigroup():
#     print('Enter elements of binary relation:')
#     s = input()
#     br_list = [i for i in s.split(' ')]
#     n = len(br_list)
#     print('Enter matrices dimension')
#     d = int(input())
#     matrices_list = {}
#     for i in range(n):
#         print(f'Enter matrix values for binary relation \"{br_list[i]}\":')
#         matrix = [list(map(int, input().split())) for i in range(d)]
#         matrix = np.array(matrix).reshape(d, d)
#         matrices_list[br_list[i]] = matrix
    
#     new_set = br_list.copy()
#     l = 2
#     correlations = []
#     while True:
#         combinations = []
#         for i in range(l, l + 1):
#             comb = list(product(''.join([str(elem) for elem in br_list]), repeat=i))
#             combinations += comb
#         for comb in combinations:
#             cur_matrix = matrices_list[comb[0]].copy()
#             word = comb[0]
#             for el_i in range(1, len(comb)):
#                 cur_matrix *= matrices_list[comb[el_i]]
#                 word += comb[el_i]
#             fl = True
#             for key, value in matrices_list.items():
#                 if (np.array_equal(cur_matrix, value)):
#                     fl = False
#                     eq_word = key
#                     break
#             if fl:
#                 matrices_list[word] = cur_matrix
#                 new_set.append(word)
#             else:
#                 correlations.append(str(word + '->' + eq_word))
#         if l == len(br_list):
#             break
#         l += 1
    
#     print("Your semigroup: ")
#     print_set(new_set, len(new_set))
    
#     print("Your semigroup (matrices): ")
#     for key, value in matrices_list.items():
#         print(key, ":\n", value)
    
#     print("Your correlations: ")
#     for el in correlations:
#         print(el)
#     choose_mode()

def create_bin_rel_semigroup():
    print('Enter elements of binary relation:')
    s = input()
    br_list = [i for i in s.split(' ')]
    n = len(br_list)
    print('Enter matrices dimension')
    d = int(input())
    matrices_dict = {}
    for i in range(n):
        print(f'Enter matrix values for binary relation \"{br_list[i]}\":')
        matrix = [list(map(int, input().split())) for i in range(d)]
        matrix = np.array(matrix).reshape(d, d)
        matrices_dict[br_list[i]] = matrix
    
    correlations = {}
    while True:
        new_matrices_dict = {}
        for key1, val1 in matrices_dict.items():
            for key2, val2 in matrices_dict.items():
                new_matrices_dict[key1 + key2] = val1 * val2
        check_set = set(br_list.copy())
        for key1, val1 in new_matrices_dict.items():
            fl = True
            for key2, val2 in matrices_dict.items():
                if (np.array_equal(val1, val2)) and key1 != key2:
                    correlations[key1] = key2 
                    fl = False
                    break
            if fl:
                matrices_dict[key1] = val1
                br_list.append(key1)
        if check_set == set(br_list):
            break
    
    print("Your semigroup: ")
    print_set(br_list, len(br_list))
    
    print("Your semigroup (matrices): ")
    for key, value in matrices_dict.items():
        print(key, ":\n", value)
    
    print("Your correlations: ")
    for key, val in correlations.items():
        print(key + '->' + val)
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


# def create_semigroup_via_set_simply():
#     print('Enter elements of set:')
#     s = input()
#     set_list = [i for i in s.split(' ')]
#     print('Number of elements in presentation:') 
#     k = int(input())
#     presentation = {}
#     for i in range(k):
#         print(f'Enter element ???{i + 1}')
#         key = input()
#         print(f'Enter equivalent of element ???{i + 1}')
#         val = input()
#         presentation[key] = val
#     semigroup = set_list.copy()
#     l = 2
#     while True:
#         combinations = []
#         for i in range(l, l + 1):
#             comb = list(product(''.join([str(elem) for elem in set_list]), repeat=i))
#             for el in comb:
#                 tmp = ''
#                 for i in el:
#                   tmp += str(i)
#                 combinations.append(tmp)
#         check_semgr = semigroup.copy()
#         for comb in combinations:
#             k = 1
#             while True:
#                 tmp = str(comb)
#                 for key, val in presentation.items():
#                     if key in comb and comb not in semigroup:
#                         comb = comb.replace(key, val)
#                 if tmp == comb:
#                     break
#             if comb not in semigroup:
#                 semigroup.append(comb)
#         if set(check_semgr) == set(semigroup):
#             break
#         l += 1

#     print("Your semigroup:")
#     print(semigroup)
#     choose_mode()

def create_semigroup_via_set_simply():
    print('Enter elements of set:')
    s = input()
    set_list = [i for i in s.split(' ')]
    print('Number of elements in presentation:') 
    k = int(input())
    presentation = {}
    for i in range(k):
        print(f'Enter element ???{i + 1}')
        key = input()
        print(f'Enter equivalent of element ???{i + 1}')
        val = input()
        presentation[key] = val
    semigroup = set_list.copy()
    while True:
        new_elements = []
        for el1 in semigroup:
            for el2 in semigroup:
                new_word = el1 + el2
                while True:
                    tmp = str(new_word)
                    for key, val in presentation.items():
                        if key in new_word:
                            new_word = new_word.replace(key, val)
                    if tmp == new_word:
                        break
                new_elements.append(new_word)        
        check_semgr = set(semigroup.copy())
        for el in new_elements:
            if el not in semigroup:
                semigroup.append(el)
        if check_semgr == set(semigroup):
            break
        
    print("Your semigroup:")
    print(semigroup)
    choose_mode()

# ?????????????? ????????
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