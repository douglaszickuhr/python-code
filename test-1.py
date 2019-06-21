def group_by_owners(files):
    my_dict = dict()
    for key, val in files.items():
        if val not in my_dict:
            my_dict.setdefault(val, list()).append(key)
        else:
            my_dict[val].append(key)
    return my_dict


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(group_by_owners(files))
