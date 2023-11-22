# The ABCDJ Catalog

***under construction***

---

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
- recreate with: `datalad rerun d286c81d053a4dadf4d094a765bfc6316364c5fa`

`./inputs`
- input files used during catalog creation and updates

`./user-docs`
- sphinx-based documentation sources
- to contain documentation for catalog users and contributors
