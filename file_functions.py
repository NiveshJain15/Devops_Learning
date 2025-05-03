def create_and_write_to_file():
    # Ask user for filename
    filename = input("Enter the filename to create (include .txt extension): ")
    
    try:
        # Open file in write mode ('w')
        # This will create the file if it doesn't exist or overwrite it if it does
        with open(filename, 'w') as file:
            print(f"File '{filename}' opened for writing.")
            
            # Ask user for content to write
            print("Enter the content to write to the file.")
            print("Type 'END' on a new line when you're done:")
            
            # Collect content lines until user enters 'END'
            content_lines = []
            while True:
                line = input()
                if line == 'END':
                    break
                content_lines.append(line)
            
            # Join all lines with newline characters and write to file
            content = '\n'.join(content_lines)
            file.write(content)
            
            print(f"Content successfully written to '{filename}'.")
    
    except IOError as e:
        print(f"Error: Could not write to file. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    print("File operation completed.")

# Run the program
if __name__ == "__main__":
    create_and_write_to_file()