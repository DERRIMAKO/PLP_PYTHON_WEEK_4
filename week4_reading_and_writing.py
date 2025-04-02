# This program reads a file, modifies its content, and writes it to a new file.
def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            content = file.read()
            print(content)

            modified_content = content.upper() #modify content

        with open("modified.txt", "w") as file:
            file.write(modified_content) # write content to a new file

            print("Modified document saved as 'modified.txt'")

    except FileNotFoundError:
        print("Error: 'original.txt' not found.")
    except Exception:
        print("Error: an expected error occured")

# Run the function
modify_file('original.txt', 'modified.txt')

