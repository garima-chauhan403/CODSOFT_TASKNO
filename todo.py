# To-Do List App

tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(i, task)

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted!")
        else:
            print("Invalid task number")

    elif choice == "4":
        print("Program closed")
        break

    else:
        print("Wrong choice")