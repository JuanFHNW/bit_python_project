"""Main entry point for the task tracker application."""
import sys
import taskFunctions.addTask as add_task
import taskFunctions.showTask as show_task
import taskFunctions.editTask as edit_task
import taskFunctions.deleteTask as delete_task
import index


def main():
    """Run the main event loop for the task tracker."""
    should_exit = False

    while not should_exit:
        index.show_home()
        user_action_home = input("Chose an option 1-5\n")
        match user_action_home:
            case "1":
                show_task.show_task()
            case "2":
                add_task.add_task()
            case "3":
                edit_task.edit_task()
            case "4":
                delete_task.delete_task()
            case "5":
                # Quit programme
                sys.exit()


if __name__ == "__main__":
    main()
