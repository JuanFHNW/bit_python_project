"""Main module for the task tracker application."""
import datetime
import json_handler
import interface


def delete_old_tasks():
    """Delete tasks which are older than today."""
    tasks = json_handler.get_json_tasks()

    today = datetime.date.today()
    tasks_to_keep = []
    old_tasks = []
    # Take the tasks from up to today
    for task in tasks:
        try:
            year, month, day = map(int, task["date"].split('-'))
            date_obj = datetime.date(year, month, day)
        except ValueError:
            interface.print_error("Error date at analyzing the json file")
            continue
        if date_obj >= today:
            tasks_to_keep.append(task)
        else:
            old_tasks.append(task)
    # Overwrite json file if there are old tasks
    if tasks != tasks_to_keep:
        if json_handler.overwrite_all_tasks(tasks_to_keep):
            for deleted_task in old_tasks:
                interface.print_msg(
                    f"Task {deleted_task['date']}: {deleted_task['description']} deleted"
                )
        else:
            interface.print_error("Error at deleting old tasks")


def show_home():
    """Display home screen with upcoming tasks."""
    # Delete tasks which are older than today
    delete_old_tasks()
    tasks = json_handler.get_json_tasks()
    tasks.sort(key=lambda task: task['date'])

    if len(tasks) > 0:
        # Take the first 3 tasks
        upcoming_tasks = tasks[:3]
        interface.print_tasks(upcoming_tasks, "Your upcoming tasks: ")
    else:
        interface.print_msg("You have no tasks right now")
    interface.print_home()


if __name__ == "__main__":
    show_home()
