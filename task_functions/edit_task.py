"""Module for editing tasks in the task tracker."""
import json_handler
import interface
import task_functions.utils.task_utils as task_utils


def edit_task():
    """Get user input and edit a task in the JSON file."""
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
    # Get specific task which should be edited
    selected_task = task_utils.get_specific_task(
        found_tasks,
        "The follwing tasks were found. Write down the corresponding number for the task you want to edit.\n"
    )

    # Get new date and description for the task which it will be updated to
    new_date = interface.get_input_date(
        "Write down the new date in the following format: \nyyyy.mm.dd\n"
    )
    new_desc = interface.get_input_description(
        "Write down the new description of the task:\n"
    )

    # Update the task
    json_handler.update_entry(selected_task, new_desc, new_date)
    interface.wait_for_user("You tasks is now updated press enter to continue\n")


if __name__ == "__main__":
    edit_task()
