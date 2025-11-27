import json
from datetime import date 
def addTask():
    while True:
        userInputDate = input("Write down the date you want to add to your task in the follwing format: \nyyyy.mm.dd\n")
        try:
            year, month, day = userInputDate.split('.')
            if len(year) == 4 and year.isdigit() and len(month) == 2 and month.isdigit() and len(day) == 2 and day.isdigit(): 
                year = int(year)
                month = int(month)
                day = int(day) 
                print(f"userinput data:  {userInputDate}")
                break
            else:
                print("Wrong input please use the format: yyyy.mm.dd")
        except ValueError:
            print("Wrong input!") 

    taskDescription = input("Write down the description of the task:\n")
    task = {
        "date": date(year, month, day).isoformat(),
        "description": taskDescription
        }
    #add task data to json file
    try:
        with open('taskData.json', "r+") as taskJson:
            taskFileJson = json.load(taskJson)
            taskFileJson.append(task)
            taskJson.seek(0)
            json.dump(taskFileJson, taskJson, indent=4)
            taskJson.truncate()
        print("Your task was added")
    except Exception as e:
        print("There was an error storing the data:", e)
 
if __name__ == "__main__":
    addTask()