# Minimal descriptive metadata for research data

## Introduction
Data and metadata standards can be complex and difficult to start working with. This document provides a practical guideline to working with a generic minimal metadata description that can be used to describe any dataset. In this document we define: 
- **dataset** as information generated, or used, that is conceptually and/or logically related and can be written down (encoded/serialised) as one or more files in a machine readable format.
- **metadata** as information that describes a dataset and can be written down (serialised/encoded) in one or more standard formats and a
- **standard format** a formally defined metadata schema that is well defined, serialisable and available in a machine readable format. In this document the metadata properties are derived from and map to a subset of the [DataCite Metadata Schema](https://schema.datacite.org/meta/kernel-4.4/).

### Why (minimal) metadata?
In principle, *richer metadata is better*, however, the properties used in this subset should be applicable to (and supported by) a wide a range of tools, platforms etc. In addition, the properties decscribed in this document should be usable by researchers who do not have a domain specific alternative and who, in general, may even be discouraged from using metadata at all if *required* to add extensive metadata to every dataset they produce. Instead a minimalist approach is used i.e. the number of *required* properties is kept to a mimnimum (only those necessary to ensure DataCite interoperability). Furthermore a more extensive set of properties is provided that allows for richer descriptions of the data as well as semantic linking to other resources. The use of these additional properties is highly recommended.

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
| 7a | Contributor(s) | Name | R | R | Enter names as: &lt;family name>, &lt;first name> &lt;initials> e.g. Olivier, Brett G. A Contributor can also be an organization, for example a university, research institute, or your department at the VU.
| 7b | | Affiliation(s) | M | M | Always make sure to always enter affiliations when you archive or publish your dataset.<br>Make sure you at least add the VU, the correct name for the VU is “Vrije Universiteit Amsterdam”.
| 7c | | Identifier(s) | R | R | If known, enter one or more unique identifiers like AuthorID, ORCID, ISNI or ResearcherID.
| 7d | | Type | M | M | The role of the contributor, see the [table below](#contributor-types) for possible types. If contributor is used then Contributor Type is mandatory. 
| 8  | Date(s) | | R | R | If applicable add extra dates applying to your dataset. A good addition is the “Date collected”, meaning the date or date range when you collected the dataset.
| 9  | Language | | O | O | The primary language of your dataset. Please use a 2 letter code (e.g. en, nl, fr, see https://www.loc.gov/standards/iso639-2/php/code_list.php).
| 10 | Resource Type | | M | M | Choose one of the following terms from the [table below](#resource-types)  
| 11 | Alternate Identfier(s) | | O | O | Alternative identifiers (next to the one supplied in 1) uniquely describing your dataset.
| 12 | Related Identfier(s) | Identifier | R | R | List other resources related to your dataset, for example journal articles for which the data was used or other dataset generated from the same source.<br>Please use unique identifiers like DOIs.
| 12a |  | Relation Type | R | R | The particular relation to the resource should be described by one of the terms in the [table below](#relation-types)
| 13 | Size | | O | O | The size (MB, GB, TB) of your dataset, in most cases the repository will calculate this for you.
| 14 | Format | | O | O | Technical formats of your data (for example pdf, xls, stata). This will help other researchers to use your data and provides information on the long term preservation of the data.<br>Consider adding a README file to your dataset to provide a more in-depth explanation on which software you used to create your dataset.
| 15 | Version | | O | O | Version number of your dataset. Useful if you need to publish an updated version of your dataset later.
| 16 | Rights | | M | M |Provide information about how other researchers can use your dataset.<br>If your dataset is Open, e.g. other researchers will be able to access it you should provide a license under which they can do so. For standard licenses provide a URL such as https://creativecommons.org/licenses/by-sa/4.0/<br>If you need to use a custom license, provide it as a text file called `license.txt`.
| 17 | Description | | M | M | Describe your dataset, e.g. the subject, the sample size, methodology, etc. It is best to keep this description concise. More elaborate documentation should be added in a text file called README.
| 18 | GeoLocation | | R | R | If your data is linked to a particular location provide a place name (English preferred) and/or the coordinates. Coordinates can either be a point location (as: longitude, latitude) or a bounding box defined by 4 coordinates (as: west longitude, east longitude, north latitude, south latitude)
| 19 | Funding Reference | | O | O | The name(s) of the organization(s) funding the research. If using this property also add the Award Number.
| 20 | Related item | | O | O | {PV merge with 12?}

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

## Contributor types

| **Option** | **Definition**
|---|---
| ContactPerson	| Person with knowledge of how to access, troubleshoot, or otherwise field issues related to the resource
| DataCollector	| Person/institution responsible for finding or gathering/collecting data under the guidelines of the author(s) or Principal Investigator (PI)
| DataCurator | Person tasked with reviewing, enhancing, cleaning, or standardizing metadata and the associated data submitted for storage, use, and maintenance within a data centre or repository
| DataManager | Person (or organisation with a staff of data managers, such as a data centre) responsible for maintaining the finished resource
| Distributor | Institution tasked with responsibility to generate/disseminate copies of the resource in either electronic or print form
| Editor | A person who oversees the details related to the publication format of the resource
| HostingInstitution | Typically, the organisation allowing the resource to be available on the internet through the provision of its hardware/software/operating support
| Producer | Typically, a person or organisation responsible for the artistry and form of a media product
| ProjectLeader | Person officially designated as head of project team or sub- project team instrumental in the work necessary to development of the resource
| ProjectManager | Person officially designated as manager of a project. Project may consist of one or many project teams and sub-teams.
| ProjectMember | Person on the membership list of a designated project/project team
| RegistrationAgency | Institution/organisation officially appointed by a Registration Authority to handle specific tasks within a defined area of responsibility
| RegistrationAuthority | A standards-setting body from which Registration Agencies obtain official recognition and guidance
| RelatedPerson | A person without a specifically defined role in the development of the resource, but who is someone the author wishes to recognize
| Researcher | A person involved in analysing data or the results of an experiment or formal study. May indicate an intern or assistant to one of the authors who helped with research but who was not so “key” as to be listed as an author.
| ResearchGroup | Typically refers to a group of individuals with a lab, department, or division that has a specifically defined focus of activity.
| RightsHolder | Person or institution owning or managing property rights, including intellectual property rights over the resource
| Sponsor | Person or organisation that issued a contract or under the auspices of which a work has been written, printed, published, developed, etc.
| Supervisor | Designated administrator over one or more groups/teams working to produce a resource, or over one or more steps of a development process
| WorkPackageLeader | A Work Package is a recognized data product, not all of which is included in publication. The package, instead, may include notes, discarded documents, etc. The Work Package Leader is

## Relation types

| **Option** | Definition
|---|---
|IsCitedBy | indicates that B includes A in a citation
| Cites | indicates that A includes B in a citation
| IsSupplementTo | indicates that A is a supplement to B
| IsSupplementedBy | indicates that B is a supplement to A
| IsContinuedBy | indicates A is continued by the work B
| Continues | indicates A is a continuation of the work B
| Describes |indicates A describes B
| IsDescribedBy | indicates A is described by B
| HasMetadata | indicates resource A has additional metadata B
| IsMetadataFor | indicates additional metadata A for a resource B
| HasVersion | indicates A has a version (B)
| IsVersionOf | indicates A is a version of B
| IsNewVersionOf | indicates A is a new edition of B, where the new edition has been modified or updated
| IsPreviousVersionOf | indicates A is a previous edition of B
| IsPartOf | indicates A is a portion of B; may be used for elements of a series
| HasPart | indicates A includes the part B
| IsPublishedIn | indicates A is published inside B, but is independent of other things published inside of B
| IsReferencedBy | indicates A is used as a source of information by B
| References | indicates B is used as a source of information for A
| IsDocumentedBy | indicates B is documentation about/ explaining A; e.g. points to software documentation
| Documents | indicates A is documentation about B; e.g. points to software documentation
| IsCompiledBy | indicates B is used to compile or create A
| Compiles | indicates B is the result of a compile or
| IsVariantFormOf | indicates A is a variant or different form of B
| IsOriginalFormOf | indicates A is the original form of B
| IsIdenticalTo | indicates that A is identical to B, for use when there is a need to register two separate instances of the same resource
| IsReviewedBy | indicates that A is reviewed by B
| Reviews | indicates that A is a review of B
| IsDerivedFrom | indicates B is a source upon which A is based
| IsSourceOf | indicates A is a source upon which B is based
| IsRequiredBy | Indicates A is required by B
| Requires | Indicates A requires B
| Obsoletes | Indicates A replaces B
| IsObsoletedBy | Indicates A is replaced by B