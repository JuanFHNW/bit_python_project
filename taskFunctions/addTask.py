import json
import get_date


def addTask():
    print("test adtask")
    userInputDate = input(
        "Write down the date you want to add to your task in the follwing format: \nyyyy.mm.dd\n")
    try:
        userInputDate = get_date(userInputDate)
        # print(f"userinput data:  {userInputDate}")
    except:
        print("Your input wasn't readable. Please try again")

    taskDescription = input("Write down the description of the task:\n")

    task = {
        "date": userInputDate.isoformat(),
        "description": taskDescription
    }
    # add task data to json file
    try:
        with open('taskData.json', "r+") as taskJson:
            taskFileJson = json.load(taskJson)
            taskFileJson["task_details"].append(task)
            taskJson.seek(0)
            json.dump(taskFileJson, taskJson, indent=4)
            taskJson.truncate()
        print("Your task was added")
    except:
        print("There was an error storing the data")

        print("There was an error storing the data")


if __name__ == "__main__":
    addTask()
