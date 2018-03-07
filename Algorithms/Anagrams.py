# Group strings that are anagram of each other into a list without 
# duplicate maintaining the order (stable)

# INPUT
# ['xxy', 'cab', 'bca', 'cab', 'bac', 'dash', 'shad']
# 
# OUTPUT
# [
#   ['xxy'],
#   ['cab', 'bca’, 'bac'],
#   ['dash', 'shad']
# ]

def anagrams_list(l):

    count = 0
    dict_occ = set()
    dict_output_i = {}
    output = []

    for s in l:
        if s in dict_occ:
            continue
        
        dict_occ.add(s)
        sorted_s = "".join(sorted(s))

        if sorted_s in dict_output_i:
            output[dict_output_i[sorted_s]].append(s)
        else:
            dict_output_i[sorted_s] = count
            output.append([s])
            count += 1

    return output

# l = ['xxy', 'cab', 'bca', 'cab', 'bac', 'dash', 'shad']
# print(anagrams_list(l))