checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    item = checklist[index]
    return item

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

def mark_completed(index):
    update(index, "√" + checklist[index])
    list_all_items()

def select(function_code):
    # Create item


    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number")

        # Remember that item_index must actually exist or our program will crash.
        print(read(int(item_index)))

    elif function_code == "D":
        index = user_input("Index Number")
        destroy(index)
        list_all_items()

    elif function_code == "U":
        index = user_input("Index Number")
        item = user_input("item")
        update(int(index), item)
        list_all_items()

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def test():
    create("purple sox")
    create("red cloak")
    create("blue Shoes")
    create("yellow pants")
    create("green longsleeve")
    #
    # print(read(0))
    # print(read(1))
    #
    # update(0, "purple socks")
    # destroy(1)
    #
    # print(read(0))
    # list_all_items()

    #user_value = user_input("Please Enter a value:")
    #print(user_value)




test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, Q to stop loop, R to Read from list, D to remove items and P to display list")
    running = select(selection)
