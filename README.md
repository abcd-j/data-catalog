# The ABCDJ Catalog

***under construction***

---

## Repository Layout

`./data`
- a datalad subdataset of the `data-catalog` dataset/repo
- will populate the catalog home page
- functions as the superdataset for ABCDJ datalad datasets
- all datasets added to the catalog will first be added as subdatasets to the `abcdj-data` superdataset

`./code`
- location for scripts to be used for catalog updates

`./catalog`
- this is where the catalog sources live
- the live catalog site serves this directory
- created with `eb3ce6e19ef4e69cbd853d04ba916a32525c804a`

`./inputs`
- input files used during catalog creation, updates, and testing

`./user-docs`
- sphinx-based documentation sources
- to contain documentation for catalog users and contributors

## Requirements

First install `datalad` and its dependencies.

Then, in a virtual environment, run:

```
pip install -r requirements.txt
```

All commands detailed below should be run in the same virtual environment

## Design

The main source of metadata for the data catalog (at [data.abcd-j.de](data.abcd-j.de)) is the DataLad dataset at `./data` (or https://github.com/abcd-j/data), also referred to as the catalog superdataset or the catalog home page dataset.

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
- The `tabby` records are annotated with `@tby-abcdjv0`, which is the convention defined at `./inputs/tby-abcdjv0`
- The superdataset has self-describing `tabby` records located in `./data/.datalad/tabby/self`
- The `data_A` dataset is a plain subdirectory with `tabby` records
- The `data_B` dataset is a DataLad dataset (which might have its own set of self-describing `tabby` records), and  subdataset of the superdataset

An important technical aspect is the linkage between the superdataset and subdatasets, which has an influence on rendering and availability of datasets in the catalog. The decision was made for the data catalog to always show a home page dataset by default (the superdataset) which provides content describing the overall ABCD-J project, and that any datasets can be navigated to from the list of "subdatasets" of this home page dataset.

Thus, for datasets to be findable in the catalog, they have to be listed in the catalog metadata as a "subdataset" of the home page dataset. Since we have two ways in which metadata can be added to the superdataset, the way in which this linkage propagates to the catalog metadata can also be handled in two ways:
- Linkage between DataLad datasets is already built-in via (DataLad's extension of) git submodules, and this metadata can be extracted and converted to the catalog schema with a [custom script](https://github.com/datalad/datalad-catalog/blob/abcdj/datalad_catalog/extractors/catalog_core.py).
- Linkage of a subdirectory with tabby records to the datalad superdataset can be done by adding the relevant information from the subdirectory's tabby records to the `subdatasets@tby-abcdjv0.tsv` file of the superdataset's self-describing tabby records. This metadata is extracted and converted to the catalog schema using scripts in this repository.


## How to update the catalog

- (re)create the catalog
- (re)add the homepage metadata
- collecting new dataset metadata
- add new dataset metadata to the superdataset
- add a new dataset to the catalog

### (Re)create the catalog

E.g. after updating the configuration or logo, or after new features have been added to `datalad-catalog`:

```
datalad rerun eb3ce6e19ef4e69cbd853d04ba916a32525c804a
```

### (Re)add the homepage metadata

E.g. after updating the `tabby` files in `data/.datalad/tabby/self/`:

```
datalad rerun 32a7ce4b7aeea625d1ad822e30d4788e3da753ab
```
