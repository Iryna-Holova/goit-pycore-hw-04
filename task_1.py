"""
Task 1. Calculate the total and average salary of employees from a given file.
"""


def total_salary(path: str) -> tuple:
    """
    Calculates the total and average salary of employees from a given file.

    Args:
        path (str): The path to the file containing employee salary
        information.

    Returns:
        tuple: A tuple containing the total salary and the average salary.
               If the file is not found or contains invalid data, returns
               (None, None).
               If there are no employees in the file, returns (None, None).

    Raises:
        FileNotFoundError: If the file specified by `path` does not exist.
        ValueError: If the file contains invalid data.
        ZeroDivisionError: If there are no employees in the file.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            employees_list = file.readlines()
            salary_list = [
                int(employee.split(',')[1])
                for employee in employees_list
                if employee.strip()
            ]
            if not salary_list:
                raise ZeroDivisionError

            total = sum(salary_list)
            average = total / len(salary_list)
            return total, average

    except FileNotFoundError:
        print(f"File not found: {path}")
        return None, None
    except ValueError:
        print(f"Invalid data in file: {path}")
        return None, None
    except ZeroDivisionError:
        print(f"No employees in file: {path}")
        return None, None


if __name__ == "__main__":
    total_s, average_s = total_salary("./salary.txt")
    print(f"Total salary: {total_s}, "
          f"Average salary: {average_s}")
