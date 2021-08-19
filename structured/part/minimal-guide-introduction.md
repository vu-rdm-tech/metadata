## Introduction
This document is meant as a practical guideline for researchers to advise them on a minimal set of metadata to describe a research dataset.
The set of metadata properties used is based on the [DataCite Metadata Schema](https://schema.datacite.org/meta/kernel-4.4/).

### Why (minimal) metadata?
#### For archiving
By archiving we mean storing an immutable copy of a dataset for a longer period (5 or 10 years). During such a period all
the researchers involved in the particular project  might have left the organization. This means there should be enough
metadata to identify who created the dataset, what it is and why it was produced.

#### For publishing
By publishing we mean sharing the metadata and, if possible, the dataset itself on the internet. By basing our minimal
metadata guideline on DataCite The VU follows [FAIR (Findable Accessible Interoperable) principles](https://www.go-fair.org/fair-principles/).

The VU requires published datasets to be registered in the research information system Pure (https://research.vu.nl).
The minimal metadata is sufficient for Pure registrations. For most repositories (DataverseNL, Yoda, Zenodo, etc.) Pure is
able to automatically harvest the metadata so you do not have to describe the metadata twice.

#### Human vs machine readability
When describing a dataset think about how the metadata will be used. Computers will index the metadata so you should add
relevant keywords, description and a title so your dataset will pop up in an internet search. Make sure you as creator and all
the contributors are correctly named so published datasets are correctly attributed to you and automated systems can add
them to your portfolio. Explicitly add persistent URLs to related publications or datasets to the metadata so they can be linked.

Once someone finds your dataset he or she will want to read your description to quickly see if the dataset is relevant,
so especially the description should be human readable. Consider adding extra documentation in the form of a README file
or a codebook to provide more context on how the data was gathered and processed, variables used in files, what software was used, etc.

### How to use this document?
Most, if not all, repositories and publication platforms will use their own webform for metadata with mandatory and recommended fields. Consider
this document as a guideline for recommended and mandatory fields extra to those the particular system requires.
Sometimes properties might be differently named (for example authors vs creators) but in all cases it should
be possible to enter all the metadata that is advised in this document.

If the system does not provide you with functionality for entering metadata (for example research drive) you might consider
adding a text file with the metadata. We have developed a specification for such a file (https://github.com/vu-rdm-tech/melite-metadata/blob/main/melite-proposed.md).
