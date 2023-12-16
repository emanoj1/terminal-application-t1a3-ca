from checklist_functions import add_checklist, view_checklist, remove_checklist, mark_checklist

file_name = "travel-checklist.csv"

try:
    # Open file in Read mode
    todo_file = open(file_name, "r")
    todo_file.close()
    print("In try block")
    # if error, file doesn't exist (go to Except block)
    # if no error, file exists
except FileNotFoundError:
    # Since file doesn't exist, create the file and insert the first line into the file
    todo_file = open(file_name, "w")
    todo_file.write("ITEM,COMPLETED")
    todo_file.close()
    print("In except block")

#Welcome message
print("\nWelcome to your Travel Checklist!")
print("Keep a track of what to take and don't miss a thing!!")
print("Let's get started...")

#Set and Display Menu items to user
def create_menu_list():
    print("\n1. Add a new item - Enter 1")
    print("2. View added items - Enter 2")
    print("3. Remove items - Enter 3")
    print("4. Mark item as packed - Enter 4")
    print("5. Exit the menu - Enter 5")
    menu_choice = input("\nEnter your selection: ") #menu_choice is a local variable
    return(menu_choice)

#create a global variable to get the value from the menu items selection from the user. By default it is an empty string.
user_choice_menu = ""

#Begin the execution of the choice as a loop, as long as the selection isn't "5 - Exit" 
while user_choice_menu != "5":
    user_choice_menu = create_menu_list()
    if (user_choice_menu == "1"):
        add_checklist(file_name)
    elif (user_choice_menu == "2"):
        view_checklist(file_name)
    elif (user_choice_menu == "3"):
        remove_checklist(file_name)
    elif (user_choice_menu == "4"):
        mark_checklist(file_name)
    elif (user_choice_menu == "5"):
        continue # will skip next line and continue with the loop
    else:
        print("\nInvalid input - Choose a number between 1-5 only.")

print("Thank you for using Travel Checklist! Bon Voyage!")
print("\n")