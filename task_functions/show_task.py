"""Module for showing tasks in the task tracker."""
import json_handler
import interface
import task_functions.utils.task_utils as task_utils


def show_task():
    """Get user input and display matching tasks."""
    # Get the tasks from the json data
    tasks = json_handler.get_json_tasks()
    # If user wants to search by description or date
    user_search = interface.get_user_index(
        0, 1,
        "Type 0 to search for a description of your task or type 1 for a date\n"
    )
    # Get matching tasks depending on user input (description or date)
    # If the return from the get function is None, the user wants to quit
    found_tasks = task_utils.get_matching_tasks(tasks, user_search)
    if not found_tasks:
        return None
    # Print the tasks
    interface.print_tasks(found_tasks, "You have this matching task(s):")
    interface.wait_for_user("Press enter to continue\n")


if __name__ == "__main__":
    show_task()
