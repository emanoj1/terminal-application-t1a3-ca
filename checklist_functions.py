import csv

def add_checklist(file_name):
    # Ask title for the Add Checklist option
    checklist_name = input("Enter the item to carry: ")
    
    # Open the CSV file
    with open(file_name, "a") as f:
        writer = csv.writer(f)
    
    # Insert values - titl = user entered
                    # - Completed = False
        writer.writerow([checklist_name, "False"])
    print("\nDone! Your item is in the travelist!")

def view_checklist(file_name):
    # Ask title for the VIEW Checklist option
    print("\nThese are the items to carry on your trip:\n ")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__() # to skip the header row in the CSV file
        for row in reader:
            if (row[1] == "True"):
                print(f"> {row[0]} packed!") # display message if packed
            else:
                print(f">>> {row[0]} : Yet to pack.") # display message if NOT packed

def remove_checklist(file_name):
    checklist_name = input("Enter the item name you don't need anymore: ") # Ask title for the REMOVE Checklist option
    checklist_items = [] # An empty list to store items from the CSV file
    item_found = False # To keep track of entered items, and see if it exists in the list or not
    
    with open(file_name, "r") as f: # Open CSV file in read mode
        reader = csv.reader(f) # create a reader for the CSV
        for row in reader: # iterate through each row in the file
            if (checklist_name != row[0]): # If input item doesn't match the first item in the list
                checklist_items.append(row) # then append the row into checklist_items 
            else:
                item_found = True # else if it finds a match, set to item_found to True

    with open(file_name, "w") as f: # Open the CSV file
        writer = csv.writer(f) # create a CSV writer
        writer.writerows(checklist_items) # write the updated list by removing the item if it was found

    if item_found:
        print("\nDone! That item was removed!") # When the value is True, it confirms item removal
    else:
        print("\nSorry! Item not in current list. Please view your list and enter the correct item name") #When the value is False, it alerts the user of the absent item

def mark_checklist(file_name):
    checklist_name = input("Which item do you want to mark as packed?: ")
    checklist_items = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if(checklist_name != row[0]):
                checklist_items.append(row)
            else:
                checklist_items.append([row[0], "True"])
    with open(file_name, "w") as f:
        writer  = csv.writer(f)
        writer.writerows(checklist_items)
    print("\nDone! Your chosen item is packed!")
