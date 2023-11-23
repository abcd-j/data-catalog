# The ABCDJ Catalog

***under construction***

---

## Layout

`./abcdj-data`
- a datalad subdataset of the `abcdj-catalog` dataset/repo
- will populate the catalog home page
- functions as the superdataset for ABCDJ datalad datasets
- all datasets added to the catalog will first be added as subdatasets to the `abcdj-data` superdataset

`./code`
- location for scripts to be used for catalog updates

`./docs`
- this is where the catalog sources live
- the github pages site build from this directory
- created with `d286c81d053a4dadf4d094a765bfc6316364c5fa`

`./inputs`
- input files used during catalog creation and updates

`./user-docs`
- sphinx-based documentation sources
- to contain documentation for catalog users and contributors

## Developer notes

### Install requirements

First install `datalad` and dependencies.

Then, in a virtual environment:
```
pip install -r requirements.txt
```

### (Re)create the catalog

E.g. after updating the configuration or logo, or after new features have been added to `datalad-catalog`:

```
datalad rerun d286c81d053a4dadf4d094a765bfc6316364c5fa
```

### (Re)add the homepage metadata

E.g. after updating the `tabby` files in `data/.datalad/tabby/self/`:

```
datalad rerun f2f7cb5e7d1bd9d411b83ac7f776a6ff64b4283d
```



