# Simple To-Do List Application 
# --> process of todolist : 
    # add task 
    # view tasks 
    # delete task
    # exit 

def main():
    todolist = []

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todolist.append(task)
            print(f'Task "{task}" added.')

        elif choice == '2':
            if not todolist:
                print("No tasks in the list.")
            else:
                print("Tasks:")
                for idx, task in enumerate(todolist, start=1):
                    print(f"{idx}. {task}")

        elif choice == '3':
            if not todolist:
                print("No tasks to delete.")
            else:
                print("Tasks:")
                for idx, task in enumerate(todolist, start=1):
                    print(f"{idx}. {task}")
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(todolist):
                    removed_task = todolist.pop(task_num - 1)
                    print(f'Task "{removed_task}" deleted.')
                else:
                    print("Invalid task number.")

        elif choice == '4':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
if __name__ == "__main__":
    main()
    