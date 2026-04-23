def show_menu():
    print("\n---TO-DO-LIST---")
    print("1. View Tasks")
    print("2. Task Addition")
    print("3. Task Completed")
    print("4. Clear Tasks")
    print("5. Exit")


tasks = []
try:
    with open("tasks.txt", "r") as f:
        tasks = [line.strip() for line in f]
except FileNotFoundError:
    tasks = []

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")

    elif choice == "2":
        new_task = input("Enter the task: ")
        tasks.append(new_task)

        with open("tasks.txt", "a") as f:
            f.write(new_task + "\n")
        print("Task added!")

    elif choice == "3":
        tasks.clear()
        open("tasks.txt", "w").close()
        print("All tasks cleared!")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid option, please try again.")
