import json
import interface

def getJsonTasks():
    try:
        with open('taskData.json', "r") as taskJson:
            tasks = json.load(taskJson)
            return tasks
    except FileNotFoundError:
        interface.printError("File was not found")
        return []
    except json.JSONDecodeError:
        # If the file is corrupted, print error and start with an empty list
        interface.printError("Task data file is corrupt (invalid JSON format). Starting with no tasks.")
        return []
    except:
        interface.printError("loading the JSON file")
        return []
    

def addEntries(task):
    try:
        with open('taskData.json', "r+") as taskJson:
            taskFileJson = json.load(taskJson)
            taskFileJson.append(task)
            taskJson.seek(0)
            json.dump(taskFileJson, taskJson, indent=4)
            taskJson.truncate()
    except Exception as e:
        interface.printError("There was an error storing the data:", e)
 


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
        
def deleteEntry(delTask,tasks):
    eraseTask = next((i for i, item in enumerate(tasks)
        if item["date"] == delTask["date"] and item["description"] == delTask["description"]),
        None)
    
    if eraseTask is not None:
        del tasks[eraseTask]
        interface.printMsg("Task deleted")
    else:
        interface.printError("No task found")
    
    try:
        with open('taskData.json', "w") as taskJson:
            json.dump(tasks, taskJson, indent=4)
            taskJson.truncate()
    except Exception as e:
        interface.printError("There was an error deleting the data: ", e)

#overwrite the whole tasks in the json file
def overwriteAllTasks(tasks):   
    try:
        with open('taskData.json', "w") as taskJson:
            json.dump(tasks, taskJson, indent=4)
        
    except Exception as e:
        interface.printError(f"Error overwriting the tasks: {e}")
        return False
    return True
        

if __name__ == "__main__":
    tasks = getJsonTasks()
    addEntries()
