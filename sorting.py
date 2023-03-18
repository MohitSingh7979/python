print("\nmethod 1 sorting")
data = [31, 35, 34, 32, 37, 36, 39, 38]
empty = []

for i in range(len(data)):
    min_val = data[0]
    min_ind = 0
    count = 1
    print("Step #", i+1)
    print("assuming ", min_val, "as min.")
    for j in range(1, len(data)):
        if min_val > data[j]:
            print(data[j], "is shorter than our min, so, swapping")
            min_val = data[j]
            print(min_val, "is our new min value")
            min_ind = j
            count = 1
        elif min_val == data[j]:
            count += 1
            print("since it's same as our min, increamenting to ", count)
        else:
            print(min_val, "is already minimum")
    print("overall min value is", min_val)

    for _ in range(count):
        empty.append(min_val)
        print("after appending to sorted list, sorted list:", empty)
        print("unsorted list:", data)
        data.remove(min_val)
        print("after removing, unsorted list: ", data)

    print("----------------------------------------------")


print("\nmethod 2 sorting")
main_list=[7,34,34,34,37]
empList=[]
for i in range(len(main_list)):#5
    if len(main_list)==0:
        break
    min_val=main_list[0]
    count=1
    for j in range(1,len(main_list)):#4
        if min_val>main_list[j]:
            min_val=main_list[j]
            count=1
        elif min_val == main_list[j]:#2
            count+=1
        # print(count,"count")
    for _ in range(count):
        empList.append(min_val)
        main_list.remove(min_val)
        print(empList)

print("\nmethod 3 sorting")
item_list=[7,6,5,4,3,3,3,2,1,7,5,3,1,34,56]
sortedlist=[]
print(item_list,"original list\n")
while len(item_list)>0:
    min_ind=item_list[0]
    for j in range(1,len(item_list)):
        if min_ind>item_list[j]:
            min_ind=item_list[j]
    sortedlist.append(min_ind)
    item_list.remove(min_ind)
print(item_list,":current list")
print(sortedlist,": sorted list\n")
