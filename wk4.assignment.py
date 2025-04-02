# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
# # Ask the user for the input file name

#creating the file
with open("sample.txt", "w") as file:
    file.write("Hello, world!")
input_file = input("Enter the name of the file to read: ")

try:
    # Open the input file in read mode
    with open(input_file, 'r') as file:
        # Read the content of the file
        content = file.read()

    # Modify the content (e.g., convert it to uppercase)
    modified_content = content.upper()

    # Ask the user for the output file name
    output_file = input("Enter the name of the file to write the modified content: ")

    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Write the modified content to the new file
        file.write(modified_content)

    print(f"Modified content has been written to {output_file}")

except FileNotFoundError:
    # Handle the case where the input file does not exist
    print("Error: The file you specified does not exist.")
except Exception as e:
    # Handle other unexpected errors
    print(f"An error occurred: {e}")
