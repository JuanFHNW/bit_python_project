import jsonHandler
import userInput

def addTask():
    #get user input of the date for the new task
    inputDate = userInput.getInputDate("Write down the date you want to add to your task in the following format: \nyyyy.mm.dd\n")
    #get user input of the description of the new task
    inputDescription = userInput.getInputDescription("Write down the description of the task:\n")
    newTask = {
        "date": inputDate.isoformat(),
        "description": inputDescription
        }
    #add task data to json file
    jsonHandler.addEntries(newTask)

 
if __name__ == "__main__":
    addTask()