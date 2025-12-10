# Task Tracker
A robust, console-based tool for managing daily tasks, designed with a focus on clean code structure, data validation, and persistent storage.

## 📝 Analysis

**Problem**
Users struggle to efficiently manage their daily tasks, such as homework, assignments and personal to-do's, because they don’t have a simple and reliable way to organize, edit, and save their tasks. Without the TaskTracker, users find it difficult to manage their workload and keep track of what needs to be done.

**Scenario**
TaskTracker offers a minimalist and efficient solution to this problem. A user opens the application in the console and immediately sees their most urgent tasks. They can add new entries with a due date and a description. The system ensures that no invalid data (e.g., dates in the past or empty descriptions) is entered. All changes are immediately saved in a local JSON file, ensuring data remains available even after restarting the computer.

**User stories:**
1. As a user, I want to be able to search for a date or a description of a stored task and view them so I can efficiently plan my activities.
2. As a user, I want to add a new task by providing both a valid future date and a non-empty description So that I can easily register all my future obligations and ensure that my data is valid from the start.
3. As a user, I want to find a specific task (after searching by date or description) and be able to update its date and description with new, validated information so that I can keep my schedule flexible and up-to-date when plans change, without needing to create a new task.
4. As a user, I want to easily select and delete specific tasks, so I can remove completed or outdated entries and keep my workload focused and free of clutter.
5. As a user, I want to be certain that all my tasks are automatically saved and immediately available and displayed when I restart the application, so I never lose my workload data.
6. As a user, I want tasks that are older than "today" to be deleted automatically when I start the app, so that my dashboard is not disturbed with irrelevant history.
7. As a user, I want the option to cancel/quit an action (by typing '1') while I am entering data, so that I am not forced to finish a task entry if I change my mind.
8. As a user, I want to see a dashboard of the next 3 tasks immediately upon opening the app, so I get a quick status update without clicking through menus.

## ⚙️ Use Cases

The following Use Cases describe the exact interaction flow between the User and the System, including valid inputs and error handling.

### UC1: Start Dashboard & Auto-Cleanup (Covers Stories 5, 6, 8)
* **Actor:** User / System
* **Preconditions:** `task_data.json` exists (or is created).
* **Flow:**
    1.  User starts the program (System runs `main.py`).
    2.  **System** automatically scans for tasks where the date is older than `today`.
    3.  **System** permanently removes these outdated tasks to clean up the database.
    4.  **System** loads the remaining tasks and sorts them chronologically.
    5.  **System** displays the **Main Menu** and the **next 3 upcoming tasks** under the header "Your upcoming tasks".
* **Alternative Flow:**
    * *No Tasks:* If the list is empty, the System displays "You have no tasks right now".

### UC2: Add New Task (Covers Stories 2, 5, 7)
* **Actor:** User
* **Preconditions:** Main Menu is active.
* **Flow:**
    1.  User selects Option `2` (**Add task**).
    2.  System prompts for the date (Format: `yyyy.mm.dd`).
    3.  User enters a valid date that is **today or in the future**.
    4.  System prompts for the description.
    5.  User enters a **non-empty** text description.
    6.  System saves the task persistently to `task_data.json`.
    7.  System confirms: "Your task is now added".
* **Alternative Flow (Cancel):**
    * User enters `1` during input. System aborts and returns to the Main Menu.
* **Alternative Flow (Invalid Input):**
    * User enters a past date or empty description. System displays an error (e.g., "The date can't be in the past") and repeats the prompt.

### UC3: Search & View Tasks (Covers Stories 1)
* **Actor:** User
* **Preconditions:** Main Menu is active.
* **Flow:**
    1.  User selects Option `1` (**Show your tasks**).
    2.  System asks for the search mode: `0` for **Description**, `1` for **Date**.
    3.  User selects a mode and enters the search term (e.g., "Groceries" or "2025.12.24").
    4.  System performs a **case-insensitive search**.
    5.  System lists all matching tasks with their details.
    6.  User presses Enter to return to the Main Menu.

### UC4: Edit Task (Covers Stories 3, 5, 7)
* **Actor:** User
* **Preconditions:** User wants to modify an existing entry.
* **Flow:**
    1.  User selects Option `3` (**Edit task**).
    2.  **Search Step:** User performs a search (as defined in **UC3**) to narrow down the list.
    3.  System displays matching tasks with **Index Numbers** (0, 1, 2...).
    4.  User enters the index of the task to modify.
    5.  System requests the **new date** and **new description** (with validation).
    6.  System overwrites the specific entry in the JSON file with the new data.
    7.  System confirms the update.

### UC5: Delete Task (Covers Stories 4, 5, 7)
* **Actor:** User
* **Preconditions:** User wants to remove an entry.
* **Flow:**
    1.  User selects Option `4` (**Delete task**).
    2.  **Search Step:** User performs a search to find the task.
    3.  User selects the task via its Index Number.
    4.  System asks for **explicit confirmation**: "Are you sure you want to delete: [Task Details]?".
    5.  User confirms by typing `1`.
    6.  System permanently deletes the task from `task_data.json`.
* **Alternative Flow (Abort):**
    * User types `2` at confirmation. System displays "Action delete Task is cancelled" and keeps the data.


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

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.
  
## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)

