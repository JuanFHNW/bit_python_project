"""Module for adding new tasks to the task tracker."""
import json_handler
import interface


def add_task():
    """Get user input and add a new task to the JSON file."""
    # Get user input of the date for the new task
    input_date = interface.get_input_date(
        "Write down the date you want to add to your task in the "
        "following format: \nyyyy.mm.dd\n"
    )
    # Get user input of the description of the new task
    input_description = interface.get_input_description(
        "Write down the description of the task:\n"
    )
    new_task = {
        "date": input_date.isoformat(),
        "description": input_description
    }
    # Add task data to json file
    json_handler.add_entries(new_task)
    interface.wait_for_user("You tasks is now added press enter to continue\n")


if __name__ == "__main__":
    add_task()