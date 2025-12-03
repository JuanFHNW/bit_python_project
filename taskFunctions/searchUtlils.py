def getTasksbyDate(tasks_list, target_date):
    return None

def getTasksbyDescription(tasks, searchTerm):
    foundTasks = []
    for task in tasks:
        taskDescription = (task["description"])
        if searchTerm.upper() in taskDescription.upper():
            foundTasks.append(task)
    return foundTasks

if __name__ == "__main__":
    foundTasks = getTasksbyDate()
    foundTasks = getTasksbyDescription()
