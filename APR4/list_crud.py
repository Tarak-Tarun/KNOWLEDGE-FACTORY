def create_item(lst):
    item = (input("Enter item to add: "))
    lst.append(item)
    print("Item added.")

def read_items(lst):
    if len(lst) == 0:
        print("List is empty.")
    else:
        print("List items:", lst)

def update_item(lst):
    if len(lst) == 0:
        print("List is empty.")
        return
    index = int(input("Enter index to update: "))
    if 0 <= index < len(lst):
        new_value = int(input("Enter new value: "))
        lst[index] = new_value
        print("Item updated.")
    else:
        print("Invalid index.")

def delete_item(lst):
    if len(lst) == 0:
        print("List is empty.")
        return
    index = int(input("Enter index to delete: "))
    if 0 <= index < len(lst):
        lst.pop(index)
        print("Item deleted.")
    else:
        print("Invalid index.")


# Main program
my_list = []

while True:
    print("\n--- MENU ---")
    print("1. Create (Add Item)")
    print("2. Read (Display List)")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_item(my_list)
    elif choice == 2:
        read_items(my_list)
    elif choice == 3:
        update_item(my_list)
    elif choice == 4:
        delete_item(my_list)
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")