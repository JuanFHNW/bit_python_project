# TaskTracker

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.


## 📝 Analysis

**Problem**
Users struggle to efficiently manage their daily tasks, such as homework, assignments and personal to-do's, because they don’t have a simple and reliable way to organize, edit, and save their tasks. Without the TaskTracker, users find it difficult to manage their workload and keep track of what needs to be done.

**Scenario**
TaskTracker helps users to track their tasks by letting them add, edit or delete them. Each entry includes a title, description, date, and time. The system ensures input validation (preventing empty or invalid entries, for example: for date and time users can only use numbers in the following format yyyy.mm.dd.). The program also includes data persistence, so users never lose their tasks, even after restarting the app. Once tasks are set, they will always be available and displayed to users whenever they open the application.

**User stories:**
1. As a user, I want to view my stored tasks (including description and date) sorted by date, so I can efficiently plan my activities and easily see what's today's tasks or on a specific day.
2. As a user, I want to add or modify tasks to keep my schedule accurate and up to date.
3. As a user, I want to easily select and delete specific tasks, so I can remove completed or outdated entries and keep my workload focused and up-to-date.
4. As a user, I want to add a new task with a description and a date and be notified if I leave any required fields empty or use invalid input.
5. As a user, I want to be certain that all my tasks are automatically saved and immediately available and displayed when I restart the application, so I never lose my workload data.

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)


### 1. Interactive App (Console Input)

The application interacts with the user via the console. Users can:
- View the dashboard: Shows the next 3 upcoming tasks immediately upon start.
- Navigate the Menu: Choose options 1-5 to Show, Add, Edit, Delete, or Exit.
- Search interactively: When editing or deleting, users can choose to search by specific Date (1) or Description (0).

### 2. Data Validation

The application validates user input to ensure data integrity. 
This is primarily implemented in userInput.py and getDate.py:

Date Validation: When adding or editing a task, the input must match the format yyyy.mm.dd. 
The getInputDate function uses a try-except block to catch ValueError. If the format is wrong, it alerts the user:
```python
try:
 	dateObj = getDate(userInputDate)
 	return dateObj
 except ValueError:
 	print("Invalid input! Please use the format: yyyy.mm.dd")
 ```
Empty Input Checks: The program ensures task descriptions are not empty strings:
```python
if userInputDesc:
 	return userInputDesc
 else:
 	print("Your input can't be empty")
```

### 2. File processing

The application reads and writes data using the JSON format for structured storage:
Storage File: taskData.json — Stores an array of task objects.

Example structure:
```JSON
[
 	{
 		"date": "2026-09-15",
 		"description": "Doctor appointment"
 	},
 	{
 		"date": "2025-12-25",
 		"description": "Family appointment"
 	}
 ]
```
Reading Data: jsonHandler.getJsonTasks() opens the file in read mode ("r"). It includes error handling for FileNotFoundError (returns an empty list) and json.JSONDecodeError (handles corrupt files).

Writing/Updating Data:

addEntries: Appends new tasks and uses json.dump with indentation for readability.

updateEntry: Reads all tasks, finds the matching entry, modifies it, and rewrites the file.

deleteEntry: Removes the item from the list and truncates/rewrites the JSON file.

### Technology
- Python 3.12
- Environment: Visual Studio Code
- Standard Libraries: json, datetime, sys

### 📂 Repository Structure

```text

TaskTracker/
│
├── main.py                  # Entry point (Menu loop)
├── index.py                 # Dashboard/Home logic
├── interface.py             # UI Layer: Input/Output & Validierung
├── jsonHandler.py           # Data Layer: store/load
├── taskData.json            # Persistent data store
│
└── taskFunctions/           # Controller Layer 
    ├── addTask.py
    ├── editTask.py
    ├── deleteTask.py
    ├── showTask.py
    │
    └── utils/               # Logic layer (pure algorithm)
        └── taskUtils.py     # search, filter & selection-Workflows
```
### How to Run
1. Open the repository in Terminal
2. Open the Terminal
3. Run:
	```bash
	python3 main.py
	```
4. Follow the on-screen menu prompts.
   
### Libraries Used

json: Essential for parsing the taskData.json file to store tasks persistently as structured objects.
datetime: Used in getDate.py and sorting logic to ensure tasks are handled chronologically and formatted correctly (ISO format).
sys: Used in main.py to cleanly exit the application.


## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)

