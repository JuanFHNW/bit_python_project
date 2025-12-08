import taskFunctions.processHelpFunctions.searchUtlils as searchUtlil
from taskFunctions.processHelpFunctions.getDate import getDate

#asking user wethever the user wants to search for a date or description
def getDateOrDescription():
    while True:
        userInputSearch = input("Type 0 to search for a description of your task or type 1 for a date\n")
        if userInputSearch == "0":
            return userInputSearch
        elif userInputSearch == "1":
            return userInputSearch
        else:
            print("Please try again. Only number 0 and 1 are allowed.")

#asking user for a date input
def getInputDate(prompt):
    while True:
        userInputDate = input(prompt)
        try:
            dateObj = getDate(userInputDate)
            return dateObj 
        except ValueError:
            print("Invalid input! Please use the format: yyyy.mm.dd")

#asking user for a description            
def getInputDescription(prompt):
        while True:
            userInputDesc = input(prompt)
            if userInputDesc:
                return userInputDesc
            else:
                print("Your input can't be empty")


#asking user for the description of an existing task
#if the user press 1 the action quits
def getMatchingTaskDescription(tasks, prompt):
    while True:
        InputDesc = input(prompt)
        if InputDesc == "1":
            return None
        foundTasks = searchUtlil.getTasksbyDescription(tasks, InputDesc)
        if foundTasks:
            return foundTasks
        else:
            print("No tasks matching this description were found. Please try again or type '1' to quit.")

#asking user for the date of an existing task
def getMatchingTaskDate(tasks, prompt):
    while True:
        InputDate = input(prompt)
        if InputDate == "1":
            return None
        try:
            foundTasks = searchUtlil.getTasksbyDate(tasks, InputDate)
            if foundTasks:
                return foundTasks
            else:
                print("No tasks matching this date were found. Please try again or type '1' to quit.")
        except ValueError:
            print("Your input is invalid. Try again or type 1 to quit")


#asking user which exact task the action should apply to
def getSpecificTask(foundTasks,prompt):
    if len(foundTasks) == 1:
        print("This matching task was found: " + foundTasks[0]["date"] + ":  "+ foundTasks[0]["description"] )
        return foundTasks[0]
    else:
        print(prompt)
        while True:
            for i in range(len(foundTasks)):
                print(str(i) + "  "  + foundTasks[i]["date"] + ": " + foundTasks[i]["description"])
            userInputTask = input(f"Write the number (0 - {len(foundTasks)-1}) of the task you want to edit:  \n")
            #if correct input
            try:
                if int(userInputTask) < len(foundTasks):
                    print("The chosen task: " + foundTasks[int(userInputTask)]["date"] + ":  "+ foundTasks[int(userInputTask)]["description"] )
                    return foundTasks[int(userInputTask)]
                else:
                    print(f"Please write a number between 1 and {len(foundTasks)}")
            except ValueError:
                print("Invalid input. Try again.")

def printTasks(foundTasks):
    print("You have this matching task(s):")
    for task in foundTasks:
        print(f"{task['date']}: {task['description']}")
    input("Press enter to continue")    
   

if __name__ == "__main__":
    pass