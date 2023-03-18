num = int(input("Enter the Number:- "))

if num <= 1:
    print("Number is not Prime ", num)
elif num > 1:
    for a in range(2, num):
        if num%a == 0:
            print("Number is not Prime ", num)
            break
    else:
        print("Number is Prime ", num)