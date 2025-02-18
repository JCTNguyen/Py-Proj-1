import csv

csv_filename = "leashes.csv"

def add_leash():
    """Function to add a new leash to the CSV File"""
    type_ = input("Enter the type of leash: ")
    color = input("Enter the leash color: ")
    length = input("Enter the leash length: ")
    
    with open(csv_filename, mode='a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([type_, color, length])
    
    print(" Leash added successfully!\n")
    
def view_leashes():
    """Function to read and display all leashes from the CSV file."""
    with open(csv_filename, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row) #print each row in reader file
            


#sort_leashes_by_length function
import csv    
def sort_leashes_by_length():
    """Reads the CSV file and sorts the leashes by length."""
    file = None
    
    try: 
        file = open(csv_filename, mode="r") #Open CSV file
        reader = csv.reader(file)
        leashes = list(reader) #Convert reader to list
        
        if len(leashes) <= 1:  # If there are no leashes or only one leash
            print("No leash data to sort.")
            return
    
        #Extract header and data separately
        header = leashes [0]
        data = leashes [1:]
    
        # Sort by length (convert to float to handle numerical sorting)
        try:
            data.sort(key=lambda row: float(row[2].replace(" METERS", "").replace("FT", "")))
        except ValueError:
            print("Error: Some leash lengths are not in valid format")
        
        #Display sorted results
        print("\n Leashes sorted by length:")
        print(header) 
        for row in data:
            print(row)
         
    except FileNotFoundError:
        print("Error: File does not exist.")
    
    except Exception as e:
        print(f" Error while sorting leashes: {e}") 
    
    finally:
        if file is not None:
            file.close()
            print(" File closed successfully.")

#interactive menu
while True:
    print("\n Leash Manager - Choose an option:")
    print("1. Add a new leash")
    print("2. View all leashes")
    print("3. Sort leashes by length (ascending)")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        add_leash()
    elif choice == "2":
        view_leashes()
    elif choice == "3":
        sort_leashes_by_length()  # Call the new function
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please enter 1, 2, 3, or 4.\n")
