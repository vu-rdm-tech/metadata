# Minimal descriptive metadata for research data

## Introduction
This is meant to be a practical guideline fo researchers to advise them on a minimal set of metadata to describe a research dataset. 
The set of metadata properties used is based on the [DataCite Metadata Schema](https://schema.datacite.org/meta/kernel-4.4/).

### Why (minimal) metadata?
#### For archiving
By archiving we mean storing an immutable copy of a dataset for a longer period (5 or 10 years). During such a period all 
the researchers involved in the particular project  might have left the organization. This means there should be enough 
metadata to identify who created the dataset, what it is and why it was produced. 

#### For publishing
By publishing we mean sharing the metadata and if possible the dataset itself on the internet. By using the DataCite schema The VU follows
[FAIR (Findable Accessible Interoperable) principles](https://www.go-fair.org/fair-principles/).

The VU also wants published datasets to be registered in the research information system Pure (https://research.vu.nl). 
The minimal metadata is sufficient for Pure registrations. For most repositories (DataverseNL, Yoda, Zenodo, etc.) will be
able to automatically harvest the metadata so you do not have to describe the metadata twice.  

#### Human vs machine readability
When describing a dataset think about how the metadata will be used. Machines will index the metadata so you should add 
relevant keywords, description and a title so your dataset will pop up in an internet search. Make sure you as creator and all 
the conbtributors are correctly named so published datasets are correctly attributed to you and automated systems can add
them to your portfolio. Explicitly add persistent URLs to related publications or datasets to the metadata so they can be linked.

Once someone finds your dataset he or she will want to read your description to quickly see if the dataset is relevant, 
so especially the description should be human readable. Consider adding extra documentation in the form of a README file 
or a codebook to provide more context on how the data was gathered and processed, variables used in files, which software was used, etc. 

### How to use this document?
Most, if not all, repositories and publication will have their own webform with mandatory and recommended fields. Consider 
this document as a guideline. Sometimes properties might be differently named (author vs creator) but in all cases it should 
be possible to enter all the metadata that is advised in this document.

If the system does not provide you with functionality for entering metadata (for example research drive) you might consider 
adding a text file with the metadata. We have developed a specification for such a file (https://github.com/vu-rdm-tech/melite-metadata/blob/main/melite-proposed.md).

## Properties and explanations

**M** Considered mandatory for findability of your dataset and correct registration in Pure  
**R** Recommended for optimal findability  
**O** Optional

| **ID** | **Property** | **Subproperty** | **Publishing** | **Archiving** | **Explanation**
|---|---|---|---|---|---
| 1 |  Identifier |  | M | O | This should be a global unique identifier, which preferably is unchangeable and links to the datasets. In most cases the repository where you publish your data will generate this in the form of a Handle or DOI.<br>If no persistent URL is available you could use a normal URL, but be aware that you should not move the data afterwards.<br>(A persistent identifier is optional for unpublished archived datasets.)
| 2a |Creator(s) | Name | M | M | Enter names as: &lt;family name>, &lt;first name> &lt;initials> e.g. Olivier, Brett G. 
| 2b | | Affiliation(s) | M | M | Always make sure to always enter your affiliations when you archive or publish your dataset.<br>Make sure you at least add the VU, the correct name for the VU is “Vrije Universiteit Amsterdam”.<br>Note: some repositories may allow you to enter a ROR identifier (Research Organization Registry). The VU ROR is: [https://ror.org/008xxew50](https://ror.org/008xxew50)
| 2c | | Identifier(s) | R | R | If known, enter one or more unique identifiers like AuthorID, ORCID, ISNI or ResearcherID.<br>The VU strongly recommends registering for an ORCID ([https://orcid.org/](https://orcid.org/)). This is an easy way to uniquely identify yourself over which you have full control.
| 3  | Title | | M | M | A descriptive title for your dataset, should not be longer than about 200 characters
| 4  | Publisher | | M | O | Name of the organization where you published your dataset. In most cases the repository where you upload your data will fill this in automatically. Otherwise fill in the name of the organization owning the website or database.<br>(This field only applies to published datasets.)
| 5  | Publication Year | | M | O | The year (or date) you first published your dataset. the repository where you upload your data will usually generate this automatically.<br>(This field only applies to published datasets.)
| 6  | Subject(s) | | R | R | Provide a list of keywords describing your dataset. This will make it easier to find your dataset on the internet.<br>Some repositories will have controlled term lists to choose from.
| 7a | Contributor(s) | Name | R | R | Enter names as: &lt;family name>, &lt;first name> &lt;initials> e.g. Olivier, Brett G.
| 7b | | Affiliation(s) | M | M | Always make sure to always enter affiliations when you archive or publish your dataset.<br>Make sure you at least add the VU, the correct name for the VU is “Vrije Universiteit Amsterdam”.
| 7c | | Identifier(s) | R | R | If known, enter one or more unique identifiers like AuthorID, ORCID, ISNI or ResearcherID.
| 8  | Date(s) | | R | R | If applicable add extra dates applying to your dataset. A good addition is the “Date collected”, meaning the date or date range when you collected the dataset.
| 9  | Language | | O | O | The primary language of your dataset. Please use a 2 letter code (e.g. en, nl, fr, see https://www.loc.gov/standards/iso639-2/php/code_list.php).
| 10 | Resource Type | | M | M | Choose one of the following terms that best applies to your resource (For most data this will be “Dataset”):<br>Audiovisual, Book, BookChapter, Collection, ComputationalNotebook, ConferencePaper, ConferenceProceeding, DataPaper, Dataset, Dissertation, Event, Image, InteractiveResource, Model, OutputManagementPlan, PeerReview, PhysicalObject, Preprint, Report, Service, Software, Sound, Standard, Text, Workflow, Other 
| 11 | Alternate Identfier(s) | | O | O | Alternative identifiers (next to the one supplied in 1) uniquely describing your dataset.
| 12 | Related Identfier(s) | Identifier | R | R | List other resources related to your dataset, for example journal articles for which the data was used or other dataset generated from the same source.<br>Please use unique identifiers like DOIs.
| 12 |  | Relation Type | R | R | The particular relation to the resource should be described by one of the terms in the following list:<br>IsCitedBy, Cites, IsSupplementTo, IsSupplementedBy, IsContinuedBy, Continues, Describes, IsDescribedBy, HasMetadata, IsMetadataFor, HasVersion, IsVersionOf, IsNewVersionOf, IsPreviousVersionOf, IsPartOf, HasPart, IsPublishedIn, IsReferencedBy, References, IsDocumentedBy, Documents, IsCompiledBy, Compiles, IsVariantFormOf, IsOriginalFormOf, IsIdenticalTo, IsReviewedBy, Reviews, IsDerivedFrom, IsSourceOf, IsRequiredBy, Requires, Obsoletes, IsObsoletedBy
| 13 | Size | | O | O | The size (MB, GB, TB) of your dataset, in most cases the repository will calculate this for you.
| 14 | Format | | O | O | Technical formats of your data (for example pdf, xls, stata). This will help other researchers to use your data and provides information on the long term preservation of the data.<br>Consider adding a README file to your dataset to provide a more in-depth explanation on which software you used to create your dataset.
| 15 | Version | | O | O | Version number of your dataset. Useful if you need to publish an updated version of your dataset later.
| 16 | Rights | | M | M |Provide information about how other researchers can use your dataset.<br>If your dataset is Open, e.g. other researchers will be able to access it you should provide a license under which they can do so. For standard licenses provide a URL such as https://creativecommons.org/licenses/by-sa/4.0/<br>If you need to use a custom license, provide it as a text file called `license.txt`.
| 17 | Description | | M | M | Describe your dataset, e.g. the subject, the sample size, methodology, etc. It is best to keep this description concise. More elaborate documentation should be added in a text file called README.
| 18 | GeoLocation | | R | R | If your data is linked to a particular location provide a place name (English preferred) and/or the coordinates. Coordinates can either be a point location (as: longitude, latitude) or a bounding box defined by 4 coordinates (as: west longitude, east longitude, north latitude, south latitude)
| 19 | Funding Reference | | O | O |
| 20 | Related item | | O | O |




## Resource types

<table>
  <tr>
   <td><strong>Audiovisual</strong>
   </td>
   <td>A series of visual representations imparting an impression of motion when shown in succession. May or may not include sound.
   </td>
  </tr>
  <tr>
   <td><strong>Book</strong>
   </td>
   <td>A medium for recording information in the form of writing or images, typically composed of many pages bound together and protected by a cover
   </td>
  </tr>
  <tr>
   <td><strong>BookChapter</strong>
   </td>
   <td>One of the main divisions of a book.
   </td>
  </tr>
  <tr>
   <td><strong>Collection</strong>
   </td>
   <td>An aggregation of resources, which may encompass collections of one resourceType as well as those of mixed types. A collection is described as a group; its parts
   </td>
  </tr>
  <tr>
   <td><strong>ComputationalNotebook</strong>
   </td>
   <td><a href="https://en.wikipedia.org/wiki/Literate_programming">A virtual notebook environment used for literate</a> programming
   </td>
  </tr>
  <tr>
   <td><strong>ConferencePaper</strong>
   </td>
   <td>Article that is written with the goal of being accepted to a conference
   </td>
  </tr>
  <tr>
   <td><strong>ConferenceProceeding</strong>
   </td>
   <td>Collection of academic papers published in the context of an academic conference
   </td>
  </tr>
  <tr>
   <td><strong>DataPaper</strong>
   </td>
   <td>A factual and objective publication with a focused intent to identify and describe specific data, sets of data, or data collections to facilitate discoverability
   </td>
  </tr>
  <tr>
   <td><strong>Dataset</strong>
   </td>
   <td>Data encoded in a defined structure
   </td>
  </tr>
  <tr>
   <td><strong>Dissertation</strong>
   </td>
   <td>A written essay, treatise, or thesis,
   </td>
  </tr>
  <tr>
   <td><strong>Event</strong>
   </td>
   <td>A non-persistent, time- based occurrence
   </td>
  </tr>
  <tr>
   <td><strong>Image</strong>
   </td>
   <td>A visual representation other than text
   </td>
  </tr>
  <tr>
   <td><strong>InteractiveResource</strong>
   </td>
   <td>A resource requiring interaction from the user to be understood, executed, or experienced
   </td>
  </tr>
  <tr>
   <td><strong>Model</strong>
   </td>
   <td>An abstract, conceptual, graphical, mathematical or visualization model that represents empirical objects, phenomena, or physical processes
   </td>
  </tr>
  <tr>
   <td><strong>OutputManagementPlan</strong>
   </td>
   <td>A formal document that outlines how research outputs are to be handled both during a research project and after the project is completed
   </td>
  </tr>
  <tr>
   <td><strong>PeerReview</strong>
   </td>
   <td>Evaluation of scientific, academic, or professional work by others working in the same field
   </td>
  </tr>
  <tr>
   <td><strong>PhysicalObject</strong>
   </td>
   <td>An inanimate, three- dimensional object or substance
   </td>
  </tr>
  <tr>
   <td><strong>Preprint</strong>
   </td>
   <td>A version of a scholarly or scientific paper that precedes formal peer review and publication in a peer-reviewed scholarly or scientific journal
   </td>
  </tr>
  <tr>
   <td><strong>Report</strong>
   </td>
   <td>A document that presents information in an organized format for a specific audience and purpose
   </td>
  </tr>
  <tr>
   <td><strong>Service</strong>
   </td>
   <td>An organized system of apparatus, appliances, staff, etc., for supplying some function(s) required by end users
   </td>
  </tr>
  <tr>
   <td><strong>Software</strong>
   </td>
   <td>A computer program other than a computational notebook, in either source code (text) or compiled form. Use this type for general software components supporting scholarly research. Use the “ComputationalNote book” value for virtual notebooks.
   </td>
  </tr>
  <tr>
   <td><strong>Sound</strong>
   </td>
   <td>A resource primarily intended to be heard
   </td>
  </tr>
  <tr>
   <td><strong>Standard</strong>
   </td>
   <td>Something established by authority, custom, or general consent as a model, example, or point of reference
   </td>
  </tr>
  <tr>
   <td><strong>Text</strong>
   </td>
   <td>A resource consisting primarily of words for reading that is not covered by any other textual
   </td>
  </tr>
  <tr>
   <td><strong>Workflow</strong>
   </td>
   <td>A structured series of steps which can be executed to produce a final outcome, allowing users a means to specify and enact their work in a more reproducible manner
   </td>
  </tr>
  <tr>
   <td><strong>Other</strong>
   </td>
   <td>
   </td>
  </tr>
</table>

