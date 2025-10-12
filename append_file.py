
first_data = input("Enter some text to write into the file: ")
with open("output.txt", "w") as file:
    file.write(first_data + "\n")
print("first line written to output.txt successfully.")
Second_data = input("Enter Second line text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(Second_data + "\n")
print("Second line appended successfully.")
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
