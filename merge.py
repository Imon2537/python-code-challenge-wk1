# this funcs combines two dictionaries and mergers them into one
dict1 = {
    'car': 'subaru, ',
    'model': 'forester, '
}
dict2 = {
    'car': 'rolls royce',
    'model' : "cullinan"
}
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

merge = merge_dicts(dict1, dict2)
print(merge)
