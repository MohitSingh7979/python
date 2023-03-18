# stack
def show_opts():
    print("P to print the array")
    print("I to push the value or")
    print("R to pop the value")
    print("Q to quit")


def handleR(opts):
    arr = opts["arr"]
    if len(arr) == 0:
        print("stack already empty")
        return False
    arr.reverse()
    print("removed", arr[0])
    arr.remove(arr[0])
    arr.reverse()
    return False


def handleI(opts):
    arr = opts["arr"]
    print("Enter value: ", end="")
    inp = int(input())
    arr.append(inp)
    return False


def handleQ(opts):
    return True


def handleD(opts):
    print("unknown option")


def handleP(opts):
    print(opts["arr"])


def handleH(opts):
    show_opts()


cmds = {'R': handleR, 'I': handleI, 'Q': handleQ,
        'D': handleD, 'P': handleP, 'H': handleH}

will_exit = False

# num if condit else num2

arr = []
print("Cli for Stack")
while not will_exit:
    print("(h for help)> ", end="")
    inp = input().upper()
    cmd = inp if inp in cmds else "D"
    handler = cmds[cmd]
    opts = {"arr": arr}
    will_exit = handler({"arr": arr})