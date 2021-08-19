# Metadata guidelines

[minimal metadata guide](minimal_metadata_guide.md)

[Yoda datacite mapping](Yoda/Metadata%20Yoda-Pure.ods)

[Using metadata in Yoda](https://yoda.vu.nl/site/getting-started/metadata-add.html)
([Source](https://github.com/vu-rdm-tech/site/blob/master/getting-started/metadata-add.md))

[melite text format](melite/melite-proposed.md) 
When cloning the repository initialise this module with `git submodule update --init --remote -- melite`

## Building metadata documentation from parts
Example: the minimal guide template [structured/docs/minimal-guide.md(structured/docs/minimal-guide.md)
```
cd structured
python preprocess.py -i docs/minimal-guide.md -o minimal-metadata-guide.md
```
## Creating different file formats
Install [pandoc](https://pandoc.org/installing.html).
```
pandoc -f markdown -t docx -o minimal-metadata-guide.docx minimal-metadata-guide.md 
```