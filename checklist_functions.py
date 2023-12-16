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
    # Ask title for the Add Checklist option
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
    # Ask title for the Add Checklist option
    checklist_name = input("Remove the items you longer need to carry: ")

def mark_checklist(file_name):
    # Ask title for the Add Checklist option
    checklist_name = input("If packed, mark the items as complete: ")

