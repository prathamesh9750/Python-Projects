def task():
    tasks = [] #Empty list of tasks
    print("\n -------------- Welcome to My To-Do-List App ---------------")
    print("\n --------------- Created by Prathamesh Bhor --------------- ")

    total_tasks = int(input("Enter how many tasks you want to add : "))
    for i in range (1, total_tasks+1):
        task_name = input(f"Enter task {i} : ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")
    while True:
        operation = int(input("Enter :\n1-Add task\n2-Update task\n3-Delete task\n4-View tasks\n5-Exit task manager\n >>> "))
        if operation == 1:
            new_task = input("Enter task you want to add : ")
            tasks.append(new_task)             
            print(f"Task {new_task} has been added sucessfully...")

        elif operation == 2:
            task_update = input("Enter task you want to update: ")
            if task_update in tasks:
                update = input("Enter new task : ")
                ind = tasks.index(task_update) 
                tasks[ind] = update           
                print(f"Updated task {update}")

        elif operation == 3:
            task_delete = input("Enter task you want to delete : ")
            if task_delete in tasks:
                ind = tasks.index(task_delete)
                del tasks[ind]                    
                print(f"Task {task_delete} has been deleted successfully...")

        elif operation == 4:
            print(f"Todays tasks are {tasks}") 

        elif operation == 5:
            print("Closing To-Do-List...")
            break  
        else:
            print("Invalid Input !!")
task()