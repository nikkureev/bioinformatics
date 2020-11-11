pep_dict = {'pep_1': ['tax_1', 'genus_1', 'species_1'],
            'pep_2': ['tax_1', 'genus_1', 'species_2'],
            'pep_3': ['tax_1', 'genus_2', 'species_3'],
            'pep_4': ['tax_1', 'genus_2', 'species_4'],
            'pep_5': ['tax_2', 'genus_3', 'species_5']}


def tree_adapter(iter_object, pep_id, n, l, pep_name):
    if n == l - 1:
        iter_object[pep_id[-1]] = [pep_name]
    else:
        if pep_id[n] in iter_object.keys():
            tree_adapter(iter_object[pep_id[n]], pep_id, n + 1, l, pep_name) 
        else:
            iter_object[pep_id[n]] = {}
            tree_adapter(iter_object[pep_id[n]], pep_id, n + 1, l, pep_name) 
    
    
def taxonomy_estimation(pep_dict):
    tree = {}
    for i, v in pep_dict.items():
        tree_adapter(tree, v, 0, len(v), i)
    return tree


def newik_converter(tree_dict):
    newik_tree = []
    for v in tree_dict.values():
        if type(v) == list:
            newik_tree.append(v)
        else:
            newik_tree.append(newik_converter(v))
    return newik_tree

wood = taxonomy_estimation(pep_dict)
result = str(newik_converter(wood)).replace("{", "(").replace("}", "):0.3").replace("[", "(").replace("]", "):0.3")
print('newik format:', result)
