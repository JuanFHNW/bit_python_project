"""Main entry point for the task tracker application."""
import task_functions.add_task as add_task
import task_functions.show_task as show_task
import task_functions.edit_task as edit_task
import task_functions.delete_task as delete_task
import index


def main():
    """Run the main event loop for the task tracker."""
    should_exit = False

    while not should_exit:
        user_action_home = index.show_home()
        match user_action_home:
            case 1:
                show_task.show_task()
            case 2:
                add_task.add_task()
            case 3:
                edit_task.edit_task()
            case 4:
                delete_task.delete_task()
            case 5:
                # Quit programme
                should_exit = True
                #sys.exit()


if __name__ == "__main__":
    main()
