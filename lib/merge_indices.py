"""
Merge indices of language links in Wikipedia

Usage:
  merge_indices.py --input_folder=<input_folder> --verbose=<verbose>

Options:
    --input_folder=<input_folder> output of create_index.py
    --verbose=<verbose> 0 --> no stdout 1 --> general stdout 2 --> detailed stdout

Example:
    python merge_indices.py --input_folder='output' --verbose="2"
"""
from docopt import docopt
import os
import pickle
from glob import glob
from collections import defaultdict, Counter

# load arguments
arguments = docopt(__doc__)
print()
print('PROVIDED ARGUMENTS')
print(arguments)
print()

all_mappings = {}
input_folder = arguments['--input_folder']
verbose = int(arguments['--verbose'])

for pickle_path in glob(f'{input_folder}/*p'):
    basename = os.path.basename(pickle_path)
    basename = basename.strip('.p')
    source_lang, target_lang = basename.split('2')
    
    for lang in [source_lang, target_lang]:
        if lang not in all_mappings:
            all_mappings[lang] = defaultdict(dict)

    mapping = pickle.load(open(pickle_path, 'rb'))
    for source, target in mapping.items():
        all_mappings[source_lang][source][target_lang] = target
        all_mappings[target_lang][target][source_lang] = source

output_path = f'{input_folder}/merged_indices.p'
with open(output_path, 'wb') as outfile:
    pickle.dump(all_mappings, outfile)

if verbose >= 2:
    print(f'saved to {output_path}')
