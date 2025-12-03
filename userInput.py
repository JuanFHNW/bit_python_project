import taskFunctions.searchUtlils as searchUtlil
from get_date import get_date

#asking user for a date input
#if parameter new = 1 then print is for a new date. Default is not new
def getTaskDateInput(new=0):
    while True:
        if new == 0:
            userInputDate = input("Write down the date in the following format: \nyyyy.mm.dd\n")
        elif new == 1:
            userInputDate = input("Write down the new date in the following format: \nyyyy.mm.dd\n")
        try:
            dateObj = get_date(userInputDate)
            return dateObj 
        except ValueError:
            print("Wrong input! Please use the format: yyyy.mm.dd")
            
def getNewTaskDescription():
        while True:
            userInputDesc = input(f"Write down the new description of the task you want to edit\n")
            if userInputDesc:
                return userInputDesc
            else:
                print("Your input can't be empty")


#asking user for the description of the task
#if parameter new = 1 then print is for a new description. Default is not new
def getTaskDescriptionInput(tasks, action):
    while True:
        userInputDesc = input(f"Write down the description of the task you want to {action}\n")
               
        foundTasks = searchUtlil.getTasksbyDescription(tasks, userInputDesc)
        
        if foundTasks:
            return foundTasks
        else:
            print("No tasks matching this description were found. Please try again or type '1' to quit.")

#asking user which exact task the action should apply to
def getSpecificTask(foundTasks):
    print("The follwing tasks were found. Write down the corresponding number for the task you want to edit. \n")
    while True:
        for i in range(len(foundTasks)):
            print(str(i) + "  " + foundTasks[i]["description"])
        userInputTask = input("Write the number of the task you want to edit: \n")
        #if correct input
        if int(userInputTask) < len(foundTasks):
            print("The chosen task: " + foundTasks[int(userInputTask)]["date"] + ":  "+ foundTasks[int(userInputTask)]["description"] )
            return foundTasks[int(userInputTask)]
        else:
            print(f"Please write a number between 1 and {len(foundTasks)}")
      

if __name__ == "__main__":
    inputDate = getTaskDateInput()
    inputDescription = getTaskDescriptionInput("edit")