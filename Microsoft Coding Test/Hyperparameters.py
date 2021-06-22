###
## Author: Taiwo O. Adetiloye
## Date: Aug 28, 2020
## Solution 1
###

''' Corner cases
1. If the prefix_length is greater that the length of the key prefix,
then the formulation would be distorted
2.  The dictionary is not ideal for situation where the
hyperparameters has to be changed since dictionary keys are immutable.
3. This is compatible with Python3 using collections to get unique items

Problem 1: Hyperparameter Naming

Sofia, a data scientist, wants to train a machine learning model that accepts a set of tunable hyperparameters.
The hyperparameters are specified in a Python dictionary as follows:

H = {
   “learning_rate”: 0.1,
   “dropout_in”: 0.5,
   “dropout_out”: 0.3,
   “use_cutout”: True,
   “use_skip”: False,
   “momentum”: 0.9
}

Sofia wants to nicely serialize the hyperparameters into a string such that she can easily remember her experiments.
To this end, she decides to code a function get_experiment_name(hyperparameters_dict, prefix_length=-1) that returns a string.
A prefix_length specifies the length of the hyperparameter prefix that will be reported in the experiment name string.
In the case that two hyperparameters have the same prefix of length prefix_length, the function returns the minimum
length prefix that can uniquely identify the hyperparameter.

A few example usages are:

get_experiment_name(H) -> “learningrate_0.1_dropoutin_0.5_dropoutout_0.3_usecutout_True_useskip_False_momentum_0.9”

get_experiment_name(H, 3) -> “lea_0.1_dropouti_0.5_dropouto_0.3_usec_True_uses_False_mom_0.9”

get_experiment_name(H, 1) -> “l_0.1_dropouti_0.5_dropouto_0.3_usec_True_uses_False_m_0.9”

Complete the following function and discuss/analyze corner-cases i.e. possible problems with the current formulation:

def get_experiment_name(hyperparameters_dict, prefix_length=-1):
    experiment_name = “”
    return experiment_name

'''
import collections


def get_experiment_name(hyperparameters_dict, prefix_length=-1):
    H = hyperparameters_dict

    experiment_name = ""

    # define default value of experiment

    for key, value in H.items():
        prefix_determinator = key.replace("_", "") + "_" + str(value) + "_"
        experiment_name = experiment_name + prefix_determinator

    if (prefix_length == -1) or (prefix_length is None):

        # return default value
        get_length = len(experiment_name)  # get length of experiment name
        return experiment_name[:get_length - 1]

    else:
        H_key_list = list(H.keys())  # get key lists

        # get prefix
        prefix_determinator1 = [H_key_list[i].split("_")[0] for i in range(len(H_key_list))]

        # get same key prefix
        uniq = [item for item, count in collections.Counter(prefix_determinator1).items() if count > 1]
        uniq_prefix = []

        for key in H.keys():
            for i in uniq:
                if key.startswith(i):
                    split_key = key.split("_")
                    str1 = split_key[0]
                    str2 = split_key[1][:1]
                    concat_key = str1 + str2
                    uniq_prefix.append(concat_key)
                    H_key_list.remove(key)

        H_key_list_prefix = [i[:prefix_length] for i in H_key_list]

        # Replace experiment name strings with new values
        experiment_name = experiment_name \
            .replace("learningrate", H_key_list_prefix[0]) \
            .replace("momentum", H_key_list_prefix[1]) \
            .replace("dropoutin", uniq_prefix[0]) \
            .replace("dropoutout", uniq_prefix[1]) \
            .replace("usecutout", uniq_prefix[2]) \
            .replace("useskip", uniq_prefix[3])

        get_length = len(experiment_name)  # get length of experiment name
        return experiment_name[:get_length - 1]


if __name__ == '__main__':
    H = {
        "learning_rate": 0.1,
        "dropout_in": 0.5,
        "dropout_out": 0.3,
        "use_cutout": True,
        "use_skip": False,
        "momentum": 0.9
    }
    # Test_case 1
    print(get_experiment_name(
        H))  # “learningrate_0.1_dropoutin_0.5_dropoutout_0.3_usecutout_True_useskip_False_momentum_0.9”

    # Test_case 2
    print(get_experiment_name(H, 1))  # “l_0.1_dropouti_0.5_dropouto_0.3_usec_True_uses_False_m_0.9”

    # Test_case 3
    print(get_experiment_name(H, 3))  # “lea_0.1_dropouti_0.5_dropouto_0.3_usec_True_uses_False_mom_0.9”