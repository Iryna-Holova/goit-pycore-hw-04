"""
Task 3. Directory structure
"""

import sys
from pathlib import Path

import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)


def get_dir_structure(path: Path, prefix: str = "") -> None:
    """
    Prints the structure of a directory.

    Args:
        path (Path): The path to the directory to print its structure.
        prefix (str): The prefix for formatting the directory structure.
    """
    print(f"📂 {Fore.BLUE}{path.name}/")
    list_dir = list(path.iterdir())
    for index, item in enumerate(list_dir):
        is_last = index == len(list_dir) - 1
        print(prefix + (" ┗" if is_last else " ┣"), end="")
        if item.is_dir():
            get_dir_structure(item, prefix=prefix+('  ' if is_last else ' ┃'))
        else:
            print(f"📃 {Fore.GREEN}{item.name}")


def main() -> None:
    """
    The main function.
    """
    if len(sys.argv) != 2:
        print(Back.YELLOW + "Usage: python task_3.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    path = Path(directory)

    if not path.exists():
        print(f"{Back.RED}Error: '{directory}' does not exist.")
        sys.exit(1)

    if not path.is_dir():
        print(f"{Back.RED}Error: '{directory}' is not a directory.")
        sys.exit(1)

    get_dir_structure(path)
    print(Back.GREEN + "<<< Done! >>>")
    sys.exit(0)


if __name__ == "__main__":
    main()
