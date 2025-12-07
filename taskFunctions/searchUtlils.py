import datetime

#compare target date with the date of the tasks
def getTasksbyDate(tasks, targetDate):
    foundTasks = []
    tasks.sort(key=lambda task: task['description'].lower())
    targetDate = datetime.date.fromisoformat(targetDate.replace(".", "-"))

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

if __name__ == "__main__":
    #for testing usage
    tasks = [{'date': '2026-09-15', 'description': 'Doctor appointment'}, {'date': '2025-12-25', 'description': 'Family appointment'}, {'date': '2025-12-25', 'description': 'dog appointment'}, {'date': '2028-11-11', 'description': 'friends and family appointment'}, {'date': '2030-12-29', 'description': 'new bird appointment'}, {'date': '2018-12-22', 'description': 'tessttt'}, {'date': '2025-05-03', 'description': 'peepd'}]
    foundTasks = getTasksbyDate(tasks, '2025.12.25')
    foundTasks = getTasksbyDescription()
