import jsonHandler as jsonHandler
import interface as interface
import taskFunctions.utils.taskUtils as taskUtils


def deleteTask():
    #get the tasks from the json data
    tasks = jsonHandler.getJsonTasks()
    
    #if user wants to search by description or date
    userSearch = interface.getDateOrDescription()
    #get matching tasks depending user input description or date, if the return from the get function is null the user wants to quit
    foundTasks = taskUtils.getMatchingTasks(tasks, userSearch)
    if not foundTasks:
        return None
    #get the specific task which should be deleted
    deleteTask = taskUtils.getSpecificTask(foundTasks, "The follwing tasks were found. Write down the corresponding number for the task you want to edit. \n")

    #delete the task
    jsonHandler.deleteEntry(deleteTask,tasks)

    
if __name__ == "__main__":
    deleteTask()
