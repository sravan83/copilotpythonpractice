# Task: Read the contents of 'data.txt' and print each line with line numbers

file_path = 'data.txt'

try:
    with open(file_path, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

        # Print each line with line numbers
        for line_number, line in enumerate(lines, start=1):
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
