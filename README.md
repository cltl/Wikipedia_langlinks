# Wikipedia language links

This repo aims to create an index of the interlanguage links in Wikipedia

## Authors

* **Marten Postma** (m.c.postma@vu.nl)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details

### Python modules (Python 3.6 is used)
A number of external modules need to be installed, which are listed in **requirements.txt**.
Depending on how you installed Python, you can probably install the requirements using one of following commands:
```bash
pip install -r requirements.txt
```

### Resources
A number of resources need to be downloaded. Please change it if you want to use other languages. This can be done calling:
```bash
bash download.sh
```

### build index
Call (edit for other languages)
```bash
bash extract.sh
```

### inspect coverage

Call ```
python inspect_coverage.py -h```