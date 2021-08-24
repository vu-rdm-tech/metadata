# Minimal descriptive metadata for research data

## Introduction
Data and metadata standards can be complex and difficult to start working with. This document provides a practical guideline to working with a generic minimal metadata description that can be used to describe any dataset. In this document we define:
- **dataset** as information generated, or used, that is conceptually and/or logically related and can be written down (encoded/serialised) as one or more files in a machine readable format.
- **metadata** as information that describes a dataset and can be written down (serialised/encoded) in one or more standard formats and a
- **standard format** a formally defined metadata schema that is well defined, serialisable and available in a machine readable format. In this document the metadata properties are derived from and map to a subset of the [DataCite Metadata Schema](https://schema.datacite.org/meta/kernel-4.4/).

### Why (minimal) metadata?
In principle, *richer metadata is better*, however, the properties used in this subset should be applicable to (and supported by) a wide a range of tools, platforms etc. In addition, the properties decscribed in this document should be usable by researchers who do not have a domain specific alternative and who, in general, may even be discouraged from using metadata at all if *required* to add extensive metadata to every dataset they produce. Instead a minimalist approach is used i.e. the number of *required* properties is kept to a mimnimum (only those necessary to ensure DataCite interoperability). Furthermore a more extensive set of properties is provided that allows for richer descriptions of the data as well as semantic linking to other resources. The use of these additional properties is highly recommended.

#### For archiving
By archiving we mean storing an immutable copy of a dataset for a longer period (5 or 10 years). During such a period all the researchers involved in the particular project  might have left the organization. This means there should be enough metadata to identify who created the dataset, what it is and why it was produced.

#### For publishing
By publishing we mean sharing the metadata and, if possible, the dataset itself on the internet making it findable and reusable by other researchers. In this way, like DataCite, our minimal metadata guidelines enables [FAIR (Findable, Accessible, Interoperable, Reusable)](https://www.go-fair.org/fair-principles/) data management.

The VU data management policy requires published datasets to be registered in the research information system [Pure](https://research.vu.nl) and rhe minimal metadata specification includes the necessary properties that allows for easy dataset registration in Pure. When research data is deposited in widely-used, registered, repositories (DataverseNL, Yoda, Zenodo, etc.) it can be automatically harvested and registered in Pure without having to enter the same information twice.

#### Human vs. machine readability
When describing a dataset think about how the metadata will be used. Computers will index the metadata so you should add
relevant keywords, description and a title so your dataset will pop up in an internet search. Make sure you as creator and all the contributors are correctly named so published datasets are correctly attributed to you and automated systems can attribute the dataset to your research output. Explicitly adding persistent URLs to related publications or datasets to the metadata enables them to be efficiently linked together.

Once someone finds your dataset he or she will want to read your description to quickly see if the dataset is relevant,
so it is important that the *Description* should be human readable. While the description should describe the data it is generally good practice to add extra information about the dataset in additional documentation. This can take the form of a README.txt file or codebook and can provide more context on how the data was gathered and processed, the experimental protocols and software used to generate the dataset as well as the filename system and variable nanes used in the individual files etc.

### How to use this document?
Most, if not all, repositories and publication platforms will use their own webform for metadata with mandatory and recommended fields. Consider
this document as a guideline for recommended and mandatory fields extra to those the particular system requires. Sometimes properties might be differently named (for example authors vs creators) but in all cases it should be possible to enter, at least, the mandatory metadata that is advised in this document. Similarly, during your research, if domain-specific metadata exists, that includes the mandatory properties described here, then it is recomended to use the domain-specific format as metadata. However, in cases where no domain-specific metadata exists, the guidelines presented here should be considered.

If your storage system does not provide you with functionality for entering metadata (for example ResearchDrive, OneDrive) you can consider using the human-writable, machine readable form of these guidelines, [Melite](https://github.com/vu-rdm-tech/melite-metadata/blob/main/melite-proposed.md), which we have developed and can be saved as a plaing text file.

### Using related identifiers
This metadata specification allows you to link the dataset or collection that it describes to other online resources. More commonly know as [Linked Data](https://en.wikipedia.org/wiki/Linked_data) these relations form the basis of the Semantic Web and can be thought of as a set of statements that relate a *subject* (the dataset described by the metadata) using a *predicate* (the related identifier property) to an *object* (represented by a unique identifier).

For example, consider metadata describing this specification document (the dataset), we could say:
* the dataset is derived from DataCite 4.
* the dataset is a version of the text that is developed on GitHub.
* the dataset is the source of the human-readable format Melite

If we add in some specific detail and make the subject implicit (everything is about the dataset) we can rewrite the above as:
* **IsDerivedFrom** 10.14454/3w3z-sa82
* **IsVersionOf** https://github.com/vu-rdm-tech/metadata
* **IsSourceOf** https://github.com/vu-rdm-tech/melite-metadata

By doing this we have linked or mapped the relations between our document to other internet resources in a machine readable way.
