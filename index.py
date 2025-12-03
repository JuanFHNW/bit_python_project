import json

def printNextTasks():
    try:
         with open('./taskData.json', "r") as taskJson:
            #load data and sort it by date
            tasks = json.load(taskJson)
            tasks.sort(key=lambda task: task['date'])
            #print the up to the first 3 tasks 
            i = 0
            if len(tasks) > 0:
                while i <= len(tasks) and i < 3:
                    print(tasks[i]["date"] + ": " + tasks[i]["description"])
                    i = i+1
            else:
                print("You have no tasks right now")
    except:
        print("Error loading your next tasks")


def showHome():
    print("Your upcoming tasks: ")
    printNextTasks()
    print("\n==== TASK PLANER MENU ====")
    print("1 Show your task")
    print("2 Add task")
    print("3 Edit task")
    print("4 Delete task")
    print("5 Exit")
    print("========================")

if __name__ == "__main__":
    showHome()
