cd resources/wikipedia-parallel-titles
bash build-corpus.sh en nlwiki-20190720  > nl-en.txt
bash build-corpus.sh it nlwiki-20190720  > nl-it.txt
bash build-corpus.sh en itwiki-20190720  > it-en.txt

python create_index.py --output_folder="output" --input_path="nl-en.txt" --from_lang_to_lang="nl---en" --verbose=2
python create_index.py --output_folder="output" --input_path="it-en.txt" --from_lang_to_lang="it---en" --verbose=2
python create_index.py --output_folder="output" --input_path="nl-it.txt" --from_lang_to_lang="nl---it" --verbose=2

python merge_indices.py --input_folder='output' --verbose="2"
