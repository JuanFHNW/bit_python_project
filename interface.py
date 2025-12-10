"""Utility functions for the interactive task interface."""

import datetime


def print_home():
    print("\n==== TASK PLANNER MENU ====")
    print("1. Show your tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. Delete task")
    print("5. Exit")
    print("==========================")


def get_input_date(prompt, allow_quit=False):
    """Prompt for a date in yyyy.mm.dd format.

    If ``allow_quit`` is True the user may enter the string "1" to quit.
    Returns a ``datetime.date`` on success or the string "1" when quitting.
    """
    today = datetime.date.today()
    while True:
        input_date = input(prompt)
        if allow_quit and input_date == "1":
            return input_date
        try:
            year, month, day = map(int, input_date.split('.'))
            date_obj = datetime.date(year, month, day)
            if date_obj >= today:
                return date_obj
            print("The date can't be in the past")
        except ValueError:
            print("Invalid input! Please use the format: yyyy.mm.dd")


def get_input_description(prompt):
    """Prompt for a non-empty description string."""
    while True:
        user_input_desc = input(prompt).strip()
        if user_input_desc:
            return user_input_desc
        print("Your input can't be empty")


def print_tasks(tasks, prompt, show_index=False):
    """Print a list of tasks.

    Each task is expected to be a dict containing the keys ``'date'`` and
    ``'description'``.
    """
    print(prompt)
    if show_index:
        for i, task in enumerate(tasks):
            print(f"{i}  {task['date']}: {task['description']}")
    else:
        for task in tasks:
            print(f"{task['date']}: {task['description']}")


def print_error(message):
    print(f"Error: {message}")


def print_msg(message):
    print(message)


def get_user_index(min_length, max_length, prompt):
    """Prompt for an integer index between ``min_length`` and ``max_length``.

    Both bounds are inclusive.
    """
    while True:
        input_index = input(prompt)
        try:
            idx = int(input_index)
            if min_length <= idx <= max_length:
                return idx
            print(f"Please write a number between {min_length} and {max_length}")
        except ValueError:
            print("Invalid input. Try again.")


def wait_for_user(prompt):
    input(prompt)


if __name__ == "__main__":
    # testing
    # test_index = get_user_index(0, 10, "Type a number between 0 and 10")
    user_date = get_input_date("Type a date\n")
    print(user_date)