Instructions
************

In this section we'll take you through the process of contributing data to the ABCD-J catalog.
In essence, it involves filling metadata properties into sheet-based forms and submitting the
completed forms.


Step 1 - View the example sheets
================================

To familiarize yourself with the metadata format, we have constructed a complete metadata
record that is ready for submission to a data catalog. You can access this in one of two ways:

* in an online `example Google Sheets document`_
* by downloading this :download:`example Excel file <_static/abcdj-example-record.xlsx>`

The example record is about the `Palmer Penguins dataset`_. You will see that the document
contains several sheets, such as ``dataset``, ``authors``, etc. We will expand on these sections
below.

.. _example Google Sheets document: https://docs.google.com/spreadsheets/d/1YNZV5_kSa9HS8iB8bfSBQf9_sMr4d3cl
.. _Palmer Penguins dataset: https://allisonhorst.github.io/palmerpenguins/

Step 2 - Access the template sheets
===================================

When filling in the metadata properties for your dataset, you can use empty template sheets
to speed up the process. The template sheets can be accessed in one of two ways:

* via the `template Google Sheets document`_ (download once the tab is open)
* via the :download:`template Excel file <_static/abcdj-template-record.xlsx>`

.. _template Google Sheets document: https://docs.google.com/spreadsheets/d/1LNeiVilsA-2EEvDjKr1FdibTMx78tTMy

Step 3 - Fill in the metadata properties
========================================

In the template document, you will find seven sheets, each sheet corresponding
to a specific category of metadata with specific fields to be completed.

Figure 1 below shows how these categories appear in multiple sheets contained within the Excel document.

.. image:: /_static/data_catalog_entry_categories.png
   :alt: data catalog entry categories
   :align: center

The metadata categories (i.e. sheet names) are:

* ``dataset`` - properties of the dataset itself (required)
* ``data-controller`` - properties of the people or organizations in control of the data (required)
* ``authors`` - authors or creators of the dataset (required)
* ``funding`` - funding sources associated with the data (required)
* ``publications`` - publications associated with the data
* ``files`` - files that form part of the dataset
* ``used-for`` - the purpose of the dataset


While only the ``dataset``, ``data-controller``, ``authors``, and ``funding`` categories are
required to be completed, we recommend completing as many categories and properties as
possible in order to generate a more comprehensive record that enhances the display and 
accessibility of the dataset in the catalog.

.. important::
    The ``required`` aspect is applicable to both *categories* and *properties*.
    All ``required`` categories should be completed, and all ``required``
    properties should be completed for any category that is completed.

Below we provide more specific information about the metadata categories and their
respective properties.

``dataset`` (required)
----------------------

This category contains the main descriptive properties of your dataset.
Property names are given in the first column, and values should be entered
in the second column (and possibly in the following columns). Recognized properties are:

**name (required)**
    
    The ``name`` identifies the dataset uniquely within the ABCD-J project,
    and within the data catalog, i.e. there must not be different datasets
    with the same name. The name should be suitable for a directory/folder name.
    Spaces and special characters should be avoided. 
    
.. note:: 
    If the dataset is structured as a DataLad dataset, the ``name`` property
    should be the DataLad dataset ID, and the ``type`` property should be ``datalad``.

**title (required)**

    This ``title`` will be the actual display name of the dataset the catalog.
    The language must be English.

**description (required)**

    A general description of the dataset. It may summarize its purpose, scope, content,
    and potential applications. If a long description needs to be split into paragraphs,
    each paragraph can be put into a dedicated column in this row. The language must be English.

**type (required)**

    The type of dataset, which provides a way for DataLad users to provide additional useful
    information. Options are ``custom`` (the default) or ``datalad``. The latter should only
    be selected if the dataset is already structured as a DataLad dataset. In that case, the
    required ``name`` property of the dataset should be the DataLad dataset ID.

**version (required)**

    A label that identifies the version of the dataset. If a dataset is unversioned, it is
    acceptable to state ``latest``. Otherwise any numerical label (e.g., 1.2), or text label
    (e.g., GITSHA 7db210fb5) can be provided here. The version should change when the content
    of the dataset changes.

**sample[organism] (required)**
    
    A classification of the organism(s) associated with, or studied for, the dataset. One or
    more organisms can be given, one per column.
    
    Organisms must be identified by their ID in the NCBI organismal taxonomy,
    which can be searched at https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon.
    
    For example, the identifier for human or homo sapiens is ``NCBITaxon:9606``.
    The column value should be ``NCBITaxon:9606`` in this case.

**sample[organism-part] (required)**
    
    A classification of organism part(s) associated with, or studied for, the dataset.
    One or more organism parts can be given, one per column.
    
    Organism parts must be identified by their ID in the Uber-anatomy ontology (UBERON),
    which can be searched at https://www.ebi.ac.uk/ols4/ontologies/uberon.
    
    For example, the identifier for upper limb segment is ``UBERON:0008785``.
    The column value should be ``UBERON:0008785`` in this case. As another example,
    the identifier for the brain is ``UBERON:0000955``, but more precise definitions
    for individual brain structures are available.

keywords
    
    Keywords describing the major topical themes of the dataset. Any number of keywords
    can be given, one keyword per column. Keywords aid the discoverability of a dataset.

license

    A license document (URL) that applies to the dataset and defines the terms and conditions for use.

doi

    A Digital Object Identifier assigned to the dataset (e.g., from a data portal it was published in).
    The DOI should preferably point to the dataset version described in the catalog record.

homepage

    A URL the catalog should advertise as the primary source of information/data on this dataset.
    This could be, for example, a dataset page in a data portal.

last-updated

    The date of the last modification of the described dataset (version), for example a release date.
    The date must be given in ISO 8601 format (i.e., ``YYYY-MM-DD``).


``data-controller`` (required)
------------------------------

This category lists one or more entities (natural persons or organizations) that are (legally) responsible
for a dataset, and serve as an official contact point regarding collaboration inquiries. 

For datasets involving personal data (as defined in the European General Data Protection Regulation; GDPR)
this category lists *data controllers*. For any other research datasets, these are typically the PIs of the
involved project(s).

Property names are given in the first non-comment row, and values for each entity are given in subsequent rows
(columns corresponding to the header row specification). Recognized properties are:

**name (required)**

    The full name of the responsible entity. For example, the name of a project PI
    or a data protection officer.

**email (required)**

    An email address with which the entity can be contacted. For example, the institutional email address
    of the project PI.

type

    The type of data controller (either Person, or Organization).

address

    A (postal) address for the responsible entity.


``authors`` (required)
----------------------

This category lists one or more entities (natural persons or organizations) that are considered authors
of the dataset. These authors need not be identical to an author list of an associated publication. Any
entity listed in this category will be credited as an author on the catalog page of the dataset.

Property names are given in the first non-comment row, and values for each entity are given in subsequent rows
(columns corresponding to the header row specification). Recognized properties are:

**name (required)**
    
    The full name of the author.

email

    An email address with which the author can be contacted.

orcid

    ORCID of this author, to uniquely identify a researcher.

affiliation
    
    One or more names of organizations or institutions an author is affiliated with. Affiliations are free-form text.
    Multiple affiliations can be given by entering additional affiliations in new columns of the same row.


``funding`` (required)
----------------------

This category lists one or more funding sources that are associated with the dataset and that shall be
credited on the dataset's catalog page.

Property names are given in the first non-comment row, and values for each entity are given in subsequent rows
(columns corresponding to the header row specification). Recognized properties are:

**funder (required)**

    The name of the funding body that provided the financial resources (typically in the form of a grant)
    that funded the creation/collection of the dataset.
    
**grant (required)**

    A grant identifier. This is typically a funder-specific project code.

url

    A persistent online addres for the specific grant.


``publications``
----------------

This category lists one or more publications associated with the dataset and that shall be credited on the
dataset's catalog page.

Property names are given in the first non-comment row, and values for each entity are given in subsequent rows
(columns corresponding to the header row specification). Recognized properties are:

**citation (required, but optional if doi is specified)**

    A free-form text citation for the publication that enables the publication record to be displayed on the catalog page.
    All citations in a metadata record should use a common, and homogeneous format.

doi

    A Digital Object Identifier (URL, starting with https://doi.org/) for a publication. This enables publication
    DOI display on a catalog page, persistently identifies the publication, and enables metadata retrieval from
    bibliographic databases.

url

    A URL pointing to the publication. A corresponding link is placed on the dataset page in the catalog.
    This need not be given when a publication DOI is specified.

date

    Date of publication in ISO 8601 format (i.e., ``YYYY-MM-DD``), but year alone is also sufficient.


``files``
---------

.. important::
    For help with generating automatic filelists for your dataset, please see
    the secion: :doc:`for_maintainers`. For further assistance, contact the ABCD-J
    support team at ``t.heunis@fz-juelich.de``.

This category lists one or more files that form part of the dataset.

Property names are given in the first non-comment row, and values for each entity are given in subsequent rows
(columns corresponding to the header row specification). Recognized properties are:

**path[POSIX] (required)**

    The relative path of the file (within the dataset) in POSIX/UNIX notation, i.e. using forward slashes as separators.
    This enables display of a file tree on the dataset catalog page. Tip: do not include a top-level directory that matches
    the dataset name, because the files are already understood as being part of the dataset.

size[bytes]
    
    The file size in bytes. This property enables (total) size information in the catalog record and the file
    tree on the dataset catalog page.

checksum[md5]

    The MD5 checksum ("fingerprint") of the file, which enables content/download verification.

url

    The file content URL, which allows (possibly access-protected) download of that particular file.
    This enables the display of a download button for that specific file on the dataset catalog page.

``used-for``
------------

This table lists one or more activities/projects that the dataset has been or is presently being used for.

Property names are given in the first non-comment row, and values for each entity are given in subsequent rows
(columns corresponding to the header row specification). Recognized properties are:

**title (required)**

    A title for the activity/project. This will be displayed on the dataset page in the catalog.

url

    A URL pointing to a web page representing the activity/project, or providing information on it.
    A corresponding link is shown on the dataset page in the catalog.

description
    
    A description of the activity/project, possibly focused on the role/association of the dataset in it.
    If a long description needs to be split into paragraphs, each paragraph can be put into a dedicated column.
    The language must be English.


Step 4 - Share the metadata!
============================

Once you have completed all the **required** (and ideally also the optional) metadata categories and properties,
your metadata document with its completed sheets will be almost ready to share. Please follow these steps:

Name the document
-----------------

Rename your document to use the following format: ``<partner-code>_<dataset-title>``.

- The ``partner-code`` should be ``A``, ``B``, ``C``, ``D``, or ``J`` (for Aachen, Bonn, Cologne, Düsseldorf, Jülich).
- The ``dataset-title`` should be the same as the ``title`` metadata property completed in the ``dataset`` category/sheet.
- Please use dashes (``-``) to separate words in the title (no spaces). 

For example, if a dataset titled "Movies in the scanner" was collected at Research Center Jülich, the metadata document name should be ``J_Movies-in-the-scanner``.

Share the document
------------------

You can share the document in several ways:

- Send an Excel document (``.xlsx``) as an attachment via email.
- Upload an Excel document to your sharing service of choice and provide a download link.
- Upload an Excel document to Google Sheets and provide an access link.
- Provide an access link to a Google Sheets document.

Please direct all email communication to the ABCD-J support team at ``t.heunis@fz-juelich.de``.