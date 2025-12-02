import datetime
import json

def deleteTask():
    try:
        userInputDate = input("Write down the task you want to delete in the following format: \nyyyy.mm.dd\n")
        year, month, day = map(int, userInputDate.split('.'))
        userInputDate = datetime.date(year, month, day)
    except ValueError:
        print("Your input wasn't readable")
        return

    foundTask = []
    try:
        with open('./taskData.json', "r") as taskJson:
            tasks = json.load(taskJson)
            for task in tasks:
                task_date = datetime.date.fromisoformat(task["date"])
                if task_date == userInputDate:
                    foundTask.append(task)
    except:
        print("There was an error searching for data")
        
    if not foundTask:
        print("You have no task(s) on this date")
    else:
        print(f"You have this task(s) on this date:")
        for task in foundTask:
            print(f"{task['description']}")

    byeDescription = input("Type the description you want to delete:\n")
    
    eraseTask = next((i for i, item in enumerate(tasks)
        if item["date"] == userInputDate.isoformat() and item["description"] == byeDescription),
        None)
    
    if eraseTask is not None:
        del tasks[eraseTask]
        print("Task deleted")
    else:
        print("No task found")
    
    try:
        with open('taskData.json', "w") as taskJson:
            json.dump(tasks, taskJson, indent=4)
            taskJson.truncate()
    except Exception as e:
        print("There was an error deleating the data: ", e)
    
    while True:
        proceedCheck = input("\nType 1 to continue: ")
        if proceedCheck == "1":
            break
        else:
            print("Wrong input please type 1")
    
if __name__ == "__main__":
    deleteTask()
