# Queue
def introduction():
    print("P : show queue")
    print("I : Enque")
    print("R : Deque")
    print("Q : Terminate Program")


def handleH(options):
    introduction()
    return False


def handleP(options):
    print(options["queue"])
    return False


def handleI(options):
    print("enter the value to be inserted in queue")
    queue = options["queue"]
    try:
        user_value = int(input())
        queue.append(user_value)
    except Exception:
        print("please enter only one correct value")

    return False


def handleR(options):
    print("first value will be removed from the queue")
    queue = options["queue"]
    if len(queue) > 0:
        rem_value = queue[0]
        print(rem_value)
        queue.remove(queue[0])
        return False
    elif print("Nothing in Queue!!"):
        return False


def handleD(options):
    return False


def handleQ(options):
    return True


commands = {
    "I": handleI,
    "R": handleR,
    "Q": handleQ,
    "D": handleD,
    "P": handleP,
    "H": handleH
}

pro_exit = False

queue = []
print("QUEUE")
introduction()
while not pro_exit:
    print(">> ", end="")
    user_inp = input().upper()
    select_commands = user_inp if user_inp in commands else "D"
    options = {"queue": queue}
    pro_exit = commands[select_commands](options)
