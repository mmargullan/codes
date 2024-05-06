def show_list(l):
    x = 1
    for i in l:
        print(f"{x}) {i}")
        x = x + 1

def add_item(l):
    x = input("Enter a task: ")
    l.append(x)
    
def del_item(l):
    show_list(l)
    x = int(input("Enter a task number to delete: "))
    del l[x-1]

def create_list():
    l = []
    add_item(l)
    return l


print("Create a to do list")
new_l = create_list()
while True:
    query = input("Enter a command:\n1)show list\n2)add task\n3)delete task: ")
    if query == "1":
        show_list(new_l)
    elif query == "2":
        add_item(new_l)
        print("Updated list:")
        show_list(new_l)
    elif query == "3":
        del_item(new_l)
        print("Updated list:")
        show_list(new_l)
    else:
        break
