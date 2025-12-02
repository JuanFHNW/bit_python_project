import json
import get_date
 
def editTask():
    try:
        userInputDesc = input("Write down the name of the task you want to edit\n")
    except ValueError:
        print("Your input wasn't readable")
    #load json data
    try:
        with open('./taskData.json', "r") as taskJson:
            tasks = json.load(taskJson)
    except FileNotFoundError:
        print("Error: File was not found")
    except:
        print("Error loading the JSON file")

    foundTasks = []
    while True:
        for task in tasks:
            task_description = (task["description"])
            if userInputDesc.upper() in task_description.upper():
                foundTasks.append(task)

        if not foundTasks:
            print("You have no tasks like this name")
        else:
            break

    if len(foundTasks) > 1:
        emFoundTask = enumerate(foundTasks)
        print("The follwing tasks were found. Write down the corresponding number for the task you want to edit. \n")
        for i in range(len(foundTasks)):
            print( str(i) + "  " + foundTasks[i]["description"])
            #print("[" + str(emFoundTask) + "] " + foundTask)
        userInputTask = input("Write the number of the task you want to edit: \n")
        if int(userInputTask) < len(foundTasks):
            editTask = foundTasks[int(userInputTask)]
        else:
            print("NOO GOOD")
    elif foundTasks.count == 1:
        editTask = foundTasks[0]

    print("Your chosen Taskk: " + editTask["date"] + ":  "+ editTask["description"] )

    newDate = input("Write down the new date in the following format: \nyyyy.mm.dd\n")
    newDate = get_date.get_date(newDate)
    newDesc = input("Write down the new description\n")

    #try:
    with open('./taskData.json', "r") as taskJson:
        jsTasks = json.loads(taskJson.read())
            
        for jsTask in jsTasks:
            if editTask["description"] == jsTask.get("description") and editTask["date"] == jsTask.get("date"):
                jsTask["description"] = newDesc
                jsTask["date"] = newDate.isoformat()
                break
    with open('./taskData.json', "w") as taskJson:
        json.dump(jsTasks, taskJson, indent=4)
        input("You tasks is now updated press enter to continue")
    # except:
    #    print("There was an error searching for data")

        

if __name__ == "__main__":
    editTask()
