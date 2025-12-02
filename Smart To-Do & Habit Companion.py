
tasks = []
habits = {}
done_habits_today = set()

# ---- TASK ----
def add_task():
    t = input("Enter task: ").strip()
    if t:
        tasks.append({"title": t, "done": False})
        print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks.")
        return
    for i, t in enumerate(tasks, 1):
        s = "Done" if t["done"] else "Not done"
        print(f"{i}. {t['title']} - {s}")

def mark_task_done():
    view_tasks()
    if not tasks:
        return
    num = input("Enter task number: ")
    if num.isdigit():
        num = int(num)
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked done.")
        else:
            print("Invalid number.")

# ---- HABITS ----

def add_habit():
    h = input("Enter habit: ").strip()
    if h and h not in habits:
        habits[h] = 0
        print("Habit added.")

def view_habits():
    if not habits:
        print("No habits.")
        return
    for h, s in habits.items():
        print(f"{h} -  Streak {s}")

def mark_habit_done():
    if not habits:
        print("No habits.")
        return
    view_habits()
    h = input("Which habit done today? ")
    if h in habits:
        if h not in done_habits_today:
            habits[h] += 1
            done_habits_today.add(h)
            print("Habit marked done.")
        else:
            print("Already done today.")
    

# ---- INSIGHT ----

def daily_insight():
    if not tasks and not habits:
        print("No data.")
        return

    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    task_score = int((done / total) * 100) if total else 0
    habit_points = len(done_habits_today)
    score = (task_score + habit_points * 10) // 2

    print("\n--- DAILY INSIGHT --")
    print("Task completion:", task_score, "%")
    print("Habits completed today:", habit_points)
    print("Wellness Score:", score, "/100")

# ---- MENU ----

def menu():
    while True:
        print("New day started for Task and Habits")
        print("1.Add Task  2.View Tasks  3.Task Done")
        print("4.Add Habit 5.View Habits 6.Habit Done")
        print("7.Daily Insight 8.Exit")

        ch = input("Choice: ")

        if ch == "1": 
            add_task()
        elif ch == "2": 
            view_tasks()
        elif ch == "3": 
            mark_task_done()
        elif ch == "4": 
            add_habit()
        elif ch == "5": 
            view_habits()
        elif ch == "6": 
            mark_habit_done()
        elif ch == "7": 
            daily_insight()
        elif ch == "8":
            print("Bye and stay healthy")
            break
        else:
            print("Invalid choice.")

menu()