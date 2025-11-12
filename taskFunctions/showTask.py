import get_date
import datetime
import json

def showTask():
    try:
        userInputDate = input("Write down the date you want to see your task in the follwing format: \nyyyy.mm.dd\n")
        year, month, day = map(int, userInputDate.split('.'))
        userInputDate = datetime.date(year, month, day)
    except ValueError:
        print("Your input wasn't readable")

    
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
         print(f"You have this task(s) on this date: {foundTask['description']}")

if __name__ == "__main__":
    showTask()
