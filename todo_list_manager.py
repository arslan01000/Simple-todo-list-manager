# A simple to-do list manager: add, remove, and view tasks.

todo_list = ['Take out the trash', 'Walk the dog', 'Pay for internet']

todo_list_sorted = sorted(todo_list)
print("\nYour to-do list:")

if len(todo_list_sorted) > 0:
    print(f"1. {todo_list_sorted[0]}")
if len(todo_list_sorted) > 1:
    print(f"2. {todo_list_sorted[1]}")
if len(todo_list_sorted) > 2:
    print(f"3. {todo_list_sorted[2]}")
if len(todo_list_sorted) > 3:
    print(f"4. {todo_list_sorted[3]}")
if len(todo_list_sorted) > 4:
    print(f"5. {todo_list_sorted[4]}")

action = input("\nChoose an action: add (1), remove (2), or exit (3): ").strip()

if action == "1":
    new_task = input("Enter a new task: ").strip().capitalize()

    match new_task.lower():
        case task if len(todo_list) > 0 and task == todo_list[0].lower():
            print("This task is already in the list!")
        case task if len(todo_list) > 1 and task == todo_list[1].lower():
            print("This task is already in the list!")
        case task if len(todo_list) > 2 and task == todo_list[2].lower():
            print("This task is already in the list!")
        case task if len(todo_list) > 3 and task == todo_list[3].lower():
            print("This task is already in the list!")
        case task if len(todo_list) > 4 and task == todo_list[4].lower():
            print("This task is already in the list!")
        case _:
            todo_list.append(new_task)
            print(f"Task '{new_task}' added to the list!")

    todo_list_sorted = sorted(todo_list)
    print("\nYour to-do list:")
    if len(todo_list_sorted) > 0:
        print(f"1. {todo_list_sorted[0]}")
    if len(todo_list_sorted) > 1:
        print(f"2. {todo_list_sorted[1]}")
    if len(todo_list_sorted) > 2:
        print(f"3. {todo_list_sorted[2]}")
    if len(todo_list_sorted) > 3:
        print(f"4. {todo_list_sorted[3]}")
    if len(todo_list_sorted) > 4:
        print(f"5. {todo_list_sorted[4]}")

elif action == "2":
    task_number = int(input("Enter the task number to remove: "))
    todo_list_sorted = sorted(todo_list)

    if task_number == 1 and len(todo_list_sorted) > 0:
        todo_list.remove(todo_list_sorted[0])
    elif task_number == 2 and len(todo_list_sorted) > 1:
        todo_list.remove(todo_list_sorted[1])
    elif task_number == 3 and len(todo_list_sorted) > 2:
        todo_list.remove(todo_list_sorted[2])
    elif task_number == 4 and len(todo_list_sorted) > 3:
        todo_list.remove(todo_list_sorted[3])
    elif task_number == 5 and len(todo_list_sorted) > 4:
        todo_list.remove(todo_list_sorted[4])
    else:
        print("Invalid number! Please try again.")

    todo_list_sorted = sorted(todo_list)
    print("\nYour to-do list:")
    if len(todo_list_sorted) > 0:
        print(f"1. {todo_list_sorted[0]}")
    if len(todo_list_sorted) > 1:
        print(f"2. {todo_list_sorted[1]}")
    if len(todo_list_sorted) > 2:
        print(f"3. {todo_list_sorted[2]}")
    if len(todo_list_sorted) > 3:
        print(f"4. {todo_list_sorted[3]}")
    if len(todo_list_sorted) > 4:
        print(f"5. {todo_list_sorted[4]}")

elif action == "3":
    print("Exiting the program. Goodbye!")

else:
    print("Invalid input. Program terminated.")
