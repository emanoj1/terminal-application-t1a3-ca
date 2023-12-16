import csv

def add_checklist(file_name):
    print("Add checklist")
    # Ask title for the Add Checklist option
    checklist_name = input("Enter the item to carry: ")
    
    # Open the CSV file
    with open(file_name, "a") as f:
        writer = csv.writer(f)
    
    # Insert values - titl = user entered
                    # - Completed = False
        writer.writerow([checklist_name, "False"])

def view_checklist(file_name):
    print("View item")

def remove_checklist(file_name):
    print("Remove item")

def mark_checklist(file_name):
    print("Mark item")

