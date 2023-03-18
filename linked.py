def Introduction():
    print("Enter S: Show Linked List")
    print("Enter I: Insert a Node")
    print("Enter D: Delete a Node")
    print("Enter Q: Quit the program")

def Show_linked_list(options):
    for k,v in linked_list.items():
        print(k,v)
    return True

def Insertion(options):
    usr_inp=int(input())

    def root_node(self,val):
        self.value= val
        self.next = None
        
    
    print(options["linked_list"])
    return True

def Deletion():
    return True

def Default():
    return True

def Quit(options):
    return False

commands ={ "S":Show_linked_list,
            "I":Insertion,
            "D":Deletion,
            "Q":Quit,
            "Default":Default}

prgm_exit = True

print("linked list")
Introduction()

linked_list={}
def __init__()

while prgm_exit:
    print(">",end=" ")
    user_Input = input().upper()
    select_option = user_Input if user_Input in commands else "Default"
    options={"linked_list":linked_list}
    prgm_exit=commands[select_option](options)
    
