import json
import get_date
import jsonHandler
import taskFunctions.searchUtlils as searchUtlils
import userInput

def editTask():
    #get json data
    tasks = jsonHandler.getJsonTasks()
    #get matching tasks depending user input
    foundTasks = userInput.getTaskDescriptionInput(tasks, "edit")
    if not foundTasks:
        return None

    #get the task which the user wants to edit
    if len(foundTasks) > 1:
        editTask = userInput.getSpecificTask(tasks)
    elif len(foundTasks) == 1:
        editTask = foundTasks[0]

    #get new date and description of the task which will be edited
    newDate = userInput.getTaskDateInput(1)
    newDesc = userInput.getNewTaskDescription()

    #update the task
    jsonHandler.updateEntry(editTask, newDesc, newDate)
       

if __name__ == "__main__":
    editTask()
