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


While the ``dataset``, ``data-controller``, ``authors``, ``funding`` categories are all
required to be completed, we recommend completing as many categories and properties as
possible in order to generate a more comprehensive record that enhances the display and 
accessibility of the dataset in the catalog.

Below we provide more specific information about the metadata categories and their
respective properties.


