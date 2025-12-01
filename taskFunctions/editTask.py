import json
import get_date
 
def editTask():
    try:
        userInputDesc = input("Write down the name of the task you want to edit\n")
    except ValueError:
        print("Your input wasn't readable")

    foundTasks = []
    try:
        with open('./taskData.json', "r") as taskJson:
            tasks = json.load(taskJson)
            for task in tasks:
                task_description = (task["description"])
                if userInputDesc.upper() in task_description.upper():
                    foundTasks.append(task)
    except:
        print("There was an error searching for data")
  
    if not foundTasks:
        print("You have no task(s) on this date")
    else:
       # print("TESTT: " + foundTasks.l + type(foundTasks.len))
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

        print("Your chosen Task: " + editTask["date"] + "  "+ editTask["description"] )

        newDate = input("Write down the new date in the following format: \nyyyy.mm.dd\n")
        newDate = get_date(newDate)
        newDesc = input("Write down the new description\n")

        try:
            with open('./taskData.json', "r") as taskJson:
                jsTasks = json.loads(taskJson.read())
                
                for jsTask in jsTasks:
                    if newDesc == jsTask.get["description"]:
                        jsTasks.remove(jsTask)
                        break
        except:
            print("There was an error searching for data")

                

            


            

if __name__ == "__main__":
    editTask()
