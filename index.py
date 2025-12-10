import datetime
import jsonHandler
import interface

#delete tasks which are older than today
def deleteOldTasks():
    tasks = jsonHandler.getJsonTasks()

    today = datetime.date.today()
    tasksToKeep = []
    oldTasks = []
    #take the tasks from up to today and overwrite the json file
    for task in tasks:
        try:
            year, month, day = map(int, task["date"].split('-'))
            dateObj = datetime.date(year, month, day)
        except ValueError:
            interface.printError("Error date at analyzing the json file")
            continue
        if dateObj >= today:
            tasksToKeep.append(task)
        else:
            oldTasks.append(task)
    if task != tasksToKeep:
        if(jsonHandler.overwriteAllTasks(tasksToKeep)):
            for deletedTask in oldTasks:
                interface.printMsg(f"Task {deletedTask['date']}: {deletedTask['description']} deleted")
        else:
            interface.printError("Error at deleting old tasks")

def showHome():
    #delete tasks which are older than today
    deleteOldTasks()
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
