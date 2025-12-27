def explain_enumerate():
    print("What enumerate does:")
    print(" - enumerate(iterable, start) returns pairs (index, item).")
    print(" - Commonly used to get both index and value in a loop.")
    print()
    sample = ['Buy milk', 'Read book', 'Write code']
    print("Example (using start=1):")
    for i, task in enumerate(sample, start=1):
        print(f"  {i}: {task}")
    print()

def draw_todolist_flow():
    print("To-Do List Application Flow (ASCII):")
    print()
    print("   [Start]")
    print("      |")
    print("      v")
    print("   [Show Menu]")
    print("   1.Add  2.View  3.Delete  4.Exit")
    print("      |")
    print("      v")
    print("  /---Add Task----\\")
    print("  |  append task  |")
    print("  \\---------------/")
    print("      |")
    print("      v")
    print("  /---View Tasks---\\")
    print("  | enumerate(list) |  <- shows index + task")
    print("  \\-----------------/")
    print("      |")
    print("      v")
    print("  /--Delete Task---\\")
    print("  | remove by index |")
    print("  \\-----------------/")
    print("      |")
    print("      v")
    print("    [Exit]")
    print()

def main():
    explain_enumerate()
    draw_todolist_flow()
    print("Run the original todolist.py to interact with the app.")
    print("File: todolist.py")

if __name__ == "__main__":
    main()
