#define a list to carry my tasks
ToDoList = []
#define a list to carry TasksFinished
TasksFinished =[]
#define a list to carry TasksNotFinished
TasksNotFinished =[]

#message for the user and ask him to enter the today tasks
ToDoList = input("Enter your tasks for today separated by a comma: ").lower().split(", ")

#looping on the list which carring today tasks
for Task in ToDoList:
    #check on the list elements
    print(Task)
    #user decision finished or not finished
    UserDecision= input(f"Did you finish {Task} already?\n").lower()

    if UserDecision == "yes":
        #task finished
        print("Nice Job")
        print("_____________")
        #add it into TasksFinished list
        TasksFinished.append(Task)
    else:
        # task not finished
        print("Try not to put it off")
        print("_____________")
        # add it into TasksNotFinished list
        TasksNotFinished.append(Task)

#message for the user and ask him to enter if he/she want to  see your today's progress
ToDayProgress = input("Do you want to see your today's progress?(yes,no)\n").lower()
if ToDayProgress == "yes":
    #if user want to see
    print("*********** Done Tasks ***********\n")
    print(TasksFinished)
    print()
    print("*********** Ongoing Tasks ***********\n")
    print(TasksNotFinished)
else:
    # if user does not want to see
    input("please hit enter to exit")





