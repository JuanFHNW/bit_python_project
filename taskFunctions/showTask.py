import jsonHandler
import taskFunctions.processHelpFunctions.userInteraction as userInteraction

def showTask():

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
    #print the tasks
    userInteraction.printTasks(foundTasks)
    

if __name__ == "__main__":
    showTask()
