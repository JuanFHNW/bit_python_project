import datetime
import interface

#compare target date with the date of the tasks
def getTasksbyDate(tasks, targetDate):
    foundTasks = []
    tasks.sort(key=lambda task: task['description'].lower())
    for task in tasks:
        taskDate = datetime.date.fromisoformat(task["date"])
        if taskDate == targetDate:
            foundTasks.append(task)
    return foundTasks

#compare search term with the description of the tasks
def getTasksbyDescription(tasks, searchTerm):
    foundTasks = []
    tasks.sort(key=lambda task: task['date'])
    for task in tasks:
        taskDescription = (task["description"])
        if searchTerm.upper() in taskDescription.upper():
            foundTasks.append(task)
    return foundTasks

# 0 = user wants to search for description, 1 = user wants to search for a date
def getMatchingTasks(tasks, userSearch):
    if userSearch == "0":
            while True:
                inputDesc = interface.getInputDescription("Write down the description of the task you want to search\n")
                if inputDesc == "1":
                    return None
                foundTasks = getTasksbyDescription(tasks, inputDesc)
                if foundTasks:
                    return foundTasks
                else:
                    interface.printMsg("No tasks matching this description were found. Please try again or type '1' to quit.\n")

    elif userSearch == "1":
        while True:
            inputDate = interface.getInputDate("Write down the date of the task you want to search\n", 1)
            if inputDate == "1":
                return None
            foundTasks = getTasksbyDate(tasks, inputDate)
            if foundTasks:
                return foundTasks
            else:
                interface.printMsg("No tasks matching this date were found. Please try again or type '1' to quit.")
    if not foundTasks:
        return None


def getSpecificTask(foundTasks,prompt):
    if len(foundTasks) == 1:
        interface.printMsg("This matching task was found: " + foundTasks[0]["date"] + ":  "+ foundTasks[0]["description"] )
        return foundTasks[0]
    else:
        while True:
            interface.printTasks(foundTasks, prompt, 1)
            #get user index for the task
            InputSpecTask = interface.getUserIndex(0, len(foundTasks)-1, f"Write the number (0 - {len(foundTasks)-1}) of the task you want to edit:  \n")
            interface.printMsg("The chosen task: " + foundTasks[InputSpecTask]["date"] + ":  "+ foundTasks[InputSpecTask]["description"] )
            return foundTasks[InputSpecTask]

if __name__ == "__main__":
    #for testing usage
    tasks = [{'date': '2026-09-15', 'description': 'Doctor appointment'}, {'date': '2025-12-25', 'description': 'Family appointment'}, {'date': '2025-12-25', 'description': 'dog appointment'}, {'date': '2028-11-11', 'description': 'friends and family appointment'}, {'date': '2030-12-29', 'description': 'new bird appointment'}, {'date': '2018-12-22', 'description': 'tessttt'}, {'date': '2025-05-03', 'description': 'peepd'}]
    foundTasks = getTasksbyDate(tasks, '2025.12.25')
