"""
Usage:
  inspect_coverage.py --input_folder=<input_folder> --path_to_index=<path_to_index> --target_languages=<target_languages> --verbose=<verbose>

Options:
  --input_folder=<input_folder> input folder (we check in all subdirectories for *naf files)
  --path_to_index=<path_to_index> path to .p file containing mappings
  --target_languages=<target_languages> e.g., "nl---it---en"
  --verbose=<verbose>


Example:
    python inspect_coverage.py --input_folder="example_files" --path_to_index="merged_indices.p" --target_languages="en---nl---it" --verbose=2
"""
from docopt import docopt
import pickle
from glob import glob
from lxml import etree
from collections import defaultdict

# load arguments
arguments = docopt(__doc__)
print()
print('PROVIDED ARGUMENTS')
print(arguments)
print()


all_mappings = pickle.load(open(arguments['--path_to_index'], 'rb'))
target_languages = list(arguments['--target_languages'].split('---'))
verbose = int(arguments['--verbose'])

lang2mapping_coverage = {
    lang : defaultdict(list)
    for lang in target_languages
}

for naf_path in glob(f'{arguments["--input_folder"]}/**/*naf', recursive=True):
    doc = etree.parse(naf_path)
    root = doc.getroot()

    lang = root.get('{http://www.w3.org/XML/1998/namespace}lang')

    for entity_el in doc.xpath('entities/entity/externalReferences/externalRef'):
        wiki_url = entity_el.get('reference')

        if wiki_url not in all_mappings[lang]:
            if verbose >= 2:
                print(f'{wiki_url} not found in mapping')

            for target_language in target_languages:
                if target_language != lang:
                    lang2mapping_coverage[lang][target_language].append(0)
        else:
            for target_language in target_languages:
                if target_language != lang:
                    if target_language in all_mappings[lang][wiki_url]:
                        lang2mapping_coverage[lang][target_language].append(1)


for lang, coverage_info in lang2mapping_coverage.items():

    num_wiki_urls = len(coverage_info)
    print()
    print(f'source language: {lang}')

    for target_language, info in coverage_info.items():

        if target_language != lang:
            print(f'target language: {target_language}')
            total = len(info)
            found = sum(info)
            perc = 100 * (found / total)
            print(f'found {found} out of {total} ({round(perc, 2)}%)')
