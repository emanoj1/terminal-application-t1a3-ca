from checklist_functions import add_checklist, view_checklist, remove_checklist, mark_checklist

#Welcome message
print("\nWelcome to your Travel Checklist!")
print("Keep a track of what to take and don't miss a thing!!")
print("Let's get started...")

#Set and Display Menu items to user
def create_menu_list():
    print("\n1. Add item - Enter 1")
    print("2. View item - Enter 2")
    print("3. Remove item - Enter 3")
    print("4. Mark item - Enter 4")
    print("5. Exit - Enter 5")
    menu_choice = input("\nEnter your selection: ") #menu_choice is a local variable
    return(menu_choice)

#create a global variable to get the value from the menu items selection from the user. By default it is an empty string.
user_choice_menu = ""

#Begin the execution of the choice as a loop, as long as the selection isn't "5 - Exit" 
while user_choice_menu != "5":
    user_choice_menu = create_menu_list()
    if (user_choice_menu == "1"):
        add_checklist()
    elif (user_choice_menu == "2"):
        view_checklist()
    elif (user_choice_menu == "3"):
        remove_checklist()
    elif (user_choice_menu == "4"):
        mark_checklist()
    elif (user_choice_menu == "5"):
        continue # will skip next line and continue with the loop
    else:
        print("\nInvalid input - Choose a number between 1-5 only.")

print("Thank you for using Travel Checklist! Bon Voyage!")