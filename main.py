import sys
import taskFunctions.addTask as addTask
import taskFunctions.showTask as showTask
import taskFunctions.editTask as editTask
import taskFunctions.deleteTask as deleteTask
import index as index


def main():
    exit = False    

    while exit == False:
        index.showHome()
        userActionHome = input("Chose an option 1-5\n")
        match userActionHome:
            case "1":
                showTask.showTask()
            case "2":
                addTask.addTask()
            case "3":
                editTask.editTask()
            case "4":
                deleteTask.deleteTask()
            case "5":
                #quit programme
                sys.exit()      

if __name__ == "__main__":
    main()
