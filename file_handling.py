# File Handling Script

# File Creation and Writing to the File
try:
    # Creating or opening the file in write mode ('w')
    with open("my_file.txt", 'w') as file:
        # Writing three lines of text (including strings and numbers)
        file.write("Line 1: Hello, this is Scolah.\n")
        file.write("Line 2: Just wanted you to know that am doing so good.\n")
        file.write("Line 3: Been coding all night I slept @5am till 7am.\n")
    print("File 'my_file.txt' created and written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error during file creation or writing: {e}")

# File Reading and Displaying Contents
try:
    # Opening the file in read mode ('r')
    with open("my_file.txt", 'r') as file:
        content = file.read()  # Reading the entire content
        print("\nReading file contents:")
        print(content)  # Displaying the content on the console

except (FileNotFoundError, PermissionError) as e:
    print(f"Error during file reading: {e}")

# Appending to the File
try:
    # Opening the file in append mode ('a')
    with open("my_file.txt", 'a') as file:
        # Appending three additional lines of text
        file.write("Line 4: I then went to school till 5pm.\n")
        file.write("Line 5: Coding has become my hobby.\n")
        file.write("Line 6: Cant sleep without writing a single code.\n")
    print("New lines appended to 'my_file.txt' successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error during file appending: {e}")

# Reading the file again to display the updated content
try:
    with open("my_file.txt", 'r') as file:
        updated_content = file.read()  # Reading the entire content again
        print("\nUpdated file contents after appending:")
        print(updated_content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error during file reading: {e}")

# Ensuring resources are handled correctly
finally:
    print("\nFile handling operations completed.")
