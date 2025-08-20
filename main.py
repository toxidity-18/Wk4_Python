# file handling and exception handling :

try:
    # Ask user for the file name
    file_name = input("Enter the file name to read: ")
# error when the file is not found 
except FileNotFoundError :
    print("File not found. Please check the file name and try again.")
