import datetime

def getDate(userInputDate):
    year, month, day = map(int, userInputDate.split('.'))
    userInputDate = datetime.date(year, month, day)
    return userInputDate

if __name__ == "__main__":
    getDate("")
