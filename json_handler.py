"""JSON handler for reading and writing task data."""
import json
import interface


def get_json_tasks():
    """Load tasks from the task_data.json file.
    
    Returns:
        list: List of task dictionaries or empty list if file not found/corrupted.
    """
    try:
        with open('task_data.json', "r") as task_json:
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
    except OSError as e:
        # Handles PermissionError, disk full, etc.
        interface.print_error(f"System error while saving data: {e}")
        return []


def add_entry(task):
    """Add a new task entry to the JSON file.
    
    Args:
        task (ictionary): Task dictionary to add.
    """
    try:
        with open('task_data.json', "r+") as task_json:
            task_file_json = json.load(task_json)
            task_file_json.append(task)
            task_json.seek(0)
            json.dump(task_file_json, task_json, indent=4)
            task_json.truncate()
    except FileNotFoundError:
        interface.print_error("Task data file not found. Could not add entry.")
    except json.JSONDecodeError:
        interface.print_error("Task data file is corrupt. Could not add entry.")
    except OSError as e:
        # Handles PermissionError, disk full, etc.
        interface.print_error(f"System error while saving data: {e}")


def update_entry(edit_task, new_desc, new_date):
    """Update an existing task entry in the JSON file.
    
    Args:
        edit_task (dictionary): Task dictionary to find and update.
        new_desc (str): New description for the task.
        new_date (str): New date for the task.
    """
    try:
        with open('task_data.json', "r+") as task_json:  # Read and write the file
            js_tasks = json.load(task_json)
            task_updated = False
            # Search for the matching task
            for js_task in js_tasks:
                if (edit_task["description"] == js_task.get("description") and
                        edit_task["date"] == js_task.get("date")):
                    js_task["description"] = new_desc
                    js_task["date"] = new_date.isoformat()
                    task_updated = True
                    break
            # Only rewrite the file if a change actually happened
            if task_updated:
                task_json.seek(0)
                json.dump(js_tasks, task_json, indent=4)
                task_json.truncate()
            else:
                interface.print_error("Task not found. No changes saved.")

    except FileNotFoundError:
        interface.print_error("Task data file not found. Could not update entry.")
    except json.JSONDecodeError:
        interface.print_error("Task data file is corrupt. Could not update entry.")
    except OSError as e:
        # Handles PermissionError, disk full, etc.
        interface.print_error(f"System error while updating data: {e}")


def delete_entry(del_task, tasks):
    """Delete a task entry from the JSON file.  
    Args:
        del_task (dictionary): Task dictionary to delete.
        tasks (list): List of all tasks.
    """
    # Search for the matching task to delete
    erase_task = next(
        (i for i, item in enumerate(tasks)
         if item["date"] == del_task["date"] and
         item["description"] == del_task["description"]),
        None
    )
    # Delete the task
    if erase_task is not None:
        del tasks[erase_task]
        interface.print_msg("Task deleted")
    else:
        interface.print_error("No task found")

    try:
        with open('task_data.json', "w") as task_json:
            json.dump(tasks, task_json, indent=4)
            task_json.truncate()
    except FileNotFoundError:
        interface.print_error("Task data file not found. Could not delete entry.")
    except json.JSONDecodeError:
        interface.print_error("Task data file is corrupt. Could not delete entry.")
    except OSError as e:
        # Handles PermissionError, disk full, etc.
        interface.print_error(f"System error while saving data: {e}")

def overwrite_all_tasks(tasks):
    """Overwrite all tasks in the JSON file.
    
    Args:
        tasks (list): List of task dictionaries to write.
        
    Returns:
        boolean: True if successful, False otherwise.
    """
    try:
        with open('task_data.json', "w") as task_json:
            json.dump(tasks, task_json, indent=4)

    except FileNotFoundError:
        interface.print_error("Task data file not found. Could not overwrite entry.")
        return False
    except json.JSONDecodeError:
        interface.print_error("Task data file is corrupt. Could not overwrite entry.")
        return False
    except OSError as e:
        # Handles PermissionError, disk full, etc.
        interface.print_error(f"System error while saving data: {e}")
        return False
    return True


if __name__ == "__main__":
    tasks = get_json_tasks()
    # add_entries() example
