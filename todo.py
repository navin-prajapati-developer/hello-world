# To Do List App
todos = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        task = input("Enter task: ")
        todos.append(task)
        print("Task added!")
    
    elif choice == "2":
        if len(todos) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(todos, 1):
                print(str(i) + ". " + task)
    
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        todos.pop(num - 1)
        print("Task deleted!")
    
    elif choice == "4":
        print("Goodbye!")
        break
