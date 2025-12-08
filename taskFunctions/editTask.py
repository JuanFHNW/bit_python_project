import jsonHandler
import taskFunctions.processHelpFunctions.userInteraction as userInteraction

def editTask():
    #get the tasks from the json data
    tasks = jsonHandler.getJsonTasks()
    #if user wants to search by description or date
    userSearch = userInteraction.getDateOrDescription()
    #get matching tasks depending user input description or date, if the return from the get function is null the user wants to quit
    if userSearch == "0":
        foundTasks = userInteraction.getMatchingTaskDescription(tasks, "Write down the description of the task you want to edit\n")
    elif userSearch == "1":
        foundTasks = userInteraction.getMatchingTaskDate(tasks, "Write down the date you want to edit in the following format: \nyyyy.mm.dd\n")
    if not foundTasks:
        return None

    #get the exactly task which the user wants to edit
    editTask = userInteraction.getSpecificTask(foundTasks,"The follwing tasks were found. Write down the corresponding number for the task you want to edit. \n")

    #get new date and description of the task which to which it will be updated
    newDate = userInteraction.getInputDate("Write down the new date in the following format: \nyyyy.mm.dd\n")
    newDesc = userInteraction.getInputDescription("Write down the new description of the task: \n")

    #update the task
    jsonHandler.updateEntry(editTask, newDesc, newDate)
       
if __name__ == "__main__":
    editTask()
