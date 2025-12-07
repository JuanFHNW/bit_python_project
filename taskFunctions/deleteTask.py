import jsonHandler
import userInput

def deleteTask():
    #get the tasks from the json data
    tasks = jsonHandler.getJsonTasks()
    
    #if user wants to search by description or date
    userSearch = userInput.getDateOrDescription()
    #get matching tasks depending user input description or date, if the return from the get function is null the user wants to quit
    if userSearch == "0":
        foundTasks = userInput.getMatchingTaskDescription(tasks, "Write down the description of the task you want to delete\n")
    elif userSearch == "1":
        foundTasks = userInput.getMatchingTaskDate(tasks, "Write down the date you want to delete in the following format: \nyyyy.mm.dd\n")
    if not foundTasks:
        return None

    #get the specific tasks which the user wants to delete
    byeDescription = userInput.getSpecificTask(foundTasks,"The follwing tasks were found. Write down the corresponding number for the task you want to delete. \n")
    #delete the task
    jsonHandler.deleteEntry(byeDescription,tasks)

    
if __name__ == "__main__":
    deleteTask()
