import json
import re
def addTask():
    while True:
        userInputDate = input("Write down the date you want to add to your task in the follwing format: \nyyyy.mm.dd\n")
        if re.fullmatch(r"\d{4}.\d{2}.\d{2}"):
            print(f"userinput data:  {userInputDate}")
            break
        else:
            print("Wrong input please use the format: yyyy.mm.dd")

    taskDescription = input("Write down the description of the task:\n")

    task = {
        "date": userInputDate.isoformat(),
        "description": taskDescription
        }
    #add task data to json file
    try:
        with open('taskData.json', "r+") as taskJson:
            taskFileJson = json.load(taskJson)
            taskFileJson ["task_details"].append(task)
            taskJson.seek(0)
            json.dump(taskFileJson, taskJson, indent=4)
            taskJson.truncate()
        print("Your task was added")
    except:
        print("There was an error storing the data")
 
 
if __name__ == "__main__":
    addTask()