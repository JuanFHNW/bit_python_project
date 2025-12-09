import jsonHandler as jsonHandler
import interface

def showHome():

    tasks = jsonHandler.getJsonTasks()
    tasks.sort(key=lambda task: task['date'])

    if len(tasks) > 0:
        #take the first 3 tasks
        upcomingTasks = tasks[:3]
        interface.printTasks(upcomingTasks,"Your upcoming tasks: ")
    else:
        interface.printMsg("You have no tasks right now")
    interface.printHome()

if __name__ == "__main__":
    showHome()
