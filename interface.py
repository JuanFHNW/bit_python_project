from taskFunctions.utils.taskUtils import getDate

def printHome():
    print("\n==== TASK PLANER MENU ====")
    print("1 Show your task")
    print("2 Add task")
    print("3 Edit task")
    print("4 Delete task")
    print("5 Exit")
    print("========================")

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

def printTasks(tasks, prompt):
    print(prompt)
    for i in range(len(tasks)):
        print(str(i) + "  "  + tasks[i]["date"] + ": " + tasks[i]["description"])
      
def printError(prompt):
    print("Error: " + prompt)  

def printMsg(prompt):
    print(prompt)

def getUserIndex(minLength, maxLength, prompt):
    while True: 
        InputIndex = input(prompt)
        try:
            if int(InputIndex) >= minLength and int(InputIndex) <= maxLength:
                return int(InputIndex)
            else:
                print(f"Please write a number between {minLength} and {maxLength}")
        except ValueError:
                print ("Invalid input. Try again.")

def UserInput(prompt):
    input(prompt)
    


   

if __name__ == "__main__":
    #testing
    testIndex = getUserIndex(0,10,"Type a number between 0 and 10")