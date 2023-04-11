import sys
from os import getcwd
from pathlib import Path

from alpa.repository.branch import LocalRepoBranch
from packit.api import PackitAPI
from packit.exceptions import PackitConfigException


def main() -> int:
    git_root = LocalRepoBranch(Path(getcwd())).git_root
    if git_root is None:
        print("This is a bare git repository!", file=sys.stderr)
        return 1

    try:
        print(PackitAPI.validate_package_config(git_root))
    except PackitConfigException as exc:
        print(exc, file=sys.stderr)
        return 1
    except Exception as exc:
        print(
            f"Exception during validating packit config appeared: {exc}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
