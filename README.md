# 📝 Task Tracker

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Task Tracker** is a robust, console-based application designed to help students and professionals manage daily tasks efficiently. It focuses on clean architecture, strict data validation, and persistent storage using JSON.

---

## 📖 Table of Contents
- [Analysis & Context](#-analysis--context)
- [Key Features](#-key-features)
- [User Stories](#-user-stories)
- [Use Cases](#-use-cases)
- [Getting Started](#-getting-started)
- [Usage Guide](#-usage-guide)
- [Architecture & Design](#-architecture--design)
- [Project Requirements](#-project-requirements)
- [Team & Acknowledgments](#-team--acknowledgments)

---

## 🧐 Analysis & Context

### The Problem
Users often struggle to manage daily tasks-such as homework, assignments, and personal to-do's-because existing tools are polarized: they are either too complex with overwhelming features or too simple, lacking data persistence.

### Our Solution
**Task Tracker** offers a minimalist, reliable middle ground. It launches immediately into a dashboard of your most urgent tasks and ensures data integrity by validating all inputs. All changes are saved automatically to a local JSON file (`task_data.json`), ensuring data persists even after restarting the system.

---

## 🚀 Key Features

* **⚡ Instant Dashboard:** Immediately displays the top 3 upcoming tasks upon launch.
* **🧹 Auto-Cleanup Algorithm:** A silent startup check automatically deletes tasks strictly older than "today" to keep your list fresh.
* **💾 Persistence:** All data is stored in `task_data.json`, ensuring no data loss.
* **🔍 Smart Search:** Filter tasks by **Date** or **Description** keyword.
* **🛡️ Robust Validation:**
    * Prevents entering past dates.
    * Rejects empty descriptions.
    * Enforces `yyyy.mm.dd` format.
    * Handles corrupted files gracefully without crashing.

---

## 👤 User Stories

1.  **As a user**, I want to see a **dashboard of the next 3 tasks** immediately upon opening the app for a quick status update.
2.  **As a user**, I want to **add a new task** with a valid future date and description to keep my schedule accurate.
3.  **As a user**, I want to **search for a task** by date or description so I can efficiently plan my activities.
4.  **As a user**, I want to **edit specific tasks** to update their details as my plans change.
5.  **As a user**, I want to **delete completed or outdated tasks** to keep my workload focused.
6.  **As a user**, I want outdated tasks to be **automatically deleted** to keep my view clutter-free.
7.  **As a user**, I want the option to **cancel an action** (by typing '1') if I change my mind during input.
8.  **As a user**, I want my data **automatically saved** so I never lose my progress.

---

## ⚙️ Use Cases

### UC1: Launch & Auto-Cleanup
* **Trigger:** User runs `main.py`.
* **System Action:** Loads data, removes tasks older than `today`, sorts remaining tasks, and displays the **Main Menu** + **Top 3 Upcoming Tasks**.

### UC2: Add Task
* **Trigger:** User selects Option `2`.
* **Flow:** System prompts for date (`yyyy.mm.dd`) and description.
* **Validation:** Checks format and ensures date $\ge$ today. Confirms success upon saving.

### UC3: Search & View
* **Trigger:** User selects Option `1`.
* **Flow:** User chooses search mode (`0` for Description, `1` for Date) and enters query. System displays all matching results.

### UC4: Edit Task
* **Trigger:** User selects Option `3`.
* **Flow:** User searches for a task, selects it by ID, and provides new validated details. System overwrites the entry.

### UC5: Delete Task
* **Trigger:** User selects Option `4`.
* **Flow:** User finds a task, selects it, and confirms deletion. System permanently removes the entry.

---

## 💻 Getting Started

### Prerequisites
* Python 3.10 or higher (Developed on Python 3.12).
* **Git** (for cloning the repository).
* **No external packages required** (Uses standard libraries only: `json`, `datetime`, `sys`).

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/JuanFHNW/task_tracker.git
    cd task-tracker
    ```

2.  **Run the application**:
    ```bash
    python main.py
    ```

---

## 🕹️ Usage Guide

**Main Menu Interface:**
```text
Your upcoming tasks: 
2025-12-17: Programming presentation
2025-12-21: Submission essay
2025-12-25: Christmas


==== TASK TRACKER MENU ====
1. Show your tasks
2. Add task
3. Edit task
4. Delete task
5. Exit
==========================
```
## 💡 Pro Tips
* **Navigation:** Enter the number corresponding to the menu option (`1`-`5`).
* **Canceling:** Type `1` during any data entry prompt (like entering a date) to cancel the operation and return to the main menu.
* **Date Format:** Always use `yyyy.mm.dd` (e.g., `2025.12.25`).

---

## 🏗️ Architecture & Design
We followed the **Separation of Concerns** principle and the **IPO (Input-Process-Output)** model to ensure maintainability and clarity.

### File Structure
```text
TaskTracker/
│
├── main.py                  # Entry Point
├── index.py                 # Dashboard & Cleanup Logic
├── interface.py             # User Interface (Input/Output)
├── json_handler.py          # Data Persistence (JSON)
├── task_data.json           # Database
│
└── task_functions/          # Feature Modules
    ├── add_task.py
    ├── edit_task.py
    ├── delete_task.py
    └── show_task.py
```

### Visual Architecture
Below are the high-level diagrams illustrating our module dependencies and the function call hierarchy.

**Module Dependencies:**

![Module Dependency Diagram](assets/task_tracker_module_dependency.drawio.png)


**Function Call Tree:**

*Note: Due to the focus on clear and modular design, this diagram only includes the essential functions and omits low-level utility calls (like `print_msg` or `wait_for_user`).*

![Function Call Tree](assets/function_tree_task_tracker.drawio.png)

### Execution Flow Sketches
These timelines visualize exactly *when* each part of the code runs during key operations.

### Execution Flow Sketches (Detailed)
These timelines visualize the precise function-by-function flow for the application's key operations.

**1. App Launch & Auto-Cleanup**
This flow runs automatically whenever `main.py` calls `index.show_home()` to display the main menu.

1.  `Start (main.py)`
2.  → `index.show_home()`
3.  → `delete_old_tasks()`
    * → `json_handler.get_json_tasks()` (Load all tasks)
    * → (Loop compares dates against `datetime.date.today()`)
    * → `json_handler.overwrite_all_tasks()` (If tasks were deleted)
    * → `interface.print_msg()` (for each task deleted by cleanup)
4.  → `json_handler.get_json_tasks()` (Load tasks again for dashboard)
5.  → `tasks.sort()` (Sorts by date, using lambda function)
6.  → `interface.print_tasks()` / `interface.print_msg()` (Display dashboard)
7.  → `interface.print_home()` (Display main menu options)
8.  → `interface.get_user_index()` (Awaits and validates user action 1-5)

**2. Adding a Task (Menu Option 2)**
This flow handles gathering user input, validating it, and persisting the new entry.

1.  `User Selects "2"`
2.  → `add_task.add_task()`
3.  → `interface.get_input_date()` (Prompts user for and validates date)
4.  → `interface.get_input_description()` (Prompts user for and validates description)
5.  → `json_handler.add_entry()` (Reads, appends data, overwrites/truncates file)
6.  → `interface.wait_for_user()`
7.  → `End` (Returns to main menu)

**3. Searching & Editing a Task (Menu Option 3)**
This complex flow involves task retrieval, selection, new input validation, and file update.

1.  `User Selects "3"`
2.  → `edit_task.edit_task()`
3.  → `json_handler.get_json_tasks()`
4.  → `interface.get_user_index()` (User selects 0 for Description or 1 for Date search)
5.  → `task_utils.get_matching_tasks()` (Loops until a task is found or user quits)
    * → `interface.get_input_description()` OR `interface.get_input_date()`
    * → `task_utils.get_tasks_by_description()` OR `task_utils.get_tasks_by_date()`
    * → `interface.print_msg()` (if no matches found)
6.  → `task_utils.get_specific_task()` (User selects one task from the list of matches)
    * → `interface.print_tasks()`
    * → `interface.get_user_index()`
7.  → `interface.get_input_date()` (New date input)
8.  → `interface.get_input_description()` (New description input)
9.  → `json_handler.update_entry()` (Locates task in JSON, updates fields, and rewrites file)
10. → `interface.wait_for_user()`
11. → `End` (Returns to main menu)

## ✅ Project Requirements
This project fulfills the criteria for the **Programming Foundations** module:

- [x] **Interactive App:** Console-based menu with dynamic user interaction.
- [x] **Data Validation:** Strict input checking (dates, empty strings, types) using `try-except` blocks.
- [x] **File Processing:** Reads and writes structured JSON data (`task_data.json`) with error handling for file existence and corruption.

---

## 👥 Team & Acknowledgments

**Development Team:**
* **Bernardo Alfonso Suárez Espinoza** (Index function + Testing)
* **Juan Vock** (Edit function + Add function + Architecture)
* **Fernando Mauracher Garcia** (Delete function + Show function)


**Date:**
* 17th December 2025

---

### 📝 License
This project is provided for educational use only as part of the FHNW Programming Foundations module.
[MIT License](LICENSE)
