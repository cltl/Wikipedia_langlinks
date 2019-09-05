rm -rf resources
mkdir resources
cd resources

git clone https://github.com/clab/wikipedia-parallel-titles
cd wikipedia-parallel-titles

rm *gz

wget https://dumps.wikimedia.org/nlwiki/20190720/nlwiki-20190720-page.sql.gz
wget https://dumps.wikimedia.org/nlwiki/20190720/nlwiki-20190720-langlinks.sql.gz

wget https://dumps.wikimedia.org/itwiki/20190720/itwiki-20190720-page.sql.gz
wget https://dumps.wikimedia.org/itwiki/20190720/itwiki-20190720-langlinks.sql.gz

cp lib/*py resources/wikipedia-parallel-titles
