# Task Tracker
A robust, console-based tool for managing daily tasks, designed with a focus on clean code structure, data validation, and persistent storage.

## 📝 Analysis & Context

**Problem**
Users struggle to efficiently manage their daily tasks, such as homework, assignments and personal to-do's, because they don’t have a simple and reliable way to organize, edit, and save their tasks. Without the TaskTracker, users find it difficult to manage their workload and keep track of what needs to be done.

**Scenario**
TaskTracker offers a minimalist and efficient solution to this problem. A user opens the application in the console and immediately sees their most urgent tasks. They can add new entries with a due date and a description. The system ensures that no invalid data (e.g., dates in the past or empty descriptions) is entered. All changes are immediately saved in a local JSON file, ensuring data remains available even after restarting the computer.

## 🚀 Key Features

* **Dashboard View:** Instantly shows the top 3 upcoming tasks upon launch.
* **Automatic Cleanup:** Tasks older than "today" are automatically deleted to keep the list fresh.
* **Smart Search:** Find tasks by searching for a specific **Date** or a keyword in the **Description**.
* **Data Validation:**
    * Prevents entering past dates.
    * Ensures descriptions are not empty.
    * Validates date formats (`yyyy.mm.dd`).
* **Persistence:** All data is saved to a JSON file (`task_data.json`) automatically.
* **Error Handling:** Gracefully handles corrupt data files or invalid user inputs without crashing.

**User stories:**
1.  **As a user**, I want to be able to **search for a date or a description** of a stored task and view them so I can efficiently plan my activities.
2.  **As a user**, I want to **add a new task** by providing both a valid future date and a non-empty description, so that I can ensure my schedule is accurate from the start.
3.  **As a user**, I want to **find a specific task** (via search) and **update its date or description** with new, validated information, allowing me to adapt to changing plans.
4.  **As a user**, I want to **select and delete specific tasks** easily, so I can remove completed or outdated entries and keep my workload focused.
5.  **As a user**, I want to be certain that **all my tasks are automatically saved** and restored when I restart the application, ensuring I never lose data.
6.  **As a user**, I want tasks that are **older than "today" to be deleted automatically** upon startup, keeping my dashboard free of irrelevant history.
7.  **As a user**, I want the option to **cancel/quit an action** (by typing '1') while entering data, so I am not forced to finish a task entry if I change my mind.
8.  **As a user**, I want to see a **dashboard of the next 3 tasks** immediately upon opening the app, providing a quick status update without navigating menus.

## ⚙️ Use Cases

The following Use Cases describe the exact interaction flow between the User and the System, including valid inputs and error handling.

### UC1: Launch & Auto-Cleanup
* **Trigger:** User runs `main.py`.
* **System Action:**
    1.  Loads data from `task_data.json`.
    2.  Compares task dates against `datetime.date.today()`.
    3.  **Auto-Deletes** any task strictly older than today.
    4.  Sorts the remaining tasks chronologically.
    5.  Displays the **Main Menu** and the **Top 3 Upcoming Tasks**.

### UC2: Add Task
* **Trigger:** User selects Option `2`.
* **Flow:**
    1.  System prompts for date (`yyyy.mm.dd`).
    2.  **Validation:** Checks if format is correct AND if date is $\ge$ today.
    3.  System prompts for description (must not be empty).
    4.  System appends the new task to the JSON file and confirms success.
* **Alternative:** User types `'1'` during input to **Cancel** and return to menu.

### UC3: Search & View
* **Trigger:** User selects Option `1`.
* **Flow:**
    1.  User chooses search mode: `0` (Description) or `1` (Date).
    2.  User enters search term (e.g., "Doctor" or "2025.12.24").
    3.  System performs a **case-insensitive search** using `task_utils.py`.
    4.  Displays all matching results.

### UC4: Edit Task
* **Trigger:** User selects Option `3`.
* **Flow:**
    1.  User performs a **Search** (see UC3) to isolate the task.
    2.  System lists matches with an **Index ID**.
    3.  User selects the ID of the task to edit.
    4.  System requests new Date and Description (with validation).
    5.  System overwrites the specific entry in the JSON file.

### UC5: Delete Task
* **Trigger:** User selects Option `4`.
* **Flow:**
    1.  User performs a **Search** to find the task.
    2.  User selects the ID of the task to delete.
    3.  **Safety Check:** System asks "Are you sure you want to delete...?"
    4.  User confirms with `'1'`.
    5.  System permanently removes the entry.


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

### 🏗️ Architecture & Design
This project follows the **Separation of Concerns** principle to ensure maintainability and testability. The application is divided into distinct layers:

```text

TaskTracker/
│
├── main.py                  # [Controller] Entry Point: Runs the main event loop & menu
├── index.py                 # [Controller] Dashboard Logic: Handles startup checks & auto-cleanup
├── interface.py             # [View] UI Layer: Handles all console output and user input
├── json_handler.py          # [Model] Data Layer: Pure backend logic for JSON Read/Write
├── task_data.json           # [Database] The persistent storage file
│
└── task_functions/          # [Logic] Feature Modules
    ├── add_task.py          # Workflow for creating tasks
    ├── edit_task.py         # Workflow for updating tasks
    ├── delete_task.py       # Workflow for removing tasks
    ├── show_task.py         # Workflow for searching/viewing
    │
    └── utils/
        └── task_utils.py    # [Helper] Algorithms for sorting & filtering
```
graph TD
    Start([Start Program]) --> MainLoop{Main Loop}
    MainLoop -->|1. Cleanup & Display| ShowHome[index.show_home]
    ShowHome --> UserInput[/User Input: Option 1-5/]
    
    UserInput -->|1| Show[show_task.show_task]
    UserInput -->|2| Add[add_task.add_task]
    UserInput -->|3| Edit[edit_task.edit_task]
    UserInput -->|4| Delete[delete_task.delete_task]
    UserInput -->|5| Exit([sys.exit])
    
    Show --> Wait[interface.wait_for_user]
    Add --> Wait
    Edit --> Wait
    Delete --> Wait
    
    Wait -->|Press Enter| MainLoop
    
    style Start fill:#98c379,stroke:#333,stroke-width:2px,color:black
    style Exit fill:#e06c75,stroke:#333,stroke-width:2px,color:black
    style MainLoop fill:#61afef,stroke:#333,stroke-width:2px,color:black

### 🏗️ Architecture Overview

Here is the functional call structure of the application:

![Function Call Diagram](assets/function_tree_task_tracker.drawio.png.png)

// Assuming you saved the image as 'function_tree.png' in an 'assets' folder

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

