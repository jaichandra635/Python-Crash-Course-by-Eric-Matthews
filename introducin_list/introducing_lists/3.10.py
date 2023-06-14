'''3.10 Every fuction: '''

# Create a list of famous landmarks
landmarks = ['Eiffel Tower', 'Great Wall of China', 'Taj Mahal', 'Pyramids of Giza', 'Machu Picchu']

# Print the original list
print("Original List:", landmarks)

# Append a new landmark to the list
landmarks.append('Statue of Liberty')
print("After Append:", landmarks)

# Insert a landmark at a specific position
landmarks.insert(2, 'Colosseum')
print("After Insert:", landmarks)

# Remove a landmark from the list
landmarks.remove('Taj Mahal')
print("After Remove:", landmarks)

# Sort the list in alphabetical order
landmarks.sort()
print("After Sort:", landmarks)

# Reverse the order of the list
landmarks.reverse()
print("After Reverse:", landmarks)

# Get the index of a specific landmark
index = landmarks.index('Pyramids of Giza')
print("Index of 'Pyramids of Giza':", index)

# Count the occurrences of a landmark in the list
count = landmarks.count('Eiffel Tower')
print("Count of 'Eiffel Tower':", count)

# Check if a landmark is in the list
is_present = 'Machu Picchu' in landmarks
print("'Machu Picchu' is present:", is_present)

# Get the length of the list
length = len(landmarks)
print("Length of the list:", length)
