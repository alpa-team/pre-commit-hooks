"""
Ensure that source0 uses version macro.

when version in spec file is changed -> it should be seen in source0
"""
import sys
import uuid
from os import getcwd
from pathlib import Path
from shutil import copy2
from typing import Optional

from specfile import Specfile


SPEC_ERR_MSG = (
    "No related macro with version in source0 found. Please use "
    "some macro in source0 so when you change version in spec "
    "file, it is propagated to source0."
)


def _find_spec(cwd: Path) -> Optional[Path]:
    for file in cwd.iterdir():
        if file.is_file() and file.name.endswith(".spec"):
            return file

    return None


def main() -> int:
    cwd = Path(getcwd())
    spec_path = _find_spec(cwd)
    if spec_path is None:
        print(f"No specfile found in {cwd}!", file=sys.stderr)
        return 1

    dest_path = f"/tmp/{uuid.uuid4()}.spec"
    copy2(str(spec_path), dest_path)

    specfile = Specfile(Path(dest_path))
    with specfile.sources() as sources:
        source0 = min(sources, key=lambda src: src.number)

    new_version = str(uuid.uuid4()).replace("-", "")
    source_before = source0.expanded_location
    specfile.update_tag("Version", new_version)
    specfile.save()
    specfile.reload()
    source_after = source0.expanded_location
    if source_before == source_after or new_version not in source_after:
        print(SPEC_ERR_MSG, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
