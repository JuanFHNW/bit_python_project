"""Task utility functions for searching and filtering tasks."""
import datetime
import interface


def get_tasks_by_date(tasks, target_date):
    """Compare target date with the date of the tasks."""
    found_tasks = []
    tasks.sort(key=lambda task: task['description'].lower())
    for task in tasks:
        task_date = datetime.date.fromisoformat(task["date"])
        if task_date == target_date:
            found_tasks.append(task)
    return found_tasks


def get_tasks_by_description(tasks, search_term):
    """Compare search term with the description of the tasks."""
    found_tasks = []
    tasks.sort(key=lambda task: task['date'])
    for task in tasks:
        task_description = (task["description"])
        if search_term.upper() in task_description.upper():
            found_tasks.append(task)
    return found_tasks


def get_matching_tasks(tasks, user_search):
    """Get matching tasks based on user search preference.
    
    Args:
        tasks: List of task dictionaries
        user_search: 0 for description search, 1 for date search
        
    Returns:
        List of matching tasks or None
    """
    found_tasks = None
    if user_search == 0:
        while True:
            input_desc = interface.getInputDescription(
                "Write down the description of the task you want to search\n"
            )
            if input_desc == "1":
                return None
            found_tasks = get_tasks_by_description(tasks, input_desc)
            if found_tasks:
                return found_tasks
            interface.print_msg(
                "No tasks matching this description were found. "
                "Please try again or type '1' to quit."
            )

    elif user_search == 1:
        while True:
            input_date = interface.get_input_date(
                "Write down the date of the task you want to search\n", 1
            )
            if input_date == "1":
                return None
            found_tasks = get_tasks_by_date(tasks, input_date)
            if found_tasks:
                return found_tasks
            interface.print_msg(
                "No tasks matching this date were found. "
                "Please try again or type '1' to quit."
            )
    if not found_tasks:
        return None


def get_specific_task(found_tasks, prompt):
    """Get a specific task from a list of found tasks.
    
    Args:
        found_tasks: List of task dictionaries
        prompt: Prompt message to display
        
    Returns:
        The selected task dictionary
    """
    if len(found_tasks) == 1:
        task_msg = (
            f"This matching task was found: {found_tasks[0]['date']}: "
            f"{found_tasks[0]['description']}"
        )
        interface.print_msg(task_msg)
        return found_tasks[0]
    
    while True:
        interface.print_tasks(found_tasks, prompt, 1)
        # Get user index for the task
        input_spec_task = interface.get_user_index(
            0, len(found_tasks) - 1,
            f"Write the number (0 - {len(found_tasks) - 1}) "
            f"of the task you want to edit:\n"
        )
        task_msg = (
            f"The chosen task: {found_tasks[input_spec_task]['date']}: "
            f"{found_tasks[input_spec_task]['description']}"
        )
        interface.print_msg(task_msg)
        return found_tasks[input_spec_task]

if __name__ == "__main__":
    # For testing usage
    tasks = [
        {'date': '2026-09-15', 'description': 'Doctor appointment'},
        {'date': '2025-12-25', 'description': 'Family appointment'},
        {'date': '2025-12-25', 'description': 'dog appointment'},
        {'date': '2028-11-11', 'description': 'friends and family appointment'},
        {'date': '2030-12-29', 'description': 'new bird appointment'},
        {'date': '2018-12-22', 'description': 'tessttt'},
        {'date': '2025-05-03', 'description': 'peepd'}
    ]
    found_tasks = get_tasks_by_date(tasks, '2025.12.25')
