def main():
    H = {
        "learning_ratio": 0.4,
        "dropout_outtr": 0.9,
        "dropout_in": 0.5,
        "dropout_out": 0.3,
        "use_cutout": True,
        "momentum": 0.9,
        "moment": 0.95
    }

    initial_stop = 1

    # lea, dropuoutoutt, dropouti, droupto, use, mom
    # 0.
    # 1. find duplicates
    # 2.

    # clean the dictionary by removing the '_'
    cleaned_dict = {}
    for k, v in H.items():
        cleaned_dict[k.replace('_','')]=v

    keys = list(cleaned_dict.keys())

    duplicate = {}  # sub dictionary of H with the duplicate values
    # debugging
    duplicatesIndex = {}  # dict w/ key duplicated shor form and value of a list of keys that are duplicated at length stop
    res = {}  # {longform: shortform}

    # get duplicates
    stop = initial_stop
    while len(res.keys()) < len(keys) or len(duplicate.keys()) != 0:
        print(stop)
        print(duplicate)
        print(duplicatesIndex)
        duplicatesIndex = {}
        duplicate = {}

        # find duplicates
        for key in keys:
            # when the window is greater than the current key
            if stop > len(key):
                continue
            k = key[:stop]  # short version <-- when end of key length
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
        stop += 1
        # get the next set of keys
        keys = list(duplicate.keys())

    res_string =""
    print("-"*15)
    print(res.values())

    for k,v in res.items():
        res_string += v+"_"+str(cleaned_dict[k])+"_"
    print(res_string[:-1])

    # print the new key and value followed by '_'
    # {
    #     "learning_ratio": 0.4,
    #     "dropout_outtr": 0.9,
    #     "dropout_in": 0.5,
    #     "dropout_out": 0.3,
    #     "use_cutout": True,
    #     "momentum": 0.9,
    #     "moment": 0.95
    # }

main()

