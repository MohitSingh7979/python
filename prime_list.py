check = int(input("Enter the Number:-"))

prime_list = []

for n in range(2,check):
    prime = True
    for i in range(2,n):
        if (n%i) == 0:
            prime = False
            break
    
    if prime:
        prime_list.append(n)

print(prime_list)