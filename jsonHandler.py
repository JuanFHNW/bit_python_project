"""JSON handler for reading and writing task data."""
import json
import interface


def get_json_tasks():
    """Load tasks from the taskData.json file.
    
    Returns:
        List of task dictionaries or empty list if file not found/corrupted.
    """
    try:
        with open('taskData.json', "r") as task_json:
            tasks = json.load(task_json)
            return tasks
    except FileNotFoundError:
        interface.print_error("File was not found")
        return []
    except json.JSONDecodeError:
        # If the file is corrupted, print error and start with empty list
        interface.print_error(
            "Task data file is corrupt (invalid JSON format). "
            "Starting with no tasks."
        )
        return []
    except Exception as e:
        interface.print_error(f"Error loading the JSON file: {e}")
        return []


def add_entries(task):
    """Add a new task entry to the JSON file.
    
    Args:
        task: Task dictionary to add.
    """
    try:
        with open('taskData.json', "r+") as task_json:
            task_file_json = json.load(task_json)
            task_file_json.append(task)
            task_json.seek(0)
            json.dump(task_file_json, task_json, indent=4)
            task_json.truncate()
    except Exception as e:
        interface.print_error(f"There was an error storing the data: {e}")


def update_entry(edit_task, new_desc, new_date):
    """Update an existing task entry in the JSON file.
    
    Args:
        edit_task: Task dictionary to find and update.
        new_desc: New description for the task.
        new_date: New date for the task.
    """
    with open('taskData.json', "r") as task_json:
        js_tasks = json.loads(task_json.read())

        for js_task in js_tasks:
            if (edit_task["description"] == js_task.get("description") and
                    edit_task["date"] == js_task.get("date")):
                js_task["description"] = new_desc
                js_task["date"] = new_date.isoformat()
                break
    with open('taskData.json', "w") as task_json:
        json.dump(js_tasks, task_json, indent=4)


def delete_entry(del_task, tasks):
    """Delete a task entry from the JSON file.
    
    Args:
        del_task: Task dictionary to delete.
        tasks: List of all tasks.
    """
    erase_task = next(
        (i for i, item in enumerate(tasks)
         if item["date"] == del_task["date"] and
         item["description"] == del_task["description"]),
        None
    )

    if erase_task is not None:
        del tasks[erase_task]
        interface.print_msg("Task deleted")
    else:
        interface.print_error("No task found")

    try:
        with open('taskData.json', "w") as task_json:
            json.dump(tasks, task_json, indent=4)
            task_json.truncate()
    except Exception as e:
        interface.print_error(f"There was an error deleting the data: {e}")


def overwrite_all_tasks(tasks):
    """Overwrite all tasks in the JSON file.
    
    Args:
        tasks: List of task dictionaries to write.
        
    Returns:
        True if successful, False otherwise.
    """   
    try:
        with open('taskData.json', "w") as task_json:
            json.dump(tasks, task_json, indent=4)

    except Exception as e:
        interface.print_error(f"Error overwriting the tasks: {e}")
        return False
    return True


if __name__ == "__main__":
    tasks = get_json_tasks()
    # add_entries() example
