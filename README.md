### **!** This repository has moved to https://hub.psychoinformatics.de/abcd-j/data-catalog **!**

# The ABCDJ Catalog

This repository (which is also a DataLad dataset) contains the sources and content for:
- the ABCD-J Data Catalog hosted at: https://data.abcd-j.de/
- the ABCD-J Data Catalog RDM Documentation for users hosted at: https://rdm.abcd-j.de/
- all tools necessary for generating these two sites

For more information about the ABCD-J project, visit the website at: https://www.abcd-j.de/

---

## Content

1. [Repository Layout](#repository-layout)
2. [Requirements](#requirements)
3. [Design](#design)
4. [How to update the catalog](#how-to-update-the-catalog)
   1. [(Re)create the catalog](#recreate-the-catalog)
   2. [(Re)add the homepage metadata](#readd-the-homepage-metadata)
   3. [Collecting new dataset metadata](#collecting-new-dataset-metadata)
   4. [Add new dataset metadata to the `data` superdataset](#add-new-dataset-metadata-to-the-data-superdataset)
   5. [Add a new dataset to the catalog](#add-a-new-dataset-to-the-catalog)
5.[Deployment](#deployment)

## Repository Layout

`./catalog`
- this is where the data catalog sources live
- the live catalog site serves this directory

`./code`
- this directory contains scripts that are used for catalog updates

`./data`
- this is a DataLad subdataset of the current `data-catalog` dataset/repo
- its origin is at: https://github.com/abcd-j/data
- it functions as the superdataset for all ABCD-J datasets rendered in the catalog, i.e. it is the homepage of the catalog

`./docs`
- sphinx-based documentation sources
- contains documentation for catalog users and contributors
- published to https://rdm.abcd-j.de/ via GitHub pages

`./inputs`
- input files used during catalog creation, updates, and testing


## Requirements

First install `datalad` and its dependencies.

Then, in a virtual environment, run:

```
pip install -r requirements.txt
```

All commands detailed below should be run in the same virtual environment

## Design

The main source of metadata for the data catalog (at [data.abcd-j.de](data.abcd-j.de)) is the DataLad dataset at `./data` (or https://github.com/abcd-j/data), also referred to as the catalog superdataset or the catalog homepage dataset.

The idea is that this superdataset acts as a container for the metadata of all new datasets that should be represented in the catalog.

Metadata can be added to the superdataset in two ways:
1. As a set of `tabby` records (see [docs](https://docs.datalad.org/projects/tabby/en/latest/?badge=latest)) in a subdirectory
2. As a DataLad subdataset in a subdirectory

An example tree of the superdataset might be as follows:

```
data                                            # datalad superdataset
.
├── .datalad
│   └── tabby/self                              # self-describing tabby metadata
│       ├── authors@tby-abcdjv0.tsv
│       ├── dataset@tby-abcdjv0.tsv
│       ├── funding@tby-abcdjv0.tsv
│       └── subdatasets@tby-abcdjv0.tsv
├── data_A                                      # a subdirectory with tabby metadata
│   ├── authors@tby-abcdjv0.tsv
│   ├── data-controller@tby-abcdjv0.tsv
│   ├── dataset@tby-abcdjv0.tsv
│   ├── files@tby-ds1.tsv
│   ├── funding@tby-abcdjv0.tsv
│   ├── publications@tby-abcdjv0.tsv
│   └── used-for@tby-abcdjv0.tsv
└── data_B                                      # a datalad subdataset
    └── .datalad
```

Note that:
- The `tabby` records are annotated with `@tby-abcdjv0`, which is the tabby convention defined at `./inputs/tby-abcdjv0`
- The data superdataset has self-describing `tabby` records located in `./data/.datalad/tabby/self`
- The `data_A` dataset is a plain subdirectory with `tabby` records (i.e. TSV files)
- The `data_B` dataset is a DataLad dataset (which might have its own set of self-describing `tabby` records, or not), and is also subdataset of the catalog superdataset

An important technical aspect is the linkage between the superdataset and subdatasets, which has an influence on rendering and availability of datasets in the catalog. The decision was made for the data catalog to always show a homepage dataset by default (the superdataset) which provides content describing the overall ABCD-J project, and that any datasets can be navigated to from the list of "(sub)datasets" of this homepage dataset.

Thus, for datasets to be findable in the catalog, they have to be listed in the catalog metadata as a "subdataset" of the homepage dataset. Since we have two ways in which metadata can be added to the superdataset, the way in which this linkage propagates to the catalog metadata can also be handled in two ways:
- Linkage between DataLad datasets is already built-in via (DataLad's extension of) git submodules, and this metadata can be extracted and converted to the catalog schema with a [custom script](https://github.com/datalad/datalad-catalog/blob/abcdj/datalad_catalog/extractors/catalog_core.py).
- Linkage of a subdirectory with tabby records to the datalad superdataset can be done by adding the relevant information from the subdirectory's tabby records to the `subdatasets@tby-abcdjv0.tsv` file of the superdataset's self-describing tabby records. This metadata is extracted and converted to the catalog schema using scripts in this repository.

Another important technical aspect to note is that all content in this repository should be committed to git, so that the catalog does not have troubles trying to access content that is annexed.

## How to update the catalog

Several scripts or commands and also manual steps are required for creating, updating, and maintaining the ABCD-J Data Catalog, including:

- (re)create the catalog
- (re)add the homepage metadata
- collecting new dataset metadata
- add new dataset metadata to the `data` superdataset
- add a new dataset to the catalog

All commands given below should be run within the correct virtual environment from the root directory of a local clone of this repository.

For provenance and reproducibility, we run scripts encapsulated in the `datalad run` command.

*NOTE: several steps below are not optimized yet for automatic execution, and needs manual intervention in order to be completed correctly. Automating these steps is still a work in progress.*

### (Re)create the catalog

Since the catalog has already been created, recreation is not likely. But in some cases it might be necessary, such as after updating the catalog-level configuration or custom logo, or after new features have been added to `datalad-catalog` and we want them to be propagated to this catalog instance:

```
datalad run -m "Create the catalog" -i "inputs/*" -o "catalog/*" --assume-ready both "datalad catalog-create --catalog catalog --config-file inputs/catalog-config.json --force"
```

The `run` command's flags include:
- `-i "inputs/*"`: indicated where inputs are located
- `-o "outputs/*"`: indicated where outputs are written to
- `--assume-ready both`: assume that inputs do not need to be retrieved and outputs do not need to unlocked or removed before running the command

The command being run has the following parts:
- `datalad catalog-create`: use the `datalad-catalog` package to create a catalog
- `--catalog catalog`: the location where the catalog will be created
- `--config-file inputs/catalog-config.json`: use the provided config file for catalog creation
- `--force`: overwrite assets if the catalog already exists at the specified location

### (Re)add the homepage metadata

This will typically be necessary after the `tabby` files in `data/.datalad/tabby/self/` (or at https://github.com/abcd-j/data) have been updated.

First ensure that the local subdataset at `data` is updated with regards to its remote `origin` (if indeed that is where the update comes from). If the update originated locally, i.e. from within the local subdataset at `data`, it is recommended to let this update find its way back to the remote `origin` in any case.

Then run the following:

```
datalad run -m "Update catalog homepage's self-describing metadata" -i "inputs/*" -o "catalog/*" --assume-ready both "python code/process_homepage.py data --add-to-catalog"
```

This will:
- run the script at `code/process_homepage.py`
- extract the updated homepage metadata from tabby files at `data/.datalad/tabby/self/`
- transform this metadata to be compatible with the catalog schema
- add the catalog-compatible entry to the catalog (if the `--add-to-catalog` flag is provided)
- reset the catalog homepage to the updated version
- add a new commit to this repository containing these changes

After this, a push to this repository's `origin` (at https://github.com/abcd-j/data-catalog) will be necessary before the changes will show up on the catalog site.


### Collecting new dataset metadata

For a new dataset to be entered into the catalog, its metadata has to be collected somehow. The current method for collecting metadata is to have users complete sheet-based forms, as described in the RDM user docs at: https://rdm.abcd-j.de/instructions.html.

Once the sheets have been received from users (which could be via email, download link, or shared workspace/server access). These have to be converted to tabby-compatible TSV files. This is still a manual process at the moment. Luckily, the template sheets shared with users are already set up to be optimally compatible. A couple of manual steps are left to do:

1. Add the rows in the table below to the `dataset` sheet of the document provided by the user. These are necessary for `datalad-tabby` to import other sheets into the parent `dataset` sheet, so that metadata from all provided sheets can be loaded correctly. These rows are not included in the template doc provided to users so as not to confuse them with unnecessary technical content.

    | column 1 | column 2 |
    | - | - |
    | authors | @tabby-many-authors@tby-abcdjv0 |
    | data-controller | @tabby-optional-many-data-controller@tby-abcdjv0 |
    | files | @tabby-optional-many-files@tby-ds1 |
    | funding | @tabby-optional-many-funding@tby-abcdjv0 |
    | publication | @tabby-optional-many-publications@tby-abcdjv0 |
    | subdatasets | @tabby-optional-many-subdatasets@tby-abcdjv0 |
    | used-for | @tabby-optional-many-used-for@tby-abcdjv0 |

2. Export all sheets of the document separately as TSV files. Then ensure that all of these TSV files have the correct names (identical to the sheets they were exported from), and that each filename is appended with the tabby convention used in the process of loading metadata from these files. You should end up with a list of files similar to the following:
   - `authors@tby-abcdjv0.tsv`
   - `data-controller@tby-abcdjv0.tsv`
   - `dataset@tby-abcdjv0.tsv`
   - `files@tby-ds1.tsv`
   - `funding@tby-abcdjv0.tsv`
   - `publication@tby-abcdjv0.tsv`
   - `subdatasets@tby-abcdjv0.tsv`
   - `used-for@tby-abcdjv0.tsv`

Now you have your complete set of metadata files for a dataset!

### Add new dataset metadata to the `data` superdataset

Next, the TSV files have to be added to the DataLad dataset that groups together all catalog dataset metadata. It is maintained at https://github.com/abcd-j/data and is also included in the current repository as a Datalad subdataset at `data`.

Once you have the repository at https://github.com/abcd-j/data cloned locally, inspect the file tree. At the time of writing this part of the README, it looked like this:

```
.
├── FZJ
│   ├── jumax
│   │   ├── authors@tby-abcdjv0.tsv
│   │   ├── data-controller@tby-abcdjv0.tsv
│   │   ├── dataset@tby-abcdjv0.tsv
│   │   ├── files@tby-ds1.tsv
│   │   └── funding@tby-abcdjv0.tsv
│   └── movies
│       ├── authors@tby-abcdjv0.tsv
│       ├── data-controller@tby-abcdjv0.tsv
│       ├── dataset@tby-abcdjv0.tsv
│       ├── files@tby-ds1.tsv
│       └── funding@tby-abcdjv0.tsv
└── UKD
    └── ocr-PIRA-cohort
        ├── authors@tby-abcdjv0.tsv
        ├── data-controller@tby-abcdjv0.tsv
        ├── dataset@tby-abcdjv0.tsv
        ├── files@tby-ds1.tsv
        ├── publications@tby-abcdjv0.tsv
        └── used-for@tby-abcdjv0.tsv
```

As you can see, dataset metadata are added into subdirectories per dataset, that are in turn added into subdirectories per institute where the datasets originate from.

If a new incoming dataset originates from an institute not yet represented in the file tree, discuss the naming of a new institute directory with project/group members before creating it.

Then:
- create a new dataset directory inside the relevant institute directory (`jumax` inside `FZJ`)
- move all the TSV files into this new directory
- commit these changes to git
- push the commit to the remote `origin`

Now you will see your new dataset's metadata files in the `dataset` repository at https://github.com/abcd-j/data.

### Add a new dataset to the catalog

And now, the final step 

In your local clone of the current `data-catalog` repository, make sure you have the `main` branch checked out and updated with regards to the remote `origin`. Also make sure that its DataLad subdataset at `data` is (a) installed locally, and (b) updated with regards to its own remote `origin`. These latter steps are important because it ensures that your newest addition of TSV files is available locally AND known to the `data-catalog` repository, from where you will run all code to add entries to the catalog. You can make sure the `data` subdataset is updated by navigating to it (`cd data`) from the current repository root, and then running `datalad update --how merge`, and then checking if you can see the files that you have recently added to the `data` dataset.

Then we have to run the code to extract the metadata and add it to the catalog (and all steps in-between):

```
datalad run -m "Extract new dataset metadata from tabby records and add entries to catalog" -i "inputs/*" -o "catalog/*" --assume-ready both "python code/process_subdirectory.py data <relative-path-to-new-dataset> --dataset-type <new-dataset-type> --add-to-catalog"
```

To break it down:
- `datalad run -i "inputs/*" -o "catalog/*" --assume-ready both` does exactly the same as explained previously
- `python code/process_subdirectory.py data`: this is the script that does all the work, and its main argument points to the homepage dataset, located at `data` (relative to the current repository root)
- `<relative-path-to-new-dataset>`: should be replaced by your new dataset directory location relative to the `data` dataset root. For the example used previously in relation to the file tree, it would be `FZJ/jumax`.
- `--dataset-type <new-dataset-type>`: this is used to help the script know what to do with the `name` field provided by the user in the `dataset@tby-abcdjv0.tsv` sheet. See https://rdm.abcd-j.de/instructions.html#dataset-required:

   > If the dataset is structured as a DataLad dataset, the name property should be the DataLad dataset ID, and the type property should be datalad.
  
  The value of `<new-dataset-type>` will either be `datalad` or `other` (the latter, most likely) *(TODO: this is an example of a step that must still be automated)*
- `--add-to-catalog`: This flag adds all generated entries to the catalog.

A concrete example:

```
datalad run -m "Extract new dataset metadata from tabby records and add entries to catalog" -i "inputs/*" -o "catalog/*" --assume-ready both "python code/process_subdirectory.py data FZJ/jumax --dataset-type datalad --add-to-catalog"
```

This code will:
- run the script at `code/process_subdirectory.py`
- extract the new dataset metadata from tabby files at `data/FZJ/jumax/*`
- transform this extracted metadata to be compatible with the catalog schema
- extract the homepage metadata from tabby files at 
- add the new dataset (id and version) as a new subdataset to the homepage metadata in tabby files at `data/.datalad/tabby/self/*`
- save the updated homepage dataset at `data` (i.e. the DataLad subdataset of the current repository)
- add the new dataset's catalog-compatible entries to the catalog (if the `--add-to-catalog` flag is provided)
- reset the catalog homepage to the updated version (after adding a new subdataset)
- add a new commit to the current repository containing all these changes

After this, it is important to:

1. Push to this repository's `origin` (at https://github.com/abcd-j/data-catalog) so that the changes will show up on the catalog site.
2. Push the new commit in the `data` subdataset to its own remote `origin`.

And this concludes the elaborate process of adding a new dataset to the catalog!

## Deployment

The sources in this repository are deployed to two sites:
- the ABCD-J Data Catalog hosted at: https://data.abcd-j.de/
- the ABCD-J Data Catalog RDM Documentation for users hosted at: https://rdm.abcd-j.de/

### The Data Catalog

Deployment is done via a custom server setup handled internally by Psyinf at INM-7. A cron job runs every 15 minutes, pulls updates from this repository, and deploys all files in the `catalog` subdirectory. The server has redirects enabled according to the requirements and process described here: https://github.com/psychoinformatics-de/sfb1451-projects-catalog/pull/83

### The RDM docs

The content of the docs folder is built with Sphinx (using a github action at `.github/workflows/docbuild.yml`) and then deployed via github pages, linked to the custom domain. Settins for this can be updated via this repository's settings on GitHub.

