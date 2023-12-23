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
    # Ask title for the REMOVE Checklist option
    checklist_name = input("Enter the item name you don't need anymore: ")
    # Copy into a new CSV file after checking if its in the original list, else don't copy
    checklist_items = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (checklist_name != row[0]):
                checklist_items.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(checklist_items)
    print("\nDone! That item was removed!")


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
