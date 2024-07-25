"""
Task 2. Read cats information from a file.
"""


def get_cats_info(path: str) -> list:
    """
    Reads a file containing cat information and returns a list of dictionaries
    containing the information for each cat.

    Args:
        path (str): The path to the file containing cat information.

    Returns:
        list: A list of dictionaries containing the information for each cat.
        If the file is not found or contains invalid data, returns an empty
        list.

    Raises:
        FileNotFoundError: If the file specified by `path` does not exist.
        ValueError: If the file contains invalid data.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_list = file.readlines()
            cats_info = []
            for cat in cats_list:
                if cat.strip():
                    try:
                        cat_id, name, age = cat.strip().split(',')
                        cats_info.append(
                            {"id": cat_id, "name": name, "age": int(age)}
                        )
                    except ValueError:
                        print(f"Invalid data in line: {cat.strip()}")
                        return []
            return cats_info
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid data in file: {path}")
        return []


if __name__ == "__main__":
    info = get_cats_info("./cats.txt")
    print(info)
