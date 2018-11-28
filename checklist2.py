checklist = list()
# checklist.append('blue')
# print(checklist)
# checklist.append('orange')
# print(checklist)

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

# checklist = ['blue', 'orange']
# checklist[1] = 'cats'
# print(checklist)

def update (index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

# checklist = ['blue', 'cats']
# checklist.pop(1)
# print(checklist)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    return input(prompt).upper()

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)
        return True
    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number? ")
        # Remember that item_index must exsit or it will crash.
        read(int(item_index))
        return True
    elif function_code == "U":
        item_index = user_input("Index Number? ")
        input_item = user_input("Edit item: ")
        update(int(item_index), input_item)
        return True
    elif function_code == "D":
        item_index = user_input("Index Number? ")
        destroy(int(item_index))
        return True
    # Print all items
    elif function_code == "P":
        list_all_items()
        return True
    #Quit game
    elif function_code == "Q":
        return False
    # Catch all
    else:
        print("Unknown Option")
        return True

def test():
    create("purple sox")
    create("red cloak")

    print(list_all_items())
    print(read(0))
    print(read(1))

    update(0, "purple socks")

    print(list_all_items())
    destroy(1)

    print(list_all_items())
test()

running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, U to update list item, D to delete list item, P to display list, and Q to quit: ")
    running = select(selection)