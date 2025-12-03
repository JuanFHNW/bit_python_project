import json

def getJsonTasks():
    try:
        with open('taskData.json', "r") as taskJson:
            tasks = json.load(taskJson)
            return tasks
    except FileNotFoundError:
        print("Error: File was not found")
        return []
    except json.JSONDecodeError:
        # If the file is corrupted, print error and start with an empty list
        print("Error: Task data file is corrupt (invalid JSON format). Starting with no tasks.")
        return []
    except:
        print("Error loading the JSON file")
        return []
    

def addEntries():
    return None

def updateEntry(editTask, newDesc, newDate):
    with open('taskData.json', "r") as taskJson:
        jsTasks = json.loads(taskJson.read())
            
        for jsTask in jsTasks:
            if editTask["description"] == jsTask.get("description") and editTask["date"] == jsTask.get("date"):
                jsTask["description"] = newDesc
                jsTask["date"] = newDate.isoformat()
                break
    with open('taskData.json', "w") as taskJson:
        json.dump(jsTasks, taskJson, indent=4)
        input("You tasks is now updated press enter to continue")    

if __name__ == "__main__":
    tasks = getJsonTasks()
    addEntries()
