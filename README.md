# Metadata guidelines

The source document for all dataset metadata related guides at the VU is the **[minimal metadata guide](minimal_metadata_guide.md)** in the root folder. This document contains a table that states mandatory, recommended and optional properties that VU researchers should use if they publish their
data in any repository. At minimum researchers should make sure all mandatory properties are used, of course specific repositories might require additional mandatory fields. The source document is also availabe in [Word and PDF](https://github.com/vu-rdm-tech/metadata/tree/main/other_formats) formats.

The guide was approved by VUO in 2021 and can be considered official VU policy.

### Use
The properties used are based on the [DataCite Metadata Schema 4.4](https://schema.datacite.org/meta/kernel-4.4/). Most data repositories will use a metadata scheme that is at least compatible with DataCite so usually an easy translation can be made between terms used in a repository and the terms in this guide (for example "authors" will be "creators").

This repository acts as the _Source of Truth_ of all the dataset metadata guidelines the VU uses as internal documentation or publishes online for researchers and data stewards. If changes in the minimal guide or the tool guides are necessary, we will review these, then update this repository first and only then will we copy updated texts to the various VU websites (Teams, vuweb, libguides, yoda.vu.nl, OSF wiki, etc.). 

Metadata guides for specific tools like Yoda, OSF, DataverseNL or Pure are derivatives of this document and should use the same texts, explanations and terminology as much as possible.

Make sure the metadata guidelines version number, found in `source/docs/version.md`, is referenced in all derivatives. 

This way we can make sure all the information we publish about dataset metadata stays consistent and follows these offical guidelines. The excellent versioning functionality of github means we also keep a log of all changes.
### Intended audience
The [minimal metadata guide](minimal_metadata_guide.md) is mainly meant as a reference for support personnel involved in the VU NRDS network. 

To target researchers tool specific guides are preferred, so they do not have to interpret these guidelines for that tool themselves. 

## How to request changes
### Create an issue
The easiest way to request a change is by opening a new issue on https://github.com/vu-rdm-tech/metadata/issues.

Please be as explicit as possible about the exact change you want and why it needs to be changed.
### Create a pull request
You can also make changes in the documents themselves and propose them by making a pull request, see [Editing the documents](#editing-the-documents)
## Editing the documents
### 1. Prerequisites
- Make sure you have an [account on github](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home).
- Make sure you have [installed git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
- Make sure you have a suitable markdown editor. [Visual Studio Code](https://code.visualstudio.com/) is a nice free one.

Note that Visual Studio Code has [built-in git support](https://code.visualstudio.com/docs/editor/versioncontrol), so you do not have to use the command line git commands.

### 2. Get the documents and code
- If you don't have the code on your pc first clone the metadata repository to an appropriate place:
```
git clone https://github.com/vu-rdm-tech/metadata
```
- If you already have the repository on your pc make sure you run a `git pull` to get the latest changes.
### 3. Create a new branch for your changes
```
git checkout -b <branch name>
```
`<branch name>` should be a short string, e.g. title_changes.

This makes sure you do not directly change the main branch. Instead you will create a Pull request, that can be reviewed by others.

### 4 Editing the documents
The markdown documents can reference other documents by including them between double curly braces. 
For example to paste in the title explanation text use `{{explanation/title.md}}`. This makes it easier to reuse bits of text and target specific change requests.

### 4a. Edit the minimal metadata guide
Do not edit the `minimal_metadata_guide.md` directly, but edit the `.md` documents in the source folder.

- To edit a property explanation: edit the appropriate document under `source/explanation`
  - Note: to indicate a new line in an explanation only use the HTML tag `<br>`. Other linebreaks will mess up the table formatting
- To edit the (sub)properties and obligations: edit `source/table/minimal-metadata.md`
- To edit the introduction text: edit `source/part/minimal-guide-introduction.md`
- To edit the main document structure edit `source/docs/minimal-guide.md`

### 4b. Edit the metadata table for a specific tool
- For OSF project metadata, edit `source/docs/osf-project-metadata-table.md`.
- For Yoda, edit `source/docs/yoda-metadata-table.md`.
### 5. Update the version number
Edit `source/docs/guide_version.md`

### 6. Commit and push back to github
Once you are satisfied with your changes commit them.
```
git commit -a -m '<some useful message>'
```
You can reference a github issue in your commit message by using `#<issue number>`.

Now push the changes to the repo on github:
```
git push
```

Github will now also automatically rebuild `minimal-metadata-guide.md`, `OSF/project_metadata_table.md` and `Yoda/metadata_table.md`. You can view the results in the[repo in github](https://github.com/vu-rdm-tech/metadata) or do a `git pull` to review the changed files in your editor.

### 7. Create a Pull request
- Switch to your branch in github.
- Click "Compare & pull request"
- Write a comment and click create Pull request

The pull request can now be reviewed and merged by the repository admins.

## Troubleshoot the document rebuilding
This is defined in `.github/workflows`.

To view the logging:
See [Actions in the repo and click "Process docs"](https://github.com/vu-rdm-tech/metadata/actions/workflows/main.yml).

You should see the results of all runs here. You can also manually start a run by clicking "Run workflow" and selecting the branch you want to process.

## Creating different file formats
Install [pandoc](https://pandoc.org/installing.html) (Linux version is easiest to use). Then:
```
pandoc -f markdown -t docx -o other_formats/minimal_metadataguide.docx minimal_metadata_guide.md 
pandoc -f markdown -t pdf -o _formats/minimal_metadata_guide.pdf minimal_metadata_guide.md
```

## Other documents
[Yoda datacite mapping (Excel)](Yoda/Metadata%20Yoda-Pure.ods)

[Using metadata in Yoda](https://yoda.vu.nl/site/getting-started/metadata-add.html)
([Source](https://github.com/vu-rdm-tech/site/blob/master/getting-started/metadata-add.md))

[melite text format](melite/melite-proposed.md) 
When cloning the repository initialise this module with `git submodule update --init --remote -- melite`
