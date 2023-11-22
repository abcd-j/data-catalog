from argparse import ArgumentParser
import json
from pathlib import Path

from datalad_tabby.io import load_tabby

repo_path = Path(__file__).resolve().parent.parent

parser = ArgumentParser()
parser.add_argument(
    "path", type=str, help="Path to the tabby record(s)"
)
args = parser.parse_args()

records = load_tabby(
    src=Path(args.path),
    single=True,
    jsonld=True,
    recursive=True,
    cpaths=[repo_path / 'inputs' / 'tby-abcdjv0'],
)

print(json.dumps(records))