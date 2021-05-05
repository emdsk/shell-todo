def main():
    welcome_message()
    username = input("Shell User Name: ")
    print("Welcome " + username)
    showMenu()

def welcome_message():
    print("----------------------------------------------------------------------------")
    print("")
    print("                         Shell Todo Welcomes you")
    print("")
    print("----------------------------------------------------------------------------")
    print("")
    print("                 The Best Place To Maintain All Your Tasks")
    print("")


user_input = 'random'
#create a list
data=list()
completed_task = list() 


#we are going to create 4 options
#1.Add an item
#2.Delete an item
#3.Mark as done
#4.View items
#5.Completed and Incompleted tasks
#5.Exit

def showMenu():
    print("Menu:")
    print("1. Add an item:")
    print("2. Delete an item:")
    print("3. Mark as Done:")
    print("4. View Items:")
    print("5. Modify Task")
    print("6. Exit:")

    def print_task():
            i=1
            j=1
            print("List of incomplete Items: ")
            for item in data:
                print(i, " ",item)
                i+=1
            print("List of completed items: ")
            for item in completed_task:
                print(j,item)
                j+=1
    
    while True:
        user_input = input("Enter your CHOICES: ")

        if user_input == '1':
            item = input("What is to be done ? ")
            data.append(item)
            print("Added item ",item)
            print_task()
            showMenu()
            
        elif user_input == '2':
            print_task()
            item1 = int(input("Whatis to be removed: "))
            print("Removed item ", data[item1-1])
            del data[item1-1]
            
            showMenu()
        elif user_input == '3':
            print_task()
            item = int(input("What is to be marked as done? "))
            #if item is present in data
            if data[item-1] in data:
                completed_task.append(data[item-1])   
                data.remove(data[item-1])
                print("Marked as done:",item)
            else:
                print("Item does not exist is the to-do list")
            print_task()
            showMenu()
        elif user_input == '4':
            print_task()
            
        elif user_input == "5":
            item = int(input("Enter the item to be modified: "))
            if data[item-1] in data:
                new_item = input("Enteer the new to be replaced: ")
                data[item - 1] = new_item
            else:
                print("Index out of bound.")
            print_task()
            showMenu()
        elif user_input == '6':
                 print("See you Again With Different Tasks") 
                 break                   
 
main()