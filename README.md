# Metadata guidelines

[minimal metadata guide](minimal_metadata_guide.md)

[Yoda datacite mapping](Yoda/Metadata%20Yoda-Pure.ods)

[Using metadata in Yoda](https://yoda.vu.nl/site/getting-started/metadata-add.html)
([Source](https://github.com/vu-rdm-tech/site/blob/master/getting-started/metadata-add.md))

[melite text format](melite/melite-proposed.md) 
When cloning the repository initialise this module with `git submodule update --init --remote -- melite`

## Building metadata documentation from parts
Examples: 
The minimal guide template [structured/docs/minimal-guide.md](structured/docs/minimal-guide.md) and the Yoda table [structured/docs/yoda-metadata-table.md](structured/docs/yoda-metadata-table.md) 
```
cd structured
python preprocess.py -i docs/minimal-guide.md -o ../minimal_metadata_guide.md
python preprocess.py -i /docs/yoda-metadata-table.md -o ../Yoda/metadata_table.md
```
Note an updated Yoda table should be copied into https://github.com/vu-rdm-tech/site/blob/master/getting-started/metadata-add.md for use on yoda.vu.nl
## Creating different file formats
Install [pandoc](https://pandoc.org/installing.html).
```
pandoc -f markdown -t docx -o minimal-metadata-guide.docx minimal-metadata-guide.md 
```