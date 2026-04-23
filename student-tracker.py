students = {}

# Load existing data from file on start
try:
    with open("scores.txt", "r") as f:
        for line in f:
            name, score = line.strip().split(",")
            students[name] = int(score)
    print("Loaded existing scores from scores.txt")
except FileNotFoundError:
    print("No save file found. Starting fresh.")

while True:
    print("--- Student Tracker ---")
    print("1. Add/Update Student")
    print("2. Show All Scores")
    print("3. Show Statistics")
    print("4. Save to File")
    print("5. Exit")
    choice = input("What would you like to do? ")

    if choice == "1":
        name = input("Enter full name: ")
        try:
            score = int(input("Enter score: "))
            students[name] = score
            print(f"Added {name}!")
        except ValueError:
            print("Invalid score. Please enter a number.")

    elif choice == "2":
        if not students:
            print("No students yet!")
        else:
            print("--- Current Streak ---")
            for name in students:
                print(f"{name}: {students[name]}")

    elif choice == "3":
        if not students:
            print("No data yet!")
        else:
            all_scores = students.values()
            avg = sum(all_scores) / len(all_scores)
            print(f"Average: {avg:.1f}")
            print(f"Highest: {max(all_scores)}")
            print(f"Lowest: {min(all_scores)}")

    elif choice == "4":
        with open("scores.txt", "w") as f:
            for name, score in students.items():
                f.write(f"{name},{score}\n")
        print("Saved to scores.txt")

    elif choice == "5":
        break
