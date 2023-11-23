from argparse import ArgumentParser
import json
from pathlib import Path

from datalad_catalog.extractors import catalog_core
from datalad_next.constraints.dataset import EnsureDataset

from get_tabby_metadata import get_metadata

if __name__ == "__main__":

    repo_path = Path(__file__).resolve().parent.parent

    parser = ArgumentParser()
    parser.add_argument(
        "dataset_path", type=str, help="Path to the datalad dataset",
    )
    parser.add_argument("--add-to-catalog", action="store_true")
    args = parser.parse_args()

    ds = EnsureDataset(
        installed=True, purpose="extract core metadata", require_id=True
    )(args.dataset_path).ds

    # first get core metadata
    core_record = catalog_core.get_catalog_metadata(ds)
    # then get tabby metadata
    tabby_path = tabby_path = Path(args.dataset_path) / '.datalad/tabby/self/dataset@tby-abcdjv0.tsv'
    tabby_record = get_metadata(ds, tabby_path)

    if args.add_to_catalog:
        from datalad.api import  (
            catalog_add,
            catalog_set,
        )

        catalog_dir = repo_path / 'docs'

        # Add core metadata to the catalog
        catalog_add(
            catalog=catalog_dir,
            metadata=json.dumps(core_record),
            config_file = repo_path / 'inputs' / 'superds-config.json',
        )

        # Add tabby metadata to the catalog
        catalog_add(
            catalog=catalog_dir,
            metadata=json.dumps(tabby_record),
            config_file = repo_path / 'inputs' / 'superds-config.json',
        )
        catalog_set(
            catalog=catalog_dir,
            property="home",
            dataset_id=ds.id,
            dataset_version=ds.repo.get_hexsha(),
            reckless="overwrite",
        )

    print(json.dumps(core_record))
    print("\n\n")
    print(json.dumps(tabby_record))
