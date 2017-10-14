"""
Base IO code for all datasets
"""

# Copyright (c) 2017 Sanjib Sonowal <sanjib.s@live.com>

import csv
from os.path import dirname, join
from ..utils import Bunch

import numpy as np


def load_data(module_path, data_file_name):
    """
    Loads data from module_path/data/data_file_name.
    """
    with open(join(module_path, 'data', data_file_name)) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        target_names = np.array(temp[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[:-1], dtype=np.float64)
            target[i] = np.asarray(ir[-1], dtype=np.int)

    return data, target, target_names


def load_greetings(return_X_y=False):
    module_path = dirname(__file__)
    data, target, target_names = load_data(module_path, 'greetings.csv')

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target,
                 target_names=target_names)
