# Error Handling Lab

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("❌ Error: File not found.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print("❌ An unexpected error occurred:", e)





 

