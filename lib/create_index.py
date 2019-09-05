"""
Load interlanguage links from Wikipedia

Usage:
  create_index.py --output_folder=<output_folder> --input_path=<input_path> --from_lang_to_lang=<from_lang_to_lang> --verbose=<verbose>

Options:
    --output_folder=<output_folder>
    --input_path=<input_path>
    --from_lang_to_lang=<from_lang_to_lang> LANG1---LANG2
    --verbose=<verbose> 0 --> no stdout 1 --> general stdout 2 --> detailed stdout

Example:
    python create_index.py --output_folder="output" --input_path="nl-en.txt" --from_lang_to_lang="nl---en" --verbose=2
"""
from docopt import docopt
from pathlib import Path
from shutil import rmtree
import pickle


# load arguments
arguments = docopt(__doc__)
print()
print('PROVIDED ARGUMENTS')
print(arguments)
print()

out_folder = Path(arguments['--output_folder'])
if not out_folder.exists():
    out_folder.mkdir()

input_path = arguments['--input_path']
verbose = int(arguments['--verbose'])
src_lang, tgt_lang = arguments['--from_lang_to_lang'].split('---')
output_path = f'{out_folder}/{src_lang}2{tgt_lang}.p'


def to_wiki_url(language, page_title):
    title = page_title.replace(' ', '_')
    return f'http://{language}.wikipedia.org/wiki/{title}'

input_path = arguments['--input_path']

source2target = dict()
with open(input_path) as infile:
    for line in infile:
        source, target = line.strip().split(' ||| ')
        source_wiki = to_wiki_url(src_lang, source)
        target_wiki = to_wiki_url(tgt_lang, target)
        source2target[source_wiki] = target_wiki

with open(output_path, 'wb') as outfile:
    pickle.dump(source2target, outfile)

if verbose >= 1:
    print(f'found {len(source2target)} mappings')
    print(f'saved to {output_path}')
