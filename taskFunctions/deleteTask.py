"""Module for deleting tasks from the task tracker."""
import jsonHandler
import interface
import taskFunctions.utils.taskUtils as taskUtils


def delete_task():
    """Get user input and delete a task from the JSON file."""
    # Get the tasks from the json data
    tasks = jsonHandler.get_json_tasks()

    # If user wants to search by description or date
    user_search = interface.get_user_index(
        0, 1,
        "Type 0 to search for a description of your task or type 1 for a date\n"
    )
    # Get matching tasks depending on user input (description or date)
    # If the return from the get function is None, the user wants to quit
    found_tasks = taskUtils.get_matching_tasks(tasks, user_search)
    if not found_tasks:
        return None
    # Get the specific task which should be deleted
    selected_task = taskUtils.get_specific_task(
        found_tasks,
        "The follwing tasks were found. Write down the corresponding number for the task you want to edit. \n"
    )

    user_confirm = interface.get_user_index(
        1, 2,
        f"Are you sure you want to delete: {selected_task['date']}: {selected_task['description']}?\n"
        f"Type 1 to confirm and 2 to quit.\n"
    )

    if user_confirm == 1:
        # Delete the task
        jsonHandler.delete_entry(selected_task, tasks)
        interface.wait_for_user("You tasks is now deleted press enter to continue\n")
    else:
        interface.print_msg("Action delete Task is cancelled\n")
        return None


if __name__ == "__main__":
    delete_task()
