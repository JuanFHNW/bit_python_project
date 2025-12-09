import jsonHandler as jsonHandler
import interface as interface
import taskFunctions.utils.taskUtils as taskUtils

def editTask():
    #get the tasks from the json data
    tasks = jsonHandler.getJsonTasks()
    #if user wants to search by description or date
    userSearch = interface.getDateOrDescription()
    #get matching tasks depending user input description or date, if the return from the get function is null the user wants to quit
    foundTasks = taskUtils.getMatchingTasks(tasks, userSearch)
    if not foundTasks:
        return None
    #get specific task which should be edited
    editTask = taskUtils.getSpecificTask(foundTasks, "The follwing tasks were found. Write down the corresponding number for the task you want to edit. \n")

    #get new date and description of the task which to which it will be updated
    newDate = interface.getInputDate("Write down the new date in the following format: \nyyyy.mm.dd\n")
    newDesc = interface.getInputDescription("Write down the new description of the task: \n")

    #update the task
    jsonHandler.updateEntry(editTask, newDesc, newDate)
       
if __name__ == "__main__":
    editTask()
