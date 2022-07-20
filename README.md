# Metadata guidelines

The source document for all dataset metadata related guides is the 
[minimal metadata guide](minimal_metadata_guide.md) in the root folder.

Guides for specific tools like Yoda, OSF or Pure are derivatives of this document and will use the same texts, explanations
and terminology.

This repository acts as the _Source of Truth_ of all the dataset metadata guidelines the VU uses as internal 
documentation or publishes online for researchers and data stewards. If anything needs to change, 
either in the minimal metadata guide itself or in one of the tool guides, we update this repository first and 
then we copy the new texts to the various websites (Teams, vuweb, libguides, 
yoda.vu.nl, OSF wiki, etc.). 

Make sure to reference the metadata guidelines version number, found in `source/docs/version.md` 
in all derivatives. 

This way we can make sure all the information we publish stays consistent. The
excellent versioning functionality of github means we also keep a log of all changes.
## How to request changes
### Create an issue
The easiest way to request a change is by opening a new issue on https://github.com/vu-rdm-tech/metadata/issues.

Please be as explicit as possible about the exact change you want and why it needs to be changed.
### Create a pull request
You can also make changes in the documents themselves and propose them by making a pull request. [Editing the documents](#editing-the-documents)
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

This makes sure you do not directly change the main branch. Instead you will create a Pull request, that can be 
reviewed by others.
### 4a. Edit the minimal metadata guide
Do not edit the `minimal_metadata_guide.md` directly, but edit the `.md` documents in the source folder.

- To edit a property explanation: edit the appropriate document under `source/explanation`
- To edit the (sub)properties and obligations: edit `source/table/minimal-metadata.md`
- To edit the introduction text: edit `source/part/minimal-guide-introduction.md`

### 4b. Edit the metadata table for a specific tool
- For OSF project metadata, edit `source/docs/osf-project-metadata-table.md`.
- For Yoda, edit `source/docs/osf-project-metadata-table.md`.

As you can see in these documents you can reference an explanation by including it between double curly braces. 
For example to paste in the the title explanation use `{{explanation/title.md}}`

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

## Build the documents
Run:
```
cd structured
generate-docs.bat
```

Will create:
```
minimal_metadata_guide.md
Yoda/metadata_table.md
OSF/project_metadata_table.md
```

Note an updated Yoda table should be copied into https://github.com/vu-rdm-tech/site/blob/master/getting-started/metadata-add.md for use on yoda.vu.nl

## Other documents

[Yoda datacite mapping](Yoda/Metadata%20Yoda-Pure.ods)

[Using metadata in Yoda](https://yoda.vu.nl/site/getting-started/metadata-add.html)
([Source](https://github.com/vu-rdm-tech/site/blob/master/getting-started/metadata-add.md))

[melite text format](melite/melite-proposed.md) 
When cloning the repository initialise this module with `git submodule update --init --remote -- melite`

## Creating different file formats
Install [pandoc](https://pandoc.org/installing.html) (Linux only). Then:
```
pandoc -f markdown -t docx -o minimal-metadata-guide.docx minimal-metadata-guide.md 
pandoc -f markdown -t pdf -o minimal-metadata-guide.pdf minimal-metadata-guide.md
```