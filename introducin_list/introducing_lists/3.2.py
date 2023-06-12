''' Greetings: Start with the list you used in Exercise 3.1, but insted of just
printing each person's name, print a message to them. the text of each message
should be the same, but each message should be personalized with the person's name.'''

names = ['joey', 'jhonny', 'sinny']
print(f"Hi {names[0]}, How are you ?")
print(f"Hi {names[1]}, How are you ?")
print(f"Hi {names[2]}, How are you ?")

print("\n")

#or
#approach 2
# Creating list called names
names = ['joey', 'jhonny', 'sinny']
for name in names:
    print(f"Hi {name}, How are you doing ?")

