import datetime
import json
import taskFunctions.addTask as addTask
import taskFunctions.showTask as showTask
import taskFunctions.editTask as editTask
import taskFunctions.deleteTask as deleteTask
import get_date

def showHome():
    print("Welcome to your tasks.")
    print("\n==== TASK PLANER MENU ====")
    print("1 Show your task")
    print("2 Add task")
    print("3 Edit task")
    print("4 Delete task")
    print("5 Exit")
    print("========================")


def main():
    exit = False    

    while exit == False:
        showHome()
        userActionHome = input("Chose an option 1-5\n")
        match userActionHome:
            case "1":
                showTask.showTask()
            case "2":
                addTask.addTask()
            case "3":
                addTask.editTask()
            case "4":
                deleteTask.deleteTask()
            case "5":
                exit = True       

if __name__ == "__main__":
    main()
