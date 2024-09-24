# Step 1: Create a list of 5 numbers
numbers = [12, 7, 5, 18, 10]
print("Original List:", numbers)

# Step 2: Add an element to the list
numbers.append(25)
print("List after adding an element:", numbers)

# Step 3: Remove an element from the list
numbers.remove(7)  # Remove the element with value 7
print("List after removing an element:", numbers)

# Step 4: Find the maximum and minimum numbers in the list
max_value = max(numbers)
min_value = min(numbers)

print("Maximum number in the list:", max_value)
print("Minimum number in the list:", min_value)

#===========================================================================

# Given list of fruits
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

# 1. Add a fruit to the list
fruits.append('grape')
print("After adding a fruit:", fruits)

# 2. Remove a fruit from the list
fruits.remove('banana')
print("After removing a fruit:", fruits)

# 3. Find the length of the list
print("Number of fruits in the list:", len(fruits))

# 4. Find the first fruit in the list (alphabetically)
print("First fruit alphabetically:", min(fruits))

# 5. Find the last fruit in the list (alphabetically)
print("Last fruit alphabetically:", max(fruits))

# Given list of fruits
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

# Access the first element
first_fruit = fruits[0]
print("First fruit:", first_fruit)

# Access the middle element(s)
middle_index = len(fruits) // 2
if len(fruits) % 2 == 0:
    middle_fruit = fruits[middle_index - 1:middle_index + 1]  # If list length is even, get two middle elements
else:
    middle_fruit = fruits[middle_index]  # If list length is odd, get the single middle element
print("Middle fruit(s):", middle_fruit)

# Access the last element
last_fruit = fruits[-1]
print("Last fruit:", last_fruit)

# Change the second element to 'blueberry'
fruits[1] = 'blueberry'
print("List after changing second fruit:", fruits)


#======================================================================


# Function to take input from user, sort names, and print the sorted list
def sort_student_names():
    # Input: Accept a list of student names from the user
    student_names = input("Enter the student names, separated by commas: ").split(',')

    # Remove any leading/trailing whitespace from names
    student_names = [name.strip() for name in student_names]

    # Sort the list of names in alphabetical order
    sorted_names = sorted(student_names)

    # Output: Print the sorted list of names
    print("Sorted list of student names:")
    for name in sorted_names:
        print(name)

# Call the function
sort_student_names()

#=============================================================================================


# Function to process a list of integers
def process_integers():
    # Input: Accept a list of integers from the user (comma-separated)
    int_list = list(map(int, input("Enter integers separated by commas: ").split(',')))

    # Print the first 3 elements (if the list has at least 3 elements)
    first_3 = int_list[:3]
    print("First 3 elements:", first_3)

    # Print the last 2 elements (if the list has at least 2 elements)
    last_2 = int_list[-2:]
    print("Last 2 elements:", last_2)

    # Print the entire list in reverse order
    reversed_list = int_list[::-1]
    print("List in reverse order:", reversed_list)

# Call the function
process_integers()

#===========================================================================================


# Function to remove duplicates from a list
def remove_duplicates():
    # Input: Accept a list of elements from the user (comma-separated)
    elements = input("Enter the list elements separated by commas: ").split(',')

    # Remove any leading/trailing whitespace from each element
    elements = [element.strip() for element in elements]

    # Convert the list to a set to remove duplicates, then convert back to a list
    unique_elements = list(set(elements))

    # Output: Print the new list without duplicates
    print("List without duplicates:", unique_elements)

# Call the function
remove_duplicates()

#=================================================================================================

# Given dictionary of student details
student = {'name': 'John', 'age': 22, 'grade': 'B'}

# Update the 'grade' value to 'A'
student['grade'] = 'A'

# Add a new key-value pair for 'major'
student['major'] = 'Computer Science'

# Output: Print the updated dictionary
print("Updated student dictionary:", student)

#================================================================================================

# Function to create a dictionary of subjects and their marks
def calculate_average_marks():
    # Create a dictionary to hold subjects and their corresponding marks
    subjects = {
        'Math': [],
        'Science': [],
        'English': []
    }

    # Input marks for each subject
    for subject in subjects.keys():
        marks_input = input(f"Enter marks for {subject} separated by commas: ")
        # Split the input into a list and convert to integers
        marks = list(map(int, marks_input.split(',')))
        subjects[subject] = marks

    # Calculate and print the average marks for each subject
    for subject, marks in subjects.items():
        if marks:  # Check if there are any marks to avoid division by zero
            average = sum(marks) / len(marks)
            print(f"Average marks for {subject}: {average:.2f}")
        else:
            print(f"No marks entered for {subject}.")

# Call the function
calculate_average_marks()
