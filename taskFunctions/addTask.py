import jsonHandler
import interface

def addTask():
    #get user input of the date for the new task
    inputDate = interface.getInputDate("Write down the date you want to add to your task in the following format: \nyyyy.mm.dd\n")
    #get user input of the description of the new task
    inputDescription = interface.getInputDescription("Write down the description of the task:\n")
    newTask = {
        "date": inputDate.isoformat(),
        "description": inputDescription
        }
    #add task data to json file
    jsonHandler.addEntries(newTask)
    interface.waitForUser("You tasks is now added press enter to continue\n")   

 
if __name__ == "__main__":
    addTask()