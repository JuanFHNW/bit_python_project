import jsonHandler
import interface
import taskFunctions.utils.taskUtils as taskUtils


def deleteTask():
    #get the tasks from the json data
    tasks = jsonHandler.getJsonTasks()
    
    #if user wants to search by description or date
    userSearch = interface.getUserIndex(0, 1,f"Type 0 to search for a description of your task or type 1 for a date\n")
    #get matching tasks depending user input description or date, if the return from the get function is null the user wants to quit
    foundTasks = taskUtils.getMatchingTasks(tasks, userSearch)
    if not foundTasks:
        return None
    #get the specific task which should be deleted
    selectedTask = taskUtils.getSpecificTask(foundTasks, "The follwing tasks were found. Write down the corresponding number for the task you want to edit. \n")

    userConfirm = interface.getUserIndex(1, 2,f"Are you sure you want to delete: {selectedTask['date']}: {selectedTask['description']}?\nType 1 to confirm and 2 to quit.\n")

    if userConfirm == 1:
        #delete the task
        jsonHandler.deleteEntry(selectedTask,tasks)
        interface.waitForUser("You tasks is now deleted press enter to continue\n")
    else:
        interface.printMsg("Action delete Task is cancelled\n")
        return None



    
if __name__ == "__main__":
    deleteTask()
