import os

# Function to get a valid file path from the user
def get_file_path():
    while True:
        file_path = input("Enter or copy paste the full path of the file to read eg C:/Users/YourName/Downloads\sample_test_file.txt): ")
        if os.path.exists(file_path):  # Check if the file exists
            return file_path
        else:
            print("File not found. Please check the path and try again.")

# Main Program
def main():
    filename = get_file_path()

    try:
        with open(filename, "r") as file:
            content = file.read()

        # Simple modification: make everything uppercase
        modified = content.upper()

        with open("modified.txt", "w") as new_file:
            new_file.write(modified)

        print("File modified and saved as 'modified.txt'.")

    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
