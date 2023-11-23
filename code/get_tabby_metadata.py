from argparse import ArgumentParser
import json
from pathlib import Path
from pyld import jsonld

from datalad_catalog.schema_utils import (
    get_metadata_item,
)
from datalad_next.constraints.dataset import EnsureDataset
from datalad_tabby.io import load_tabby

from utils import (
    process_funding,
    process_authors,
    process_keywords,
    CAT_CONTEXT,
)

def get_metadata(ds, tabby_path):
    repo_path = Path(__file__).resolve().parent.parent
    home_record = load_tabby(
        src=tabby_path,
        single=True,
        jsonld=True,
        recursive=True,
        cpaths=[repo_path / 'inputs'],
    )
    expanded = jsonld.expand(home_record)
    compacted = jsonld.compact(home_record, ctx=CAT_CONTEXT)
    # Use catalog schema_utils to get base structure of metadata item
    meta_item = get_metadata_item(
        item_type='dataset',
        dataset_id=ds.id,
        dataset_version=ds.repo.get_hexsha(),
        source_name="tabby",
        source_version="0.1.0",
    )
    # note: this becomes catalog page title, so title fits better
    meta_item["name"] = compacted.get("title", "")
    meta_item["description"] = compacted.get("description", "")
    meta_item["doi"] = compacted.get("doi", "")
    meta_item["authors"] = process_authors(compacted.get("authors"))
    meta_item["keywords"] = process_keywords(compacted.get("keywords"))
    meta_item["funding"] = process_funding(compacted.get("funding"))
    return meta_item


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument(
        "dataset_path", type=Path, help="Path to the datalad dataset"
    )
    args = parser.parse_args()
    ds = EnsureDataset(
        installed=True, purpose="extract tabby metadata", require_id=True
    )(args.dataset_path).ds

    tabby_path = Path(args.dataset_path) / '.datalad/tabby/self/dataset@tby-abcdjv0.tsv'
    meta_item = get_metadata(ds, tabby_path)
    print(json.dumps(meta_item))
