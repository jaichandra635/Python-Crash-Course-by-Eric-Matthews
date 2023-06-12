'''Guest List: If you  could invite anyone, living or deceased, to dinner, who would you invite?
make a list that includes at least three people you'd like to invite to dinner. then use your list
to print a message to each person, inviting them to dinner'''

'''3.4 Guest List'''
guest_list = ['prabhas', 'ram charan', 'ntr', 'inoni']
for guest in guest_list:
    print(guest)

print("\n")

'''3.5 Changing Guest List'''
print(f"{guest_list[0]}, can't make it today.")
print("\n")

guest_list[0] = 'ravi teja' #replacing prabhas which is the index of 0 with ravi teja

print(guest_list)
print("\n")

print("found a bigger dinner table, new guests are being invited.")

print("\n")
'''3.6 More Guests'''
guest_list.insert(0, 'mahesh')
guest_list.insert(3, 'sunil')
guest_list.append('kiran')

for guest in guest_list:
    print(f"mr.{guest}, you are being invited for tonights dinner.")

'''3.7 Shrinking Guest List:'''

print("\n")
print("I can invite only two people for dinner.")
guest_list.pop(0)
guest_list.pop(1)
guest_list.pop(2)
guest_list.pop(3)
guest_list.pop(1)
print(guest_list)

print("\n")

for guest in guest_list:
    print(f"mr.{guest}, you are being invited for dinner tonight")

del guest_list[0]
del guest_list[0]
print(guest_list)