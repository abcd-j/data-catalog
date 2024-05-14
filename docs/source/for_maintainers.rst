For maintainers
***************

This section covers instructions and descriptions of helper functionality
for maintainers of the ABCD-J data catalog, or for users who have the necessary 
technical expertise to contribute metadata to catalog themselves.


The catalog setup
=================

.. note:: 
    Coming soon! This section will explain the design of the ABCD-J catalog, 
    how it is put together using different tools, and the requirements for 
    maintaining or contributing to the catalog.


Adding/updating catalog metadata
================================

.. note:: 
    Coming soon! This section will explain how to use provided Python scripts to extract
    and add new metadata to the ABCD-J catalog, or how to update existing metadata


Generating a file list
======================

As mentioned in the user :doc:`instructions`, the optional ``files`` category lists
one or more files that form part of the dataset, with recognized properties:

* ``path[POSIX]`` (required)
* ``size[bytes]`` (optional)
* ``checksum[md5]`` (optional)
* ``url`` (optional)

While such a list of files can be created manually, this becomes tedious and time
consuming for datasets with many files. It is possible to use scripts to automatically
generate a full file list for a given dataset. Such scripts need to generate a TSV file
with the recognized properties and in the format specified in the user :doc:`instructions`.

Since datasets can be stored in different formats, hosted in different locations, and be accessed
in different ways, it is unlikely that a single script can generalize a way in which to generate
a file list. We supply a script ``create_tabby_filelist.py`` that currently supports two options
via arguments:

1. A folder with files, stored on local or server storage
2. A DataLad dataset, stored on local or server storage

.. note:: 
    Customizations to support e.g. git repositories or compressed files are also possible

Hence, it is firstly important to identify whether the script will be run on a
DataLad dataset, or some files on a file system.

Before running the scripts
--------------------------

First ensure that you have a recent version of Python on your machine.
Then make sure you have the ``data-catalog`` code available locally:

.. code-block:: bash

   git clone https://github.com/abcd-j/data-catalog.git


**For running the script on a folder with files**, you do not need to install any further
requirements.

**For running the script on a DataLad dataset**, please install requirements with ``pip``

.. code-block:: bash
   
   cd data-catalog
   pip install -r requirements.txt


Running the scripts
-------------------

The `create_tabby_filelist.py`_ script can then be run as follows:

.. code-block:: python
   
   python3 code/create_tabby_filelist.py --method <glob | tree> --output <path-to-output-directory> <path-to-dataset-location>

where:

* ``<glob | tree>`` should be the selected method: ``glob`` for a folder with files, or ``tree`` for a DataLad dataset
* ``<path-to-output-directory>`` is where the TSV file named ``files@tby-ds1.tsv`` will be written to
* ``<path-to-dataset-location>`` is the location of the dataset (folder with files or DataLad dataset)

This will generate the correct TSV file at location ``<path-to-output-directory>/files@tby-ds1.tsv``, excluding the
values for the ``url``.

If your dataset has a specific download URL for each file, this can then be added to the TSV file.
This process can be done manually, or with another script. Since URLs vary substantially, there is no
general script that would be able to do this for any files. However, an example script can be
found at `add_file_urls.py`_, which could be custimized to suit your own file url schema.


.. _create_tabby_filelist.py: https://github.com/abcd-j/data-catalog/blob/main/code/create_tabby_filelist.py
.. _add_file_urls.py: https://github.com/abcd-j/data-catalog/blob/main/code/add_file_urls.py






