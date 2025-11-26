#Importing txt files and returning a string
def open_txt(filepath):
    if filepath[len(filepath)-4:] == ".txt":
        with open(filepath, "r") as file:
            data = file.read()
        return data
    else:
        return "Please use a valid txt file"

print(open_txt(""))