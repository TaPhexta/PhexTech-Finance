# PhexTech Task Manager

This project started as an exercise in building a secure, multi-user system from scratch. Initially, I planned to build a full banking application, but I decided to pivot to a Task Manager first. This allowed me to master the core logic—authentication, data persistence, and CRUD operations—before moving on to more complex financial systems.

## 🚀 The Build
The goal was to create a terminal-based app that felt like a real-world application. I focused on three main areas:

* **Security & UX:** Mimicking real-world login flows by using `maskpass` for starred PIN entry and enforcing strict validation rules for 6-digit PINs (preventing simple repeating patterns).
* **Data Architecture:** Using a centralized `tasks.json` file to handle data. I structured the logic to ensure that while multiple users can exist in the system, they can only access and modify their own unique set of tasks.
* **Persistent CRUD:** Building out the ability to Create, Read, Update, and Delete tasks, ensuring every change is immediately saved so no data is lost when the app closes.

## 🛠 Features
- **Smart User Generation:** Automatically suggests usernames based on the user's name.
- **Task Metadata:** Every task supports a description (limited to 50 chars for clean UI) and a specific due time.
- **Dynamic Status:** Visual "✅/❌" toggles to track progress within the terminal.
- **Error Handling:** Built-in checks to handle invalid inputs, non-existent task numbers, and authentication failures.

## 💻 Tech Stack
- **Language:** Python 3
- **Storage:** JSON (File-based persistence)
- **Libraries:** `maskpass` (for secure input)

## 🧠 What I Learned
Building this pushed me to think about how data flows between a user interface (`main.py`) and the underlying logic (`tasks.py`). Solving "variable shadowing" issues and managing the math between 1-based user input and 0-based Python lists were key learning moments that have prepared me for my next, larger project.

## 🔜 Future Roadmap
Now that the foundation is solid, I'm looking to add:
- **Search Functionality:** Finding tasks by keyword for better navigation.
- **Task Categories:** Sorting items into "Work," "Personal," or "Urgent."
- **Export to CSV:** Allowing users to download their task list for external use.

---
*Created as part of my Software Development portfolio.*