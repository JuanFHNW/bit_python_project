import jsonHandler
import interface
import taskFunctions.utils.taskUtils as taskUtils

def showTask():

    #get the tasks from the json data
    tasks = jsonHandler.getJsonTasks()
    #if user wants to search by description or date
    userSearch = interface.getUserIndex(0, 1,f"Type 0 to search for a description of your task or type 1 for a date\n")
    #get matching tasks depending user input description or date, if the return from the get function is null the user wants to quit
    foundTasks = taskUtils.getMatchingTasks(tasks, userSearch)
    if not foundTasks:
        return None
    #print the tasks
    interface.printTasks(foundTasks, "You have this matching task(s):")
    interface.waitForUser()
    
if __name__ == "__main__":
    showTask()
