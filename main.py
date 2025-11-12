import datetime
import json

#with open("scheduleData.json", "r") as scheduleFileJson:
  #  scheduleFiledata = json.load(scheduleFileJson)

def get_date(userInputDate):
    year, month, day = map(int, userInputDate.split('.'))
    userInputDate = datetime.date(year, month, day)
    return userInputDate
    #print(f"userinput data:  {userInputDate}")


def getUserAction():
    print("Hello user welcome to your schedule. \nDo you want to see your schedule or edit your schedule? \nPress 1 to see your schedule and 2 for edit your schedule.")
    userAction = input()

def showHome():
    print("Welcome to your schedule.")
    print("\n==== SCHEDULE PLANER MENU ====")
    print("1 Show your schedule")
    print("2 Add schedule")
    print("3 Edit schedule")
    print("4 Delete schedule")
    print("5 Exit")
    print("========================")

def showSchedule():
    try:
       # userInputDate = get_date(userInputDate)
        userInputDate = input("Write down the date you want to see your schedule in the follwing format: \nyyyy.mm.dd\n")
        year, month, day = map(int, userInputDate.split('.'))
        userInputDate = datetime.date(year, month, day)
        #print(f"userinput data:  {userInputDate}")
    except ValueError:
        print("Your input wasn't readable")

    #if userInputDate == datetime.date(2026,8,5):
     #   print("its your birthday then")
    #else:  
     #   print("no schedule on this date")
    foundTask = None
    try:
        with open('./scheduleData.json', "r") as taskJson:
            tasks = json.load(taskJson)
            for task in tasks:
                if (datetime.date(task["date"]) == userInputDate):
                    foundTask = task
    except:
        print("There was an error searching for data")
        
    if foundTask != None:
        print(f"You have this task on this date: {foundTask['description']}")
    else:
        print("You have no task on this date")

def addSchedule():
    userInputDate = input("Write down the date you want to add to your schedule in the follwing format: \nyyyy.mm.dd\n")
    try:
        userInputDate = get_date(userInputDate)
        #print(f"userinput data:  {userInputDate}")
    except:
        print("Your input wasn't readable")

    scheduleDescription = input("Write down the description of the task:\n")

    schedule = {
        "date": userInputDate.isoformat(),
        "description": scheduleDescription
    }
    #add schedule data to json file
    try:
        with open('scheduleData.json', "r+") as scheduleJson:
            scheduleFileJson = json.load(scheduleJson)
            scheduleFileJson ["schedule_details"].append(schedule)
            scheduleJson.seek(0)
            json.dump(scheduleFileJson, scheduleJson, indent=4)
            scheduleJson.truncate()
        print("Your task got added")
    except:
        print("There was an error storing the data")

    
exit == False

def main():
    while not exit:
        showHome()
        userActionHome = input("Chose an option 1-5\n")
        match userActionHome:
            case "1":
                showSchedule()
            case "2":
                addSchedule()
            case "3":
                editSchedule()
            case "4":
                deleteSchedule()
            case "5":
                exit = True       

if __name__ == "__main__":
    main()

