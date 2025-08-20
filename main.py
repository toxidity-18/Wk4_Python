# file handling and exception handling :

try:
    # Ask user for the file name
    file_name = input("Enter the file name to read: ")
    # open and read the file 
    with open(file_name, 'r') as f:
        content = f.read()
    # modification original content inside the file changed to uppercase 
    Content_Upper = content.upper()
    # creating a new file that has the modified content 
    # Modified_Output_ : is the new for our file and does not change the file types 
    with open('Modified_Ouput_'+ file_name, 'w') as f:
        f.write(Content_Upper)
    print(content)
# error when the file is not found 
except FileNotFoundError :
    print("File not found. Please check the file name and try again.")
except Exception as e:  
    print(f"An error occurred: {e}")
else:
    print("File read and modified successfully.")
finally:
    print("Execution completed.")
    