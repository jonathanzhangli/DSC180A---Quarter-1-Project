#!/usr/bin/env python3

import sys
import json

from src import motif_algorithm

def main(targets):
    if 'test' in targets:
        with open('config/single-cluster-params.json') as fh:
            data_params = json.load(fh)
        motif_algorithm.run_algorithm(**data_params)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
