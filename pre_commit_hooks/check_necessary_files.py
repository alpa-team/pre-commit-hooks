# packit config, alpa config, spec file and package metadata
import sys
from os import getcwd
from pathlib import Path

from alpa.config import AlpaRepoConfig, MetadataConfig
from alpa.repository.branch import LocalRepoBranch
from packit.config.package_config import find_packit_yaml
from packit.exceptions import PackitConfigException


def _find_spec(cwd: Path) -> bool:
    for file in cwd.iterdir():
        if file.is_file() and file.name.endswith(".spec"):
            return True

    return False


def main() -> int:
    cwd = Path(getcwd())
    git_root = LocalRepoBranch(cwd).git_root

    try:
        find_packit_yaml(git_root)
    except PackitConfigException:
        print("No packit config file found!", file=sys.stderr)
        return 1

    AlpaRepoConfig.get_config()
    MetadataConfig.get_config(cwd)

    if not _find_spec(cwd):
        print(f"No specfile found in {cwd}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
