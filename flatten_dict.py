my_dict = {"a":1,
           "b":2,
           "c":{"c1":[{"c11":1,"c12":2,"c13":3},
                      {"c21":1,"c22":2,"c23":3}],
                "d1":[{"d11":1,"d12":2,"d13":3},
                      {"d21":1,"d22":2,"d23":3}]},
           "x":1,"y":2}

def flatten_dict(my_dict):
    out = {}
    for key, val in my_dict.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subitem in val:
                inner_dict = flatten_dict(subitem).items()
                out.update({key + "_" + key2:val2 for key2, val2 in inner_dict})
        else:
            out[key] = val
    return out

flatten_dict(my_dict)