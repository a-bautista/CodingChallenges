def get_experiment_name(H, prefix_length=0):

    # res = max(H, key=H.get)
    # print(res)
    # if prefix_length> max(H, key=H.get):
    #     return -1
    max_val = float('-inf')
    for key, value in H.items():
        k_len = len(key)
        max_val = max(max_val, k_len)


    if max_val < prefix_length:
        return -1

    if not H:
        return -1

    # clean the dictionary by removing the '_'
    cleaned_dict = {}
    experiment_name = ""

    for k, v in H.items():
        cleaned_dict[k.replace('_', '')] = v

    keys = list(cleaned_dict.keys())

    # default case
    if prefix_length <= 0:
        for k, val in cleaned_dict.items():
            experiment_name += k+"_"+str(val)+"_"
        return experiment_name[:-1]

    duplicate = {}  # sub dictionary of H with the duplicate values
    # debugging
    #duplicatesIndex = {}  # dict w/ key duplicated shor form and value of a list of keys that are duplicated at length stop
    res = {}  # {longform: shortform}

    # get duplicates
    while len(res.keys()) < len(keys) or len(duplicate.keys()) != 0:

        duplicatesIndex = {}
        duplicate = {}

        # find duplicates
        for key in keys:
            # when the window is greater than the current key
            if prefix_length > len(key):
                continue
            k = key[:prefix_length]  # short version <-- when end of key length
            res[key] = k
            if k not in duplicatesIndex:
                duplicatesIndex[k] = [key]
            else:
                duplicatesIndex[k].append(key)

        # deduplication
        for k in duplicatesIndex:
            if len(duplicatesIndex[k]) > 1:
                for key in duplicatesIndex[k]:
                    # get the values of the keys
                    duplicate[key] = cleaned_dict[key]

        # increase the window
        prefix_length += 1
        # get the next set of keys
        keys = list(duplicate.keys())


    # print("-" * 15)
    # print(res.values())

    for k, v in res.items():
        experiment_name += v + "_" + str(cleaned_dict[k]) + "_"
    return experiment_name[:-1]


def main():
    H = {
        "1earning_ratio": 0.4,
        "dropout_outtr": 0.9,
        "dropout_in": 0.5,
        "dropout_out": 0.3,
        "use_cutout": True,
        "momentum": 0.9,
        "momentu": 0.95
    }

    H2 = {
        "learning_rate":0.1,
        "dropout_in":0.5,
        "dropout_out":0.3,
        "use_cutout":True,
        "use_skip":False,
        "momentum":0.9
    }
    res = get_experiment_name(H,89)
    print(res)

main()