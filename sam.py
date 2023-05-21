def add_item(my_list, item):
    my_list.append(item)
    print("Item '{}' added to the list.".format(item))


def remove_item(my_list, item):
    if item in my_list:
        my_list.remove(item)
        print("Item '{}' removed from the list.".format(item))
    else:
        print("Item '{}' not found in the list.".format(item))


def display_list(my_list):
    print("List items:")
    if my_list:
        for item in my_list:
            print(item)
    else:
        print("The list is empty.")


def search_item(my_list, item):
    if item in my_list:
        print("Item '{}' found in the list.".format(item))
    else:
        print("Item '{}' not found in the list.".format(item))


def main():
    my_list = []

    while True:
        print("\n----- List Management Menu -----")
        print("1. Add item to the list")
        print("2. Remove item from the list")
        print("3. Display the list")
        print("4. Search for an item in the list")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(my_list, item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(my_list, item)
        elif choice == '3':
            display_list(my_list)
        elif choice == '4':
            item = input("Enter the item to search: ")
            search_item(my_list, item)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == '__main__':
    main()
