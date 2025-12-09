import jsonHandler as jsonHandler
import interface



def showHome():
    interface.printMsg("Your upcoming tasks: ")

    tasks = jsonHandler.getJsonTasks()
    tasks.sort(key=lambda task: task['date'])
                #print up to the first 3 tasks 
    i = 0
    if len(tasks) > 0:
        while i <= len(tasks) and i < 3:
            interface.printMsg(tasks[i]["date"] + ": " + tasks[i]["description"])
            i = i+1
    else:
        interface.printMsg("You have no tasks right now")
    interface.printHome()

if __name__ == "__main__":
    showHome()
