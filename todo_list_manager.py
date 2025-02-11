# A simple to-do list manager: add, remove, and view tasks.

todo_list = ['Take out the trash', 'Walk the dog', 'Pay for internet']
todo_list.sort()

print("\n".join(todo_list))

while True:
    choice = input("Choose an option: add, delete, exit: \n").strip().lower()

    match choice:
        case "add":
            print("Enter a new task: ")
            new = input().strip()
            if new in todo_list:
                print("Already in the list")
            else:
                todo_list.append(new)
                todo_list.sort()
                print("\n".join(todo_list))

        case "delete":
            print("Which task number do you want to delete?")
            delete_index = int(input().strip()) - 1
            if 0 <= delete_index < len(todo_list):
                todo_list.pop(delete_index)
                print("\n".join(todo_list))
            else:
                print("Invalid task number")

        case "exit":
            print("Exiting the program")
            break

        case _:
            print("Invalid choice. Please select one of the options: add, delete, exit")
